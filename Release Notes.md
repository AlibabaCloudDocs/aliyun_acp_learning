# Release Notes

## v1.2.5 完善模型部署资源的选型指引
> 变更时间：2025.04.02

我们注意到，原章节中对于阿里云百炼、函数计算、PAI-EAS、ACS/ACK 以及 ECS 上部署大规模模型的差异描述不够清晰。为此，我们对相关内容进行了改进，旨在帮助学员能够根据实际情况选择更适合的方式进行部署。

<hr style="border: 2px solid black;">

## v1.2.4 增加 Reasoning Model 的使用技巧
> 变更时间：2025.03.25

为了帮助学员更有效地使用推理模型（如Deepseek-R1、通义千问-QwQ）来提升答疑机器人的回答质量，我们增加了关于如何撰写高质量提示词的指导。核心在于清晰地表达核心需求，并提供详尽且有用的背景信息。此外，我们还介绍了在复杂任务场景下，如何结合推理模型与通用模型各自的优势更好更快地完成任务。

**优化/新增内容示例**

<img src="https://img.alicdn.com/imgextra/i4/O1CN01jxCo8u1SPyErZB7aJ_!!6000000002240-2-tps-754-220.png" width="343">
<img src="https://img.alicdn.com/imgextra/i2/O1CN01mABRa6215pN6wom02_!!6000000006934-2-tps-1752-328.png" width="532">

推理模型与通用模型分工协作完成复杂任务：

<img src="https://img.alicdn.com/imgextra/i4/O1CN01uZWa8k243UBb3FDqO_!!6000000007335-0-tps-3604-1478.jpg" width="700">

<hr style="border: 2px solid black;">

## v1.2.3 优化实践环境的安装方法
> 变更时间：2025.03.20

考虑到“环境准备”是实践的前提，环境安装难度降低和适用范围提升可以帮助学员更好地完成后续操作。为此，本次更新在手动安装基础上增加了自动安装环境的方法，同时不再限定单一镜像，并结合python虚拟环境（venv）提升环境安装的适配性。

**优化/新增内容示例**

1. 新增自动安装脚本，可一键安装所需环境：

<img src="https://img.alicdn.com/imgextra/i4/O1CN01ZIhiOx1RmaB4K754D_!!6000000002154-2-tps-1616-1074.png" width="600">

2. 旧版扩展阅读中有conda虚拟环境配置说明，但缺少安装说明，且安装不稳定。新版通过 Python自带的venv进行虚拟环境管理，避免安装，直接配置管理：

| 旧版 | 新版 |
| --- | --- |
| <img src="https://img.alicdn.com/imgextra/i4/O1CN01hK7eo31wYcBeR5LcM_!!6000000006320-2-tps-1590-1396.png" width="500">| <img src="https://img.alicdn.com/imgextra/i3/O1CN0111ctm61ibuPoplCGl_!!6000000004432-2-tps-1438-930.png" width="500"> |

3. 新版取消了单一镜像的限定，并补充镜像选择指引：

| 旧版 | 新版 |
| --- | --- |
| <img src="https://img.alicdn.com/imgextra/i2/O1CN01iqOj6t1uTutQAYDBZ_!!6000000006039-2-tps-1642-414.png" width="500">| <img src="https://img.alicdn.com/imgextra/i2/O1CN012QM0tm1kF7wh5hHqX_!!6000000004653-2-tps-1624-1130.png" width="500"> |

<hr style="border: 2px solid black;">

## V2.0 试题题库更新
> 变更时间：2025.03.12

我们注意到目前的考试过于偏向于概念考察，且第二章重构涉及较多内容变更，为此我们重构了整体题库，优化了知识点考核比例，重点增加场景应用类试题，考察学员在实际场景中的应用能力。

| V1.0考核知识点占比： |  | I | V2.0考核知识点占比： |  |
| --- | --- | --- | --- | --- |
| 考核知识点 | 试题比例 | I | 考核知识点 | 试题比例 |
| 大模型应用开发 | 16% | I | 大模型应用开发 | 17% |
| 大模型提示词工程 | 24% | I | 大模型提示词工程 | 14% |
| 大模型检索增强 | 24% | I | 大模型检索增强 | 19% |
| 大模型微调 | 16% | I | 大模型微调 | 17% |
| 大模型伦理与安全 | 8% | I | 多Agent及多模态应用 | 16% |
| AI 辅助多模态内容生产 | 12% | I | 生产环境应用实践 | 17% |

