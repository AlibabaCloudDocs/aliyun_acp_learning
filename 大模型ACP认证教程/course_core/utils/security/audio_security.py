# coding=utf-8
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
    # 连接超时时间，单位毫秒（ms）。
    connect_timeout=10000,
    # 读超时时间，单位毫秒（ms）。
    read_timeout=3000,
    region_id='cn-shanghai',
    endpoint='green-cip.cn-shanghai.aliyuncs.com'
)

# 注意：此处实例化的client尽可能重复使用，提升检测性能。避免重复建立连接。
client = Client(config)


def submit_task(audio_url):
    serviceParameters = {
        'url': audio_url,
    }
    voiceModerationRequest = models.VoiceModerationRequest(
        # 检测类型：audio_media_detection表示语音文件检测，live_stream_detection表示语音直播流检测。
        service='audio_media_detection',
        service_parameters=json.dumps(serviceParameters)
    )

    try:
        response = client.voice_moderation(voiceModerationRequest)
        if response.status_code == 200:
            # 调用成功
            result = response.body
            print('audio submit task:{}'.format(result.data))
            # 返回task_id
            return result.data.task_id
        else:
            print('audio submit task fail. status:{} ,result:{}'.format(response.status_code, response))
    except Exception as err:
        print(err)


def get_result(task_id):
    # 提交任务时返回的taskId。
    service_parameters = {
        "taskId": task_id
    }
    voice_moderation_result_request = models.VoiceModerationResultRequest(
        # 检测类型。
        service='audio_media_detection',
        service_parameters=json.dumps(service_parameters)
    )

    try:
        response = client.voice_moderation_result(voice_moderation_result_request)
        if response.status_code == 200:
            # 获取审核结果
            result = response.body
            print('audio detect result:{}'.format(result.data))
        else:
            print('audio detect fail. status:{} ,result:{}'.format(response.status_code, response))
    except Exception as err:
        print(err)


def detect(audio_url):
    task_id = submit_task(audio_url)
    # 等待3秒再查询
    time.sleep(3)
    # 根据任务id查询结果
    result = get_result(task_id)
    # 返回一个通用结构


if __name__ == "__main__":
    # audio_url = ''
    # submit_task(audio_url)
    task_id = 'au_f_vrex9uxM7MXc8flPCiOK5V-1AzKWX'
    get_result(task_id)
