"""
数据生成脚本：用教师模型（qwen3.6-plus）生成结构化提取训练数据
运行方式：在 p2_构造大模型问答系统/ 目录下执行 python3 resources/4_1/generate_data.py
特性：增量写入，中断后可续跑，自动跳过已有数据，并行 API 调用
目标：1000 条训练 + 200 条测试，多意图 ~30%，路由分布均衡
"""
import os, sys, json, time, re, random
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
key_path = os.path.join(base_dir, '..', 'Key.json')
with open(key_path, 'r') as f:
    api_key = json.load(f)["DASHSCOPE_API_KEY"].strip()
os.environ["DASHSCOPE_API_KEY"] = api_key

from openai import OpenAI
client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

TEACHER_MODEL = "qwen3.6-plus"
TARGET_TOTAL = 1400  # 1000 train + 200 test + 余量
TEST_SIZE = 200

out_dir = os.path.dirname(os.path.abspath(__file__))
RAW_FILE = os.path.join(out_dir, "raw_samples.jsonl")  # 增量存储，中断安全

SYSTEM_PROMPT = """你是一个请求理解助手。分析用户的提问，提取结构化工单信息。

严格按以下 JSON 格式输出，不要输出任何其他内容：

{
  "intents": ["意图"],
  "department": "部门",
  "urgency": "紧急度",
  "entities": {},
  "route": "路由"
}

字段取值范围：
- intents（可多选）：入职办理、考勤请假、差旅申请、报销催办、年假查询、IT支持、权限申请、制度咨询
- department：HR、行政、IT、财务
- urgency：高、中、低
- entities：从提问中提取的关键参数（日期、金额、人名、地点、系统名称等），如无则为空对象 {}
- route：direct_answer（简单事实问题）、rag_query（需要查阅政策文档）、multi_intent_split（包含多个独立意图）、escalate（需要人工介入）"""

VALID_INTENTS = {"入职办理", "考勤请假", "差旅申请", "报销催办", "年假查询", "IT支持", "权限申请", "制度咨询"}
VALID_DEPARTMENTS = {"HR", "行政", "IT", "财务"}
VALID_URGENCY = {"高", "中", "低"}
VALID_ROUTES = {"direct_answer", "rag_query", "multi_intent_split", "escalate"}

BRAND_CONSTRAINT = "注意：场景中涉及的系统、工具、平台只能使用虚拟名称或阿里系产品（如钉钉、阿里云、通义千问、夸克等），严禁提及任何非阿里旗下的真实公司或产品名称（包括但不限于微软、谷歌、百度、腾讯、华为、苹果、字节跳动及其旗下产品）。"

