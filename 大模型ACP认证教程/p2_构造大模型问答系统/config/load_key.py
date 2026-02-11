import os
import zipfile
from pathlib import Path
import nltk

def load_nltk():
    # 1. 基础路径配置
    # 我们按照你的要求，把数据放在 /mnt/workspace/llm_learn/nltk_data
    nltk_data_dir = Path("/mnt/workspace/llm_learn/nltk_data")
    
    # LlamaIndex 内部会自动找基础目录下的 _static/nltk_cache
    actual_data_path = nltk_data_dir / "_static" / "nltk_cache"
    
    current_dir = Path(__file__).parent.resolve()
    zip_dir = current_dir.parent / "resources" / "nltk_data_zips"

    # 2. 设置环境变量 (核心：对齐 LlamaIndex 的路径逻辑)
    os.environ["LLAMA_INDEX_CACHE_DIR"] = str(nltk_data_dir.resolve())
    os.environ["NLTK_DATA"] = str(nltk_data_dir.resolve())
    os.environ["LLAMA_INDEX_DISABLE_NLTK"] = "1"

    # 3. 资源清单：新增了 punkt_tab
    packages = {
        "tokenizers/punkt": zip_dir / "punkt.zip",
        "tokenizers/punkt_tab": zip_dir / "punkt_tab.zip",
        "corpora/stopwords": zip_dir / "stopwords.zip"
    }

    if not actual_data_path.exists():
        actual_data_path.mkdir(parents=True, exist_ok=True)

    for sub_path, zip_path in packages.items():
        # 目标物理位置
        final_dest = actual_data_path / sub_path
        
        if not final_dest.exists():
            if not zip_path.exists():
                # 如果学员没下载 punkt_tab，这里会报错提醒
                raise FileNotFoundError(f"❌ 缺失离线资源包: {zip_path.name}，请从 resources 下载。")
            
            print(f"📦 正在初始化离线资源: {zip_path.name}...")
            extract_to = final_dest.parent
            extract_to.mkdir(parents=True, exist_ok=True)
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)

    # 4. 注入搜索路径
    if str(actual_data_path) not in nltk.data.path:
        nltk.data.path.insert(0, str(actual_data_path.resolve()))

    print("✅ 离线 NLTK 资源（含 punkt_tab）加载成功。")
    


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
    
    load_nltk()

if __name__ == '__main__':
    load_key()
    import os
    print(os.environ['DASHSCOPE_API_KEY'])