试题优化示例

<table style="width:800px">
  <tr>
    <th>在评测微调模型性能时，以下哪些是常用的评测指标？</th>
    <th>在进行微调模型性能评测时，选择合适的评测指标是至关重要的。假设某位 AI 工程师正在对一个大语言模型进行微调，以用于情感分析任务。他希望确保模型能够准确地对用户评论进行分类，从而提升在线商店的用户体验。在这个过程中，需要重点关注以下哪些常用的评测方法？</th>
  </tr>
  <tr>
    <td>A、召回率</td>
    <td>A、测算情感分析的召回率（Recall）</td>
  </tr>
  <tr>
    <td>B、精确率</td>
    <td>B、分析情感分析的准确率（Accuracy）</td>
  </tr>
    <tr>
    <td>C、F1分数</td>
    <td>C、在对比多个微调版本时，采取人工打标进行评测</td>
  </tr>
    <tr>
    <td>D、训练时间</td>
    <td>D、评估微调的训练时间（Training Time）</td>
  </tr>
    <tr>
    <td>E、生成速度</td>
    <td>E、微调时采用的学习率（Learning Rate）</td>
  </tr>
    <tr>
    <td>F、batch size</td>
    <td>F、微调时使用的批大小（Batch Size）</td>
  </tr>
    <tr>
    <td>正确答案：ABC <br> <mark>问题：题干设计过于简单，无背景描述，无场景限定；选项限定不足，在不同场景中可能有不同释义。</mark></td>
    <td>正确答案：ABC</td>
  </tr>
</table>

<hr style="border: 2px solid black;">

## v1.2.2 重构第三章课程内容
> 变更时间：2025.03.12

鉴于原第三章的内容已显得有些过时，我们对这部分内容进行了重新设计。本次更新旨在帮助学员巩固所学知识，深入理解当前大模型技术的应用场景及发展趋势，激发对人工智能领域持续探索的兴趣。

**新增内容示例**

<img src="https://img.alicdn.com/imgextra/i1/O1CN01OnJTwn1pXyJyxrHpr_!!6000000005371-2-tps-774-708.png" width="400">

<hr style="border: 2px solid black;">

## v1.2.1 新增章节：“2.9 大模型应用生产实践” 
> 变更时间：2025.03.10

本次更新引入了全新的章节内容，旨在帮助学员理解将大模型应用发布至生产环境的关键要素，以及如何将大模型高效、低成本地部署到实际业务场景中，并为如何搭建稳定、安全的系统架构提供指导。

**新增内容示例**

<img src="https://img.alicdn.com/imgextra/i2/O1CN013ZcUh528i1iKaH1xA_!!6000000007965-2-tps-604-702.png" width="301">
<img src="https://img.alicdn.com/imgextra/i4/O1CN01L08Hko1kRx2H9qOYc_!!6000000004681-2-tps-614-740.png" width="290">

> 注：原“2.7 大模型RAG内容安全合规检查”节内容合并至本节中。

<hr style="border: 2px solid black;">

## v1.2.0 重构章节：“2.8 通过微调提升模型的准确度与效率”
> 变更时间：2025.03.05

由于微调环节相对复杂，需要理解相对较多的基础概念，本次重构将补充关键知识点，并重新梳理微调实践，帮助学员深入理解什么是微调并积累更多实操经验。

**优化/新增内容示例**

1. 微调任务优化，从较抽象的NL2SQL任务调整为简单数学任务：

| 旧版 | 新版 |
| --- | --- |
| <img src="https://img.alicdn.com/imgextra/i4/O1CN01e3pWtX1yQUOO4p777_!!6000000006573-2-tps-1336-660.png" width="500">| <img src="https://img.alicdn.com/imgextra/i3/O1CN01ase9XQ1brko4miS59_!!6000000003519-2-tps-1332-498.png" width="500"> |