QUERY_PROMPTS = [
    # A1: 单意图 - 简单事实问题（direct_answer）
    f"""请生成25条不同员工向公司内部答疑机器人提出的简单事实性问题。要求：
1. 全部是单一意图的简单问题，可以直接回答，不需要查政策文档
2. 覆盖场景：IT支持（WiFi密码、打印机位置）、考勤请假（打卡时间）、年假查询（剩余天数）、制度咨询（办公室地址、工位安排）
3. 表达风格多样：正式、口语化、简短提问
4. 包含具体细节（楼层、部门名、时间等）
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",

    # A2: 单意图 - 需查政策（rag_query）
    f"""请生成25条不同员工向公司内部答疑机器人提出的政策咨询类问题。要求：
1. 全部是单一意图的问题，需要查阅公司政策文档才能回答
2. 覆盖场景：年假查询（跨年使用规则、计算方式）、制度咨询（报销标准、加班政策）、入职办理（入职流程、试用期规定）、权限申请（审批流程）
3. 表达风格多样：正式请求、口语化提问、新员工疑问
4. 部分问题表述含糊，需要推断意图
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",

    # A3: 单意图 - 需查政策（rag_query）- 侧重报销和差旅
    f"""请生成25条不同员工向公司内部答疑机器人提出的报销和差旅相关政策问题。要求：
1. 全部是单一意图的问题，需要查阅政策文档才能回答
2. 覆盖：差旅申请（标准、审批流程、酒店标准）、报销催办（流程、时限）、制度咨询（出差补贴标准）
3. 表达风格多样：详细描述背景的、简短直接的、语气急的
4. 包含具体金额、日期、地点等实体
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",

    # B1: 单意图 - 需人工介入（escalate）
    f"""请生成25条不同员工向公司内部答疑机器人提出的需要人工处理的复杂问题。要求：
1. 全部是单一意图但需要人工介入的问题，例如：投诉、特殊审批、争议处理、异常情况
2. 覆盖场景：考勤争议、报销被拒申诉、薪资疑问、IT故障升级、权限审批特殊情况
3. 表达风格多样：情绪化投诉、正式申诉、紧急求助、详细描述问题
4. 包含具体的人名、时间、部门等细节
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",

    # B2: 单意图 - IT支持和权限
    f"""请生成25条不同员工向公司内部答疑机器人提出的IT支持和权限申请问题。要求：
1. 全部是单一意图问题
2. IT支持：VPN连接、邮箱配置、系统卡顿、账号锁定、内网访问
3. 权限申请：新系统开通、代码仓库权限、管理后台权限、数据查看权限
4. 部分问题表达紧急情绪，部分是日常咨询
5. 包含系统名称（用虚拟名称如"星辰系统"、"云效平台"等阿里系或虚构名称）
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",

    # B3: 单意图 - 入职和考勤
    f"""请生成25条不同员工向公司内部答疑机器人提出的入职办理和考勤请假问题。要求：
1. 全部是单一意图问题
2. 入职办理：入职材料准备、工牌办理、座位分配、入职培训安排、五险一金
3. 考勤请假：请假申请、调休、迟到早退、外勤打卡、加班申请
4. 表达风格多样：新员工的不确定语气、老员工的简短提问
5. 包含具体日期（如4月28日、下周一）、时长等
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",

    # C1: 混合 - 约30%多意图
    f"""请生成25条不同员工向公司内部答疑机器人提出的问题。要求：
1. 混合覆盖所有场景：入职、考勤、差旅、报销、年假、IT、权限、制度
2. 其中约7-8条是多意图问题（一句话包含两个独立请求），其余都是单意图
3. 表达风格多样：正式、口语化、含糊、简短、详细
4. 部分问题包含具体的日期、金额、人名、地点
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",

    # C2: 混合 - 约30%多意图，侧重口语化
    f"""请生成25条不同员工向公司内部答疑机器人提出的问题。要求：
1. 混合覆盖所有场景
2. 其中约7-8条是多意图问题（一句话包含两个独立请求），其余都是单意图
3. 重点生成口语化和不规范的表达：省略主语、语气词、简写
4. 部分问题表达紧急情绪
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",

    # C3: 混合 - 约30%多意图，侧重边界情况
    f"""请生成25条不同员工向公司内部答疑机器人提出的问题。要求：
1. 混合覆盖所有场景，侧重边界情况
2. 其中约7-8条是多意图问题，其余都是单意图
3. 风格：有的非常简短（5-10字），有的很详细（带上下文背景说明）
4. 包含真实感的细节（具体日期如下周三、项目名、同事姓名等）
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",

    # D1: 纯多意图
    f"""请生成25条不同员工向公司内部答疑机器人提出的复合问题。要求：
1. 每条问题都必须包含两个或以上独立请求（多意图）
2. 意图组合多样：差旅+报销、请假+考勤、入职+权限、IT+年假等
3. 表达自然，不要生硬拼凑，要像真实员工一句话说两件事
4. 包含具体实体（日期、金额、地点、人名）
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",

    # D2: 纯多意图 - 侧重不常见组合
    f"""请生成25条不同员工向公司内部答疑机器人提出的复合问题。要求：
1. 每条问题都必须包含两个独立请求（多意图）
2. 侧重不常见组合：IT问题+差旅、权限+报销、制度咨询+入职、年假+IT支持
3. 包含一些特殊表达：反问句、吐槽语气、附带感谢的请求
4. 实体丰富：包含金额（如3500元）、日期（如4月28日）、地点（如杭州办公室）
每条问题单独一行，不要编号，不要其他说明。
{BRAND_CONSTRAINT}""",
]

NUM_ROUNDS = 6

