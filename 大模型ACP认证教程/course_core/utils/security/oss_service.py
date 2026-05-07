# coding=utf-8
# python version >= 3.6
import uuid
import oss2
import time


# 服务是否部署在vpc上
is_vpc = False
# 文件上传token endpoint->token
token_dict = dict()
# 上传文件客户端
bucket = None
# 接入区域和地址请根据实际情况修改。
# end_point = 'green-cip.cn-beijing.aliyuncs.com'


# 创建文件上传客户端
def create_oss_bucket(is_vpc, upload_token):
    global token_dict
    global bucket
    auth = oss2.StsAuth(upload_token.access_key_id, upload_token.access_key_secret, upload_token.security_token)

    if (is_vpc):
        end_point = upload_token.oss_internal_end_point
    else:
        end_point = upload_token.oss_internet_end_point
    # 注意：此处实例化的bucket请尽可能重复使用，避免重复建立连接，提升检测性能。
    bucket = oss2.Bucket(auth, end_point, upload_token.bucket_name)


# 上传文件
def upload_file(file_name, upload_token):
    create_oss_bucket(is_vpc, upload_token)
    object_name = upload_token.file_name_prefix + str(uuid.uuid1()) + '.' + file_name.split('.')[-1]
    bucket.put_object_from_file(object_name, file_name)
    return object_name


# 获取文件上传的token
def get_token(client, endpoint):
    upload_token = token_dict.setdefault(endpoint, None)
    if (upload_token == None) or int(upload_token.expiration) <= int(time.time()):
        response = client.describe_upload_token()
        upload_token = response.body.data
        token_dict[endpoint] = upload_token
    return upload_token

def get_region_id_from_endpoint(endpoint):
    # 去除endpoint中的协议部分（如果存在），并统一处理为公网形式的endpoint以便提取region
    endpoint = endpoint.split('//')[-1]  # 移除可能的协议前缀
    if endpoint.endswith('aliyuncs.com'):  # 公网Endpoint格式处理
        region_id = endpoint.split('.')[0].split('-')[-1]
    elif endpoint.endswith('internal.aliyuncs.com'):  # VPC内网Endpoint格式处理
        region_id = endpoint.split('.')[0].split('-')[-2]
    else:
        raise ValueError("Unsupported endpoint format.")
    return region_id


if __name__ == "__main__":
    end_point = 'green-cip.cn-beijing.aliyuncs.com'
    # 在您的函数中调用此函数来获取RegionId
    oss_region_id = get_region_id_from_endpoint(end_point)
    print(f"The OSS RegionId is: {oss_region_id}")

