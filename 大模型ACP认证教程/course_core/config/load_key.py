import os
import zipfile
import requests
from pathlib import Path
import nltk

def _resolve_nltk_base_dir():
    """
    选定 NLTK 离线资源的根目录，兼容 DSW、Windows 和本地开发环境。
    优先级：环境变量 LLM_LEARN_NLTK_DATA > DSW 的 llm_learn 目录 > 课程根目录 > 用户主目录。
    """
    candidates = []
    # 1. 用户显式指定的目录（可选，例如让多个课程版本共用一份资源）
    env_dir = os.environ.get("LLM_LEARN_NLTK_DATA")
    if env_dir:
        candidates.append(Path(env_dir).expanduser())
    # 2. DSW 环境：安装脚本在 /mnt/workspace 下创建了 llm_learn 虚拟环境，
    #    离线资源按课程约定放在它下面，与课程仓库分离，各课程版本共用
    dsw_llm_learn = Path("/mnt/workspace/llm_learn")
    if dsw_llm_learn.exists():
        candidates.append(dsw_llm_learn / "nltk_data")
    # 3. 非 DSW 环境（Windows、本地开发）：课程根目录，从 load_key.py 向上两级
    candidates.append(Path(__file__).resolve().parents[2] / "nltk_data")
    # 4. 兜底：课程目录只读（权限受限）时，落到 NLTK 官方标准位置
    candidates.append(Path.home() / "nltk_data")

    # 逐个候选试探：mkdir 成功即选定并立即返回，后面的候选不会被创建（短路）。
    # 用 mkdir 本身当可写性探测，而不是 os.access（后者在 Windows 上语义不可靠）；
    # exist_ok=True 保证已存在资源的老学员直接命中，不重复下载。
    for base_dir in candidates:
        try:
            (base_dir / "_static" / "nltk_cache").mkdir(parents=True, exist_ok=True)
            return base_dir
        except OSError:
            continue
    raise OSError(
        "无法创建 NLTK 离线资源目录，请将环境变量 LLM_LEARN_NLTK_DATA 设置为一个可写目录后重试。"
    )

def load_nltk():
    """
    检查并加载 NLTK 离线资源。
    核心逻辑：将资源解压到 LlamaIndex 强制要求的 _static/nltk_cache 子目录下。
    """
    # 1. 基础根目录：按运行环境自动选择（DSW 沿用 llm_learn 约定，见 _resolve_nltk_base_dir）
    base_dir = _resolve_nltk_base_dir()
    
    # 2. 【关键】LlamaIndex 真正搜索的物理深层目录
    # 如果不解压到这里，它就会报 LookupError
    actual_cache_dir = base_dir / "_static" / "nltk_cache"
    
    # 资源配置表
    resources = {
        "tokenizers/punkt": "https://www.modelscope.cn/datasets/haoznic/nltk_data_4_llm_learn/resolve/master/punkt.zip",
        "tokenizers/punkt_tab": "https://www.modelscope.cn/datasets/haoznic/nltk_data_4_llm_learn/resolve/master/punkt_tab.zip",
        "corpora/stopwords": "https://www.modelscope.cn/datasets/haoznic/nltk_data_4_llm_learn/resolve/master/stopwords.zip"
    }

    # 3. 设置环境变量，对齐搜索路径
    # 告诉 LlamaIndex：直接使用最深层 NLTK 缓存目录
    os.environ["LLAMA_INDEX_CACHE_DIR"] = str(actual_cache_dir.resolve())
    # 告诉 NLTK 库：直接去最深层目录找
    os.environ["NLTK_DATA"] = str(actual_cache_dir.resolve())
    
    if str(actual_cache_dir.resolve()) not in nltk.data.path:
        nltk.data.path.insert(0, str(actual_cache_dir.resolve()))

    # 4. 循环检查并按需下载
    actual_cache_dir.mkdir(parents=True, exist_ok=True)
    any_downloaded = False
    any_failed = False
    
    for sub_path, url in resources.items():
        # 物理检查点，例如：.../nltk_data/_static/nltk_cache/tokenizers/punkt
        check_point = actual_cache_dir / sub_path
        
        if check_point.exists():
            continue
        
        any_downloaded = True
        zip_name = Path(url).name
        print(f"📦 正在初始化离线资源: {zip_name}...")
        
        try:
            # 建立父目录 (例如 tokenizers/ 或 corpora/)
            parent_dir = check_point.parent
            parent_dir.mkdir(parents=True, exist_ok=True)
            
            # 下载 ZIP
            zip_file_path = parent_dir / zip_name
            response = requests.get(url, timeout=60, stream=True)
            response.raise_for_status()
            
            with open(zip_file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024*1024):
                    f.write(chunk)
            
            # 解压到当前父目录
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(parent_dir)
            
            zip_file_path.unlink()
            print(f"✅ {zip_name} 处理成功")
            
        except Exception as e:
            any_failed = True
            print(f"❌ {zip_name} 初始化失败: {e}")

    if any_failed:
        print(f"⚠️ 有离线资源初始化失败，请检查网络后重新运行本单元格。资源目录：{actual_cache_dir}")
    elif not any_downloaded:
        print(f"💡 环境检查：离线资源已在 {actual_cache_dir} 就绪。")
    else:
        print(f"✅ 资源已成功解压至对齐目录。")


def load_key():
    import os
    import getpass
    import json
    import dashscope
    file_name = '../Key.json'
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            Key = json.load(file)
        if "DASHSCOPE_API_KEY" in Key:
            os.environ['DASHSCOPE_API_KEY'] = Key["DASHSCOPE_API_KEY"].strip()
    else:
        DASHSCOPE_API_KEY = getpass.getpass("未找到存放Key的文件，请输入你的api_key:").strip()
        Key = {
            "DASHSCOPE_API_KEY": DASHSCOPE_API_KEY
        }
        # 指定文件名
        file_name = '../Key.json'
        with open(file_name, 'w') as json_file:
            json.dump(Key, json_file, indent=4)
        os.environ['DASHSCOPE_API_KEY'] = Key["DASHSCOPE_API_KEY"]
    dashscope.api_key = os.environ["DASHSCOPE_API_KEY"]
    
    # load_nltk()
    
if __name__ == '__main__':
    load_key()
    import os
    print(os.environ['DASHSCOPE_API_KEY'])
