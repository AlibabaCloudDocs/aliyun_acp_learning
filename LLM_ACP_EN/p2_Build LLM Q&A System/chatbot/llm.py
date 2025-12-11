import os
from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"), # How to obtain the API Key: https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url=os.getenv("DASHSCOPE_API_BASE")
)

def invoke(user_message, model_name="qwen-plus"):
    completion = client.chat.completions.create(
        model=model_name, # Model list: https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[{"role": "user", "content": user_message}]
    )
    # In production environments, it is recommended to handle invocation exceptions
    return completion.choices[0].message.content

def invoke_with_stream_log(user_message, model_name="qwen-plus"):
    completion = client.chat.completions.create(
        model=model_name, # Model list: https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[{"role": "user", "content": user_message}],
        stream=True
    )
    result = ""
    for response in completion:
        result += response.choices[0].delta.content
        print(response.choices[0].delta.content, end="")
    # In production environments, it is recommended to handle invocation exceptions
    return result