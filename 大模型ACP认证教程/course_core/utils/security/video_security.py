#encoding:utf-8
# python version >= 3.6
import time

from alibabacloud_green20220302.client import Client
from alibabacloud_green20220302 import models
from alibabacloud_tea_openapi.models import Config
import json
import os

access_key_id = os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID']
access_key_secret = os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']


config = Config(
            # 阿里云账号AccessKey拥有所有API的访问权限，建议您使用RAM用户进行API访问或日常运维。
            # 强烈建议不要把AccessKey ID和AccessKey Secret保存到工程代码里，否则可能导致AccessKey泄露，威胁您账号下所有资源的安全。
            # 常见获取环境变量方式：
            # 获取RAM用户AccessKey ID：os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID']
            # 获取RAM用户AccessKey Secret：os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            # 连接时超时时间，单位毫秒（ms）。
            connect_timeout=3000,
            # 读取时超时时间，单位毫秒（ms）。
            read_timeout=6000,
            # 接入区域和地址请根据实际情况修改。
            region_id='cn-shanghai',
            endpoint='green-cip.cn-shanghai.aliyuncs.com'
)

client = Client(config)


def submit_task(video_url):

    service_parameters = {
        'url': video_url
    }
    video_moderation_request = models.VideoModerationRequest(
        # 检测类型：videoDetection
        service='videoDetection',
        service_parameters=json.dumps(service_parameters)
    )

    try:
        response = client.video_moderation(video_moderation_request)
        if response.status_code == 200:
            result = response.body
            print('video submit task:{}'.format(result.data))
            return result.data.task_id
        else:
            print('video submit task fail. status:{} ,result:{}'.format(response.status_code, response))
    except Exception as err:
        print(err)


def get_result(task_id):
    # 提交任务时返回的taskId。
    service_parameters = {
        "taskId": task_id
    }
    video_moderation_result_request = models.VideoModerationResultRequest(
        # 检测类型：videoDetection
        service='videoDetection',
        service_parameters=json.dumps(service_parameters)
    )

    try:
        response = client.video_moderation_result(video_moderation_result_request)
        if response.status_code == 200:
            result = response.body
            print('video detect result:{}'.format(result))
        else:
            print('video detect fail. status:{} ,result:{}'.format(response.status_code, response))
    except Exception as err:
        print(err)


def detect(video_url):
    task_id = submit_task(video_url)
    time.sleep(3)
    get_result(task_id)


if __name__ == "__main__":
    video_url = ''
    # task_id = submit_task(video_url)
    task_id = 'vi_f_YLZysINUYOMP5fIHhRCIrL-1AzLt6'
    get_result(task_id)
