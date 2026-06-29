import pandas as pd
import ast
import os


"""
知识库文本过滤思路：
- 按公司职位来实现知识库文本的访问权限控制
- 一个知识库文本可能与N个职位有关联

使用csv文件模拟数据库存储
- kb_topK.csv: 知识库检索的topK文本
- kb_position_ref.csv:知识库文本和职位的关联信息
- user.csv: 用户信息和所属的公司职位
- position.csv: 职位信息
"""

# 获取当前脚本的绝对路径
base_path = os.path.dirname(os.path.abspath(__file__))

# 构建CSV文件的绝对路径
kb_topK_path = os.path.join(base_path, 'db', 'kb_topK.csv')
user_path = os.path.join(base_path, 'db', 'user.csv')
kb_position_ref_path = os.path.join(base_path, 'db', 'kb_position_ref.csv')
position_path = os.path.join(base_path, 'db', 'position.csv')


# 读取 CSV 文件
kb_topK_table = pd.read_csv(kb_topK_path)
user_table = pd.read_csv(user_path)
kb_position_ref_table = pd.read_csv(kb_position_ref_path)
position_table = pd.read_csv(position_path)


def get_filter_contents(user_id):
    # 查询用户职位（权限）
    user_position_id = user_table[user_table['user_id'] == user_id]['position_id'].values[0]
    position_name = position_table.loc[position_table['id'] == 1, 'position_name'].values[0]
    print("当前用户的职位: {}\n".format(position_name))

    # 查询topK文本对应的职位（权限）
    topK_position_table = pd.merge(kb_topK_table, kb_position_ref_table, on='kb_id')
    # 打印召回的文本
    print("==========召回文本==========")
    for content in topK_position_table["content"].tolist():
        print(content)
    print("==========召回文本==========\n")

    # 遍历合并后的表并找到匹配的职位
    matching_kb_ids = []

    for index, row in topK_position_table.iterrows():
        # 将字符串转换为列表
        position_ids = ast.literal_eval(row['position_ids'])
        if user_position_id in position_ids:
            matching_kb_ids.append(row['kb_id'])

    # 根据 kb_id 过滤出相应的行
    filtered_data = kb_topK_table[kb_topK_table['kb_id'].isin(matching_kb_ids)]
    # 获取 content 列并转换为列表
    content_list = filtered_data['content'].tolist()
    print("用户拥有权限的召回文本:", content_list)


if __name__ == "__main__":
    user_id = 201
    get_filter_contents(user_id)