COMPETITOR_BLACKLIST = [
    "微软", "Microsoft", "Google", "谷歌", "AWS", "Amazon", "亚马逊",
    "百度", "腾讯", "华为", "Huawei", "OpenAI", "ChatGPT", "GPT-4", "GPT",
    "Claude", "Meta", "Facebook", "苹果", "Apple", "三星", "Samsung",
    "字节", "ByteDance", "抖音", "飞书", "企业微信", "WeChat",
    "Slack", "Teams", "Zoom", "Notion", "WPS", "金山",
    "小米", "OPPO", "vivo", "京东", "美团", "拼多多",
    "DeepSeek", "Llama", "Gemini", "Copilot", "GitHub",
    "MacBook", "iPhone", "iPad", "iMac", "Windows", "Azure",
    "Outlook", "Excel", "PowerPoint", "Power BI", "Office 365", "Office",
    "Jira", "Confluence", "SAP", "Citrix", "Exchange",
    "Oracle", "Salesforce", "ServiceNow", "Workday",
    "LinkedIn", "Twitter", "Instagram", "TikTok", "Spotify",
    "VSCode", "Visual Studio", "IntelliJ", "PyCharm",
]


def generate_queries(prompt_template):
    response = client.chat.completions.create(
        model=TEACHER_MODEL,
        messages=[{"role": "user", "content": prompt_template}],
        temperature=0.9
    )
    lines = response.choices[0].message.content.strip().split('\n')
    queries = []
    for line in lines:
        q = line.strip()
        q = re.sub(r'^[\d]+[.、)\]]\s*', '', q)
        q = q.strip('"').strip('\u201c').strip('\u201d').strip()
        if len(q) > 5:
            queries.append(q)
    return queries


def label_query(query):
    response = client.chat.completions.create(
        model=TEACHER_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ],
        temperature=0.1
    )
    return response.choices[0].message.content


def validate_label(label_str):
    try:
        if '```' in label_str:
            match = re.search(r'```(?:json)?\s*(.*?)\s*```', label_str, re.DOTALL)
            if match:
                label_str = match.group(1)
        label = json.loads(label_str.strip())
    except json.JSONDecodeError:
        return None
    required = ["intents", "department", "urgency", "entities", "route"]
    if not all(k in label for k in required):
        return None
    if not isinstance(label["intents"], list) or len(label["intents"]) == 0:
        return None
    if not all(i in VALID_INTENTS for i in label["intents"]):
        return None
    if label["department"] not in VALID_DEPARTMENTS:
        return None
    if label["urgency"] not in VALID_URGENCY:
        return None
    if label["route"] not in VALID_ROUTES:
        return None
    if not isinstance(label["entities"], dict):
        return None
    return label


def validate_no_competitor(query, label_dict):
    text = (query + json.dumps(label_dict, ensure_ascii=False)).lower()
    for name in COMPETITOR_BLACKLIST:
        if name.lower() in text:
            return False
    return True


def load_existing():
    """加载已有的增量数据，用于续跑"""
    existing = []
    seen_queries = set()
    if os.path.exists(RAW_FILE):
        with open(RAW_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    sample = json.loads(line)
                    existing.append(sample)
                    seen_queries.add(sample["query"])
                except json.JSONDecodeError:
                    continue
    return existing, seen_queries


_write_lock = threading.Lock()

def append_sample(sample):
    """增量追加一条样本到磁盘（线程安全）"""
    with _write_lock:
        with open(RAW_FILE, 'a', encoding='utf-8') as f:
            f.write(json.dumps(sample, ensure_ascii=False) + '\n')


def finalize(all_samples):
    """去重、拆分、保存最终的 train/test 文件"""
    seen = set()
    unique = []
    for s in all_samples:
        if s["query"] not in seen:
            seen.add(s["query"])
            unique.append(s)
    all_samples = unique
    print(f"去重后: {len(all_samples)} 条")

    random.seed(42)
    random.shuffle(all_samples)

    test_size = min(TEST_SIZE, max(int(len(all_samples) * 0.15), 20))
    train_samples = all_samples[test_size:]
    test_samples = all_samples[:test_size]

    with open(os.path.join(out_dir, "train.jsonl"), "w", encoding="utf-8") as f:
        for s in train_samples:
            record = {
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": s["query"]},
                    {"role": "assistant", "content": json.dumps(s["label"], ensure_ascii=False)}
                ]
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    with open(os.path.join(out_dir, "test.jsonl"), "w", encoding="utf-8") as f:
        for s in test_samples:
            record = {"query": s["query"], "ground_truth": s["label"]}
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"\n训练集: {len(train_samples)} 条 → {out_dir}/train.jsonl")
    print(f"测试集: {len(test_samples)} 条 → {out_dir}/test.jsonl")

    # 统计
    all_intents = {}
    all_routes = {}
    all_depts = {}
    multi_intent = 0
    for s in all_samples:
        for intent in s["label"]["intents"]:
            all_intents[intent] = all_intents.get(intent, 0) + 1
        all_routes[s["label"]["route"]] = all_routes.get(s["label"]["route"], 0) + 1
        all_depts[s["label"]["department"]] = all_depts.get(s["label"]["department"], 0) + 1
        if len(s["label"]["intents"]) > 1:
            multi_intent += 1

    print(f"\n--- 意图分布 ---")
    for k, v in sorted(all_intents.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    print(f"\n--- 路由分布 ---")
    for k, v in sorted(all_routes.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    print(f"\n--- 部门分布 ---")
    for k, v in sorted(all_depts.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    print(f"\n多意图样本: {multi_intent}/{len(all_samples)} ({multi_intent/len(all_samples)*100:.0f}%)")


MAX_WORKERS = 15  # 并行标注线程数


def label_one(query, seen_queries, stats, existing, print_lock):
    """标注单条 query，线程安全。返回 True 表示成功添加。"""
    with print_lock:
        if query in seen_queries:
            stats["dup"] += 1
            return False
        seen_queries.add(query)  # 先占位防重

    try:
        label_str = label_query(query)
        label = validate_label(label_str)
        if label is None:
            with print_lock:
                stats["schema_fail"] += 1
            return False
        if not validate_no_competitor(query, label):
            with print_lock:
                stats["competitor_fail"] += 1
            return False

        sample = {"query": query, "label": label}
        append_sample(sample)
        with print_lock:
            existing.append(sample)
            n = len(existing)
        desc = query[:35] + ("..." if len(query) > 35 else "")
        print(f"  ✓ [{n}] {label['route']:20s} | {desc}", flush=True)
        return True

    except Exception as e:
        print(f"  ✗ {query[:30]}... → {e}", flush=True)
        return False


def main():
    existing, seen_queries = load_existing()
    print(f"已有数据: {len(existing)} 条")

    if len(existing) >= TARGET_TOTAL:
        print(f"已达到目标 {TARGET_TOTAL} 条，直接生成最终文件")
        finalize(existing)
        return

    stats = {"schema_fail": 0, "competitor_fail": 0, "dup": 0, "total_raw": 0}
    print_lock = threading.Lock()
    total_prompts = len(QUERY_PROMPTS) * NUM_ROUNDS
    batch_idx = 0

    for round_num in range(NUM_ROUNDS):
        if len(existing) >= TARGET_TOTAL:
            break

        # Phase 1: 并行生成所有 prompt 的 queries
        print(f"\n{'='*60}")
        print(f"Round {round_num+1}/{NUM_ROUNDS} | 并行生成 {len(QUERY_PROMPTS)} 组查询...")
        all_queries_this_round = []

        with ThreadPoolExecutor(max_workers=min(len(QUERY_PROMPTS), 8)) as pool:
            futures = {pool.submit(generate_queries, p): idx for idx, p in enumerate(QUERY_PROMPTS)}
            for future in as_completed(futures):
                idx = futures[future]
                try:
                    queries = future.result()
                    all_queries_this_round.extend(queries)
                    print(f"  Prompt {idx+1}: {len(queries)} 条", flush=True)
                except Exception as e:
                    print(f"  Prompt {idx+1}: 失败 {e}", flush=True)

        random.shuffle(all_queries_this_round)
        stats["total_raw"] += len(all_queries_this_round)
        needed = TARGET_TOTAL - len(existing)
        print(f"  本轮共 {len(all_queries_this_round)} 条待标注，还需 {needed} 条")

        # Phase 2: 并行标注
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            futures = []
            for q in all_queries_this_round:
                if len(existing) >= TARGET_TOTAL:
                    break
                futures.append(pool.submit(label_one, q, seen_queries, stats, existing, print_lock))

            for future in as_completed(futures):
                future.result()  # propagate exceptions

                if len(existing) >= TARGET_TOTAL:
                    break

        print(f"  Round {round_num+1} 结束 | 已有 {len(existing)} 条")

    print(f"\n{'='*60}")
    print(f"原始查询: {stats['total_raw']}")
    print(f"Schema 过滤: {stats['schema_fail']}")
    print(f"竞品过滤: {stats['competitor_fail']}")
    print(f"重复跳过: {stats['dup']}")
    print(f"有效样本: {len(existing)}")

    finalize(existing)


if __name__ == "__main__":
    main()
