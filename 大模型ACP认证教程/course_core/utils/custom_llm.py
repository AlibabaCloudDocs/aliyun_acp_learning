import requests
import json
from typing import Any, List, Mapping, Optional
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain_core.language_models.llms import BaseLLM
from ragas.llms import LangchainLLMWrapper
import os
import logging
from openai import OpenAI


def get_response(prompt):
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"), # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务的base_url
    )
    completion = client.chat.completions.create(
        model="qwen-plus-latest",
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}],
        )
    return completion.choices[0].message.content

class CustomLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        temperature = 0
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        response = get_response(prompt)
        print(f"prompt is :{prompt}")
        print(f"response is :{response}")
        print("*"*66)
        return get_response(prompt)