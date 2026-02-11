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

if __name__ == '__main__':
    load_key()
    import os
    print(os.environ['DASHSCOPE_API_KEY'])
