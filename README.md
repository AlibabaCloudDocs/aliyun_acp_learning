[English](./README-en.md) | 简体中文

# 阿里云大模型ACP教程

<img src="https://gw.alicdn.com/imgextra/i1/O1CN01xol8Y21oUw1VeGgbZ_!!6000000005229-0-tps-1096-569.jpg" alt="main" width="800px">

## 🎈 欢迎新同学

欢迎来到阿里云大模型ACP高级工程师认证课程，这是阿里云大模型认证的进阶篇。在开始课程之前，先来了解阿里云大模型认证的体系架构，方便你选择适合自己定位的课程。
阿里云大模型认证体系架构：

<img src="https://gw.alicdn.com/imgextra/i1/O1CN01MC00f61wMhpgctA1q_!!6000000006294-0-tps-1445-478.jpg" alt="我的notebook" width="800px">

> 如果你尚不具备编程基础，或者想从零开始了解大模型，请跳转:point_right:[阿里云大模型ACA工程师认证课程](https://edu.aliyun.com/course/3126500)

## [最近更新](./release_notes.md)
- [2026.04.30] V2.4.2 微调改为蒸馏
- [2026.04.10] V2.4.0 Qwen Code 实践课程
- [2026.03.27] V2.3.0 新增 Agent Skills 章节
- [2025.11.14] V2.2.0 重构 Agent 章节
- [2025.07.28] V2.1.0 引入 Meta Prompting
- [2025.07.24] V2.0.9 引入上下文工程框架
- [2025.06.27] V2.0.8 更新大模型应用安全合规内容
- [2025.06.13] V2.0.7 更新2.4节RAG自动化评测内容
- 详情请见[Release Notes](./release_notes.md)
  
## 🪶  课程定位

了解课程定位会帮助你更好地规划学习路径，确保课程内容与个人目标相匹配，从而提升学习效率和成果。通过学习阿里云大模型高级工程师ACP认证课程，你将
- 掌握以下知识与技能：
    - 大模型提示词技巧
    - 检索增强和微调的原理和流程
    - LangChain、Llama-Index等大模型开发组件的使用方法
    - 工程化评测的概念与方法
    - 大模型的规范和安全性
- 有能力完成以下任务：
    - 使用阿里云百炼平台构建大模型应用(开发、测评、部署、发布)
    - 使用提示词策略、检索增强、微调技术优化大模型回答质量
    - 使用Multi-Agent进行文本、图像、视频等多模态内容生产
    - 能够针对复杂业务场景设计并实施大模型驱动的解决方案
- 胜任以下岗位：
    - 大模型解决方案高级工程师
    - 大模型应用开发高级工程师


## 📙 课程列表

本课程面向具备编程基础的生成式人工智能技术爱好者和应用开发者，不仅传授理论知识，更聚焦于实战落地。我们将围绕一个完整项目——**新人答疑机器人**，系统化拆解从业务需求分析、场景适配、模型选型、Prompt 工程、应用开发到最终部署运维的全链路闭环。旨在培养学员针对复杂业务场景，独立设计并实施大模型驱动解决方案的能力，让你真正掌握从“想法”到“落地”完整路径。

<table>
<thead>
 <tr>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">章节</td>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">课时</td>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">标题</td>
 </tr>
 </thead>
 <tbody>
  <tr>
    <td rowspan="1" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">C1 课程准备</td>
    <td style="padding:10px; border: 1px solid #ddd;">1.1</td>
    <td style="padding:10px; border: 1px solid #ddd;">配置 AI 开发环境</td>
  </tr>
  <tr>
    <td rowspan="6" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">C2 构造问答系统</td>
    <td style="padding:10px; border: 1px solid #ddd;">2.0</td>
    <td style="padding:10px; border: 1px solid #ddd;">项目背景</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.1</td>
    <td style="padding:10px; border: 1px solid #ddd;">用大模型构建新人答疑机器人</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.2</td>
    <td style="padding:10px; border: 1px solid #ddd;">扩展答疑机器人的知识范围</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.3</td>
    <td style="padding:10px; border: 1px solid #ddd;">优化提示词改善回答质量</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.4</td>
    <td style="padding:10px; border: 1px solid #ddd;">自动化评测答疑机器人的表现</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.5</td>
    <td style="padding:10px; border: 1px solid #ddd;">优化 RAG 应用提升问答准确度</td>
  </tr>
  <tr>
    <td rowspan="8" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">C3 构建 Agent 系统</td>
    <td style="padding:10px; border: 1px solid #ddd;">3.0</td>
    <td style="padding:10px; border: 1px solid #ddd;">从回答问题到解决问题</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.1</td>
    <td style="padding:10px; border: 1px solid #ddd;">Agent 基础与工具调用</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.2</td>
    <td style="padding:10px; border: 1px solid #ddd;">让 Agent 学会规划与执行</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.3</td>
    <td style="padding:10px; border: 1px solid #ddd;">用多 Agent 实现团队协作</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.4</td>
    <td style="padding:10px; border: 1px solid #ddd;">用 Memory 让 Agent 积累经验</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.5</td>
    <td style="padding:10px; border: 1px solid #ddd;">用 Skill 将能力固化为可复用流程</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.6</td>
    <td style="padding:10px; border: 1px solid #ddd;">用评测驱动 Agent 开发</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.7</td>
    <td style="padding:10px; border: 1px solid #ddd;">Qwen Code 实践</td>
  </tr>
  <tr>
    <td rowspan="5" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">C4 交付上线</td>
    <td style="padding:10px; border: 1px solid #ddd;">4.0</td>
    <td style="padding:10px; border: 1px solid #ddd;">走向生产环境</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">4.1</td>
    <td style="padding:10px; border: 1px solid #ddd;">用蒸馏让小模型掌握专业能力</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">4.2</td>
    <td style="padding:10px; border: 1px solid #ddd;">部署模型</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">4.3</td>
    <td style="padding:10px; border: 1px solid #ddd;">大模型应用生产实践</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">4.4</td>
    <td style="padding:10px; border: 1px solid #ddd;">大模型应用安全合规</td>
  </tr>
  <tr>
    <td rowspan="2" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">C5 总结与展望</td>
    <td style="padding:10px; border: 1px solid #ddd;">5.1</td>
    <td style="padding:10px; border: 1px solid #ddd;">培养品味用 AI 为业务提效</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">5.2</td>
    <td style="padding:10px; border: 1px solid #ddd;">总结与展望</td>
  </tr>
  </tbody>
</table>



## 💯 考试大纲 (即将更新)

带着目的学习可以提升学习效率。在开始课程之前，请了解大模型ACP认证的考试大纲，将更有利于你的课程学习。
### 🌟 考试知识点分布


<table>
<thead>
 <tr>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">考核知识点</td>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">试题比例</td>
 </tr>
 </thead>
 <tbody>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型应用开发</td>
    <td style="padding:10px; border: 1px solid #ddd;">17%</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型提示词工程</td>
    <td style="padding:10px; border: 1px solid #ddd;">15%</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型检索增强</td>
    <td style="padding:10px; border: 1px solid #ddd;">20%</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型微调</td>
    <td style="padding:10px; border: 1px solid #ddd;">16%</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">多Agent及多模态应用</td>
    <td style="padding:10px; border: 1px solid #ddd;">16%</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">生产环境应用实践</td>
    <td style="padding:10px; border: 1px solid #ddd;">16%</td>
  </tr>

  </tbody>
</table>

### 🌟 考试大纲
<table>
<thead>
 <tr>
    <td width="140px" style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">主要章节</td>
    <td width="300px" style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">主要内容</td>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">考察知识点</td>
 </tr>
 </thead>
 <tbody>
  <tr>
    <td rowspan="1" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">大模型应用开发</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 通过OpenAI API调用大模型 <br>• 了解大模型的工作原理</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 基本API参数如model、temperature、top_p等等 <br>• 批量生成与流式生成 <br>• 理解消息与对话历史</td>
  </tr>
  <tr>
    <td rowspan="2" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">大模型提示词工程</td>
    <td style="padding:10px; border: 1px solid #ddd;">构建有效的提示词</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 提示词框架如提示词要素、提示词分隔符、提示词模板 <br>• 理解系统角色提示词的作用</td>
  </tr>
    <tr>
    <td style="padding:10px; border: 1px solid #ddd;">利用大模型处理各类任务</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 理解大模型的适用场景<br>• 利用大模型开发应用（如批量对员工咨询做意图分类、用大模型做文档审阅、实现针对问题的自动文档修订）</td>
  </tr>
   <tr>
    <td rowspan="3" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">大模型检索增强</td>
    <td style="padding:10px; border: 1px solid #ddd;">通过LlamaIndex构建RAG应用的基本使用方法</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 理解RAG的核心要素，如文件解析、文本切片、段落召回、段落重排序。<br>• 理解对RAG做召回优化如句子窗口检索、自动合并检索等等。</td>
  </tr>
<tr>
    <td style="padding:10px; border: 1px solid #ddd;">持续优化检索增强能力</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 理解更贴近实战的RAG优化方法如优化文本解析、标题改写优化、表格内容增强、文本分割方法对比等等</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">对检索增强的能力做自动化评测</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 了解RAGAS指标体系<br>• 懂得RAG系统的评测方法。</td>
  </tr>
  <tr>
    <td rowspan="2" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">大模型的微调</td>
    <td style="padding:10px; border: 1px solid #ddd;">微调的概念与要求</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 微调的作用、前提、基本步骤、常用算法</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">微调的实验与评测</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 微调数据集构建、微调参数介绍、微调模型评测</td>
  </tr>
  <tr>
    <td rowspan="2" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">智能体与应用</td>
    <td style="padding:10px; border: 1px solid #ddd;">基于百炼API构建智能体</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 理解智能体运行机制<br>• 构造复杂工作流和多智能体应用</td>
    </tr>
    <tr>
    <td style="padding:10px; border: 1px solid #ddd;">构建更复杂的AI应用</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 动手实践阿里发布的AI技术解决方案系列，体验多模态交互技术。<br>• 了解AI在医疗、教育、娱乐等行业的实际应用。
    </td>
  </tr>
  <tr>
    <td rowspan="2" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">生产环境应用实践</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 在云上部署微调模型的基本方案<br>• 在云服务如（ECS、FC、PAI）中部署模型<br>• 在百炼上部署模型</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 掌握如何使用vLLM进行大模型的部署操作<br>• 了解如何利用云服务如函数计算（FC）实现AI助手的快速发布</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型应用发布至生产环境的关键要素</td>
    <td style="padding:10px; border: 1px solid #ddd;">• 了解如何平衡大模型应用的性能和运行成本<br>• 了解如何提升大模型应用的稳定性<br>• 了解如何保障大模型应用安全合规</td>
  </tr>
  </tbody>
</table>

本考纲旨在为考生提供考试内容的普遍方向，考试范围不仅限于文中提及的部分，可能还包括其他相关未列明的内容。

## 🛠️ 教程及代码

本教程假设你已经初步了解并使用过 python、git，因此不会涉及如何安装 python、pip、git 等基础工具。你可以通过脚本“自动安装”或者“手动下载代码”在你的系统上安装课程文件。

### 1.自动安装
如果你对Linux环境熟悉，你可以体验使用脚本自动完成课程文件下载和依赖项安装。

在 DSW 的 Linux 环境，或启动 MAC 的命令行界面，点击下载[aliyun_llm_acp_install脚本](https://developer-labfileapp.oss-cn-hangzhou.aliyuncs.com/ACP/aliyun_llm_acp_install.sh)，或者输入如下命令，即可完成项目安装。

```bash
wget https://developer-labfileapp.oss-cn-hangzhou.aliyuncs.com/ACP/aliyun_llm_acp_install.sh
/bin/bash aliyun_llm_acp_install.sh
```
详情可参考[《1_0_计算环境准备》](./大模型ACP认证教程/p1_课程准备/1_0_计算环境准备.ipynb)

顺利执行上述命令后，你可以使用你的百炼API-KEY，开始你的学习。

### 2.手动下载代码

本教程github地址如下：
```
git clone https://github.com/AlibabaCloudDocs/aliyun_acp_learning.git
cd aliyun_acp_learning
pip install -r requirements.txt
```

如果遇到网络问题，GitHub无法使用，可以选择从atomgit来获取代码库

#
```
git clone https://atomgit.com/alibabaclouddocs/aliyun_acp_learning.git
cd aliyun_acp_learning
pip install -r requirements.txt
```



## 📌 问题反馈

如果你在学习过程中遇到任何问题，欢迎你[通过问卷提交评价和反馈学习体验](https://survey.aliyun.com/apps/zhiliao/Mo5O9vuie)。
你的批评和鼓励都是我们前进的动力！

