# coding=utf-8

from alibabacloud_green20220302.client import Client
from alibabacloud_green20220302 import models
from alibabacloud_tea_openapi.models import Config
from alibabacloud_tea_util import models as util_models
import json
import os
import uuid


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
    # 设置http代理。
    # http_proxy='http://10.10.xx.xx:xxxx',
    # 设置https代理。
    # https_proxy='https://10.10.xx.xx:xxxx',
    # 接入区域和地址请根据实际情况修改。
    endpoint='green-cip.cn-beijing.aliyuncs.com'
)
client = Client(config)


def detect(image_url):

    # 创建RuntimeObject实例并设置运行参数。
    runtime = util_models.RuntimeOptions()

    # 检测参数构造。
    service_parameters = {
        # 公网可访问的图片url
        'imageUrl': image_url,
        # 数据唯一标识
        'dataId': str(uuid.uuid1())
    }

    image_moderation_request = models.ImageModerationRequest(
        # 图片检测service
      	# 支持service请参考：https://help.aliyun.com/document_detail/467826.html?0#p-23b-o19-gff
        service='baselineCheck_pro',
        service_parameters=json.dumps(service_parameters)
    )

    try:
        response = client.image_moderation_with_options(image_moderation_request, runtime)
        if response.status_code == 200:
            result = response.body
            # print('response success. result:{}'.format(result))
            if result.code == 200:
                result_data = result.data
                print('image detect result: {}'.format(result_data))
                return result_data
        else:
            print('image detect fail. status:{} ,result:{}'.format(response.status_code, response))
        return
    except Exception as err:
        print(err)


if __name__ == '__main__':
    image_url = "https://img.alicdn.com/imgextra/i2/O1CN01M5Cie31udzY84ppIw_!!6000000006061-2-tps-300-158.png"
    detect(image_url)