2. 知识扩充，兼顾探究微调基本原理和不同任务上的微调方法：

<img src="https://img.alicdn.com/imgextra/i3/O1CN01XvO8za1J1qq7sfvCB_!!6000000000969-2-tps-1322-814.png" width="500">

3. 实验流程改造为多次微调，补充微调时的评价标准，并根据每次微调的结果调整微调参数：

| 旧版 | 新版 |
| --- | --- |
| <img src="https://img.alicdn.com/imgextra/i2/O1CN01Lv1q6824tEwuzN4K0_!!6000000007448-2-tps-420-522.png" width="200"> <br> <img src="https://img.alicdn.com/imgextra/i4/O1CN01DD646w1NnGIn4nO8g_!!6000000001614-2-tps-1302-568.png" width="400">| <img src="https://img.alicdn.com/imgextra/i2/O1CN01X28IKu1f6MHfCnL6X_!!6000000003957-2-tps-502-484.png" width="250"> <br> <img src="https://img.alicdn.com/imgextra/i3/O1CN01mJHPPJ25es8ka6MDL_!!6000000007552-2-tps-1300-750.png" width="400"> |

<hr style="border: 2px solid black;">

## v1.1.1 切换预装vLLM的镜像
> 变更时间：2025.01.06

为解决安装vLLM库时间过长，且安装过程中可能因网络问题导致安装失败，切换为默认预装vLLM的系统镜像。

**优化/新增内容示例**

<img src="https://img.alicdn.com/imgextra/i1/O1CN01ws3kMs1SFtWdxz84o_!!6000000002218-2-tps-1856-670.png" width="550">

<hr style="border: 2px solid black;">

## v1.1.0 重构第二章课程内容
> 变更时间：2024.11.29

结合课程上线一个多月以来的问卷反馈和综合评估，决定重构第二章课程内容，提升内容质量。本次重构重点优化课程结构和内容标准，确保内容精炼连贯，不过多赘述，关键知识点释义清晰易理解，无遗漏，结构格式统一，提升阅读体验。

> 注：因内容扩充，原2.1 开始构建新人答疑机器人扩展为2.1 用大模型构建新人答疑机器人和2.2扩展答疑机器人的知识范围两个小节。其余课程序号顺延，部分小节名称有微调。

**优化/新增内容示例**

1. 课程循序渐进，内容精炼连贯，如：避免一上来就讲RAG等陌生概念，不过多赘述：

| 旧版 | 新版 |
| --- | --- |
| <img src="https://img.alicdn.com/imgextra/i1/O1CN01W8VSrw241CDKjqbhD_!!6000000007330-2-tps-1030-822.png" width="350">| <img src="https://img.alicdn.com/imgextra/i4/O1CN01Keuwg51ZBxQobQEDa_!!6000000003157-2-tps-1000-604.png" width="350"> |

2. 补充关键知识点，避免知识跳跃，降低理解难度，如：在介绍RAG前，先讲清大模型是如何工作的，并进一步了解其知识范围的局限性，从而引出RAG的作用和实现方法，旧版讲述逻辑生硬：

| 旧版 | 新版 |
| --- | --- |
| <img src="https://img.alicdn.com/imgextra/i1/O1CN01WB80Zn1BviDiV0OUP_!!6000000000008-2-tps-1062-1314.png" width="350">| <img src="https://img.alicdn.com/imgextra/i4/O1CN01ofYerG1Wo1VBhkbSI_!!6000000002834-2-tps-724-436.png" width="250"> <br> <img src="https://img.alicdn.com/imgextra/i2/O1CN013OIMKN1YT4cK7ZmTz_!!6000000003059-2-tps-1008-462.png" width="350"> <br> <img src="https://img.alicdn.com/imgextra/i2/O1CN0123IfKP25KGJlVk9i7_!!6000000007507-2-tps-1024-386.png" width="350"> <br> <img src="https://img.alicdn.com/imgextra/i4/O1CN01UXFGnl1LpQwrz7yVF_!!6000000001348-2-tps-1016-430.png" width="350"> |

3. 统一课程内容结构，如优化小结格式和内容，做到通过小结能够理解本节学了什么，以及补充应用建议和扩展知识：

| 旧版 | 新版 |
| --- | --- |
| <img src="https://img.alicdn.com/imgextra/i2/O1CN011UZkQK1N9PqOiLjKv_!!6000000001527-2-tps-1010-218.png" width="350">| <img src="https://img.alicdn.com/imgextra/i3/O1CN01bhoQ8t1IXchP50Wm6_!!6000000000903-2-tps-1010-762.png" width="350"> |

4. 可读性提升，如指代不清，语句不通顺等：

<table style="width:800px">
  <tr>
    <th>旧版</th>
    <th>新版</th>
  </tr>
  <tr>
    <td>在大模型Agent中，长期记忆对应着系统持久化的信息，如业务历史记录、知识库等，通常存储在外部向量数据库和文档库中，<mark>提供给Agent回答用户专业领域问题。</mark></td>
    <td>在大模型Agent中，长期记忆对应着系统持久化的信息，如业务历史记录、知识库等，通常存储在外部向量数据库和文档库中，<mark>Agent会利用长期记忆来回答用户私有知识或专业领域相关的问题。</mark></td>
  </tr>
</table>

<hr style="border: 2px solid black;">

## v1.0.2 优化课程阅读体验
> 变更时间：2024.10.28

为提升阅读体验，重点优化第二章内容可读性，一方面适当补充关键描述，确保上下文连贯，另一方面减少不必要的模型输出和重复性陈述。调整第二章课程顺序，将原 2.4 节（微调）后置到 2.7 节，在完成大模型应用构建后进行微调优化，更符合学习曲线。

| 旧版 | 新版 |
| --- | --- |
| <img src="https://img.alicdn.com/imgextra/i2/O1CN01n4SUi81n45F9Eztcb_!!6000000005035-2-tps-724-574.png" width="313">| <img src="https://img.alicdn.com/imgextra/i4/O1CN01wU951B1LsdijS9Pq7_!!6000000001355-2-tps-678-574.png" width="293"> |

<hr style="border: 2px solid black;">

## v1.0.1 优化课程实操体验
> 变更时间：2024.10.17

为了提供更好的实操体验，实操环境从ModelScope Notebook切换至PAI-DSW，学员可以通过领取免费CPU/GPU实例完成本课程全部章节的学习。课程内容优化方面，重点改进前言和小结的结构，突出关键知识点，重写难以理解的表述并减少赘述。优化API_KEY读取方式，精简代码并降低密钥泄露风险。

| 旧版 | 新版 |
| --- | --- |
| <img src="https://img.alicdn.com/imgextra/i1/O1CN01vB7Nva1qnNFxYHYEO_!!6000000005540-2-tps-1520-1176.png" width="450">| <img src="https://img.alicdn.com/imgextra/i2/O1CN01TB7c1B1kaCAG8PnjU_!!6000000004699-2-tps-1442-378.png" width="450"> <br> 实操环境效果： <br> <img src="https://img.alicdn.com/imgextra/i4/O1CN01KQ3Euk1qr2QOlbfjG_!!6000000005548-2-tps-964-1270.png" width="250"> |

<hr style="border: 2px solid black;">

## v1.0.0 优化实践环境的安装方法
> 变更时间：2024.10.14

课程第一版，通过项目的方式引入理论学习，并结合动手实践进一步促进理解、巩固学习，整体课程分为课程准备、构造大模型问答系统、借助大模型辅助内容生产三个章节，16个小节的内容。

<img src="https://img.alicdn.com/imgextra/i1/O1CN01Yc9ZDv1q4wq0AORJ2_!!6000000005443-2-tps-424-118.png" width="200"> <br>
<img src="https://img.alicdn.com/imgextra/i2/O1CN01FjQKGA23xzRQWXQE3_!!6000000007323-2-tps-756-874.png" width="370"> <br>
<img src="https://img.alicdn.com/imgextra/i2/O1CN011VBRbA1c2kJTmeUux_!!6000000003543-2-tps-516-438.png" width="250">