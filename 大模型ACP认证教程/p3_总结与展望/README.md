# 3 总结与展望

通过前面课程的学习，你通过构建一个答疑机器人，并逐步优化，深入了解了大模型应用的开发及改进过程。
以下是几个关键点：

1. **上线容易，提升不易**：虽然大模型应用从开发到上线相对简单，但要取得好的效果则需要持续投入、和对业务的深入理解。与业务领域专家共同建立客观的评测方法、以及高效的评测机制是非常重要的。
   
2. **逐级优化，不断迭代**：改善大模型应用效果的方法多样，包括优化提示词、使用RAG（检索增强生成）、添加工具以及微调。推荐优先尝试成本较低的方法，如提示词优化或RAG，再考虑是否需要进行更复杂的操作，比如微调。

3. **多智协同，优势互补**：大模型具备类似人类的思考能力，构建一个多智能体系统可能会比单独的大模型更加高效强大。

4. **面向生产，注重实效**：如同传统计算机系统一样，在开发过程中也需要重视系统的性能、成本、稳定性和安全性等非功能性方面。

虽然我们是以构建 RAG 为起点，来学习大模型应用，但大模型的实际应用远不止于此。


## 🧑🏻‍💻 1. 动手体验：构建更复杂的 AI 应用

为了让你实际体验一些具体的AI应用场景，非常建议你实际体验以下几个 AI 技术解决方案。这些方案覆盖了从数据提取到内容创作、客服系统构建以及实时音视频互动等多个领域。

### 1.1 多模态数据信息提取

试想一下，你有一万张衣服商品图片，需要提取一些信息（如花纹、衣领款式），人工打标费事费力。而现在，你可以借助视觉理解大模型来自动化完成这一任务。

<a href="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8057905371/p893653.gif" target="_blank">
<img src="https://img.alicdn.com/imgextra/i3/O1CN01ex7Wxr1m8NKMoeg6u_!!6000000004909-1-tps-700-438.gif" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">
</a>

除了能够从商品图片中提取结构化信息之外，你还可以借助视觉理解模型来实现纸质表单信息提取、视频理解等。

<a href="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8057905371/p893650.gif" target="_blank">
<img src="https://img.alicdn.com/imgextra/i3/O1CN01AvlD3y1WIsYfYX8NG_!!6000000002766-1-tps-1200-750.gif" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">
</a>
<br/>
<a href="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8057905371/p893654.gif" target="_blank">
<img src="https://img.alicdn.com/imgextra/i1/O1CN01UcF39n1Ha5COllsvc_!!6000000000773-1-tps-800-500.gif" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">
</a>

你可以前往阿里云技术解决方案频道[立即体验](https://www.aliyun.com/solution/tech-solution/information-extraction)这一方案，该方案将引导你自动完成一个视觉应用的搭建，并且提供了完整源码供你参考。

### 1.2 AI 剧本生成与动画创作
当你想给孩子展示 AI 的魅力，或者为你的朋友圈里增添一些 AI 惊喜时，你都可以考虑使用阿里云推出的[AI 剧本生成与动画创作](https://www.aliyun.com/solution/tech-solution/animation-creation)解决方案。通过“在线部署”，随时体验一键创作视频的乐趣。

<a href="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7156285371/p897795.gif" target="_blank">
<img src="https://img.alicdn.com/imgextra/i1/O1CN01ZG3tNO1XxTHDoWNcP_!!6000000002990-1-tps-800-500.gif" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">
</a>

你可以和家人或朋友一起设计动画的角色形象、剧情梗概，剩下的事情完全交给AI自主完成。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01MKfrhZ1qbSwiznL4d_!!6000000005514-2-tps-1213-471.png" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">

你可以[立即部署一个实例](https://www.aliyun.com/solution/tech-solution-deploy/2863572)来体验这个解决方案，该方案会引导你搭建一个多智能体工作流，并提供了完整的源码供你参考。


### 1.3 10 分钟构建 AI 智能助手
不论是网页上，还是钉钉群、微信公公众号或企业微信，阿里云的[10 分钟构建 AI 客服](https://www.aliyun.com/solution/tech-solution/build-a-chatbot-for-your-website-or-chat-system) 解决方案系列，能帮你轻松引入 AI 客服，全天候响应客户的咨询。

你可以前往阿里云的解决方案频道[立即部署](https://www.aliyun.com/solution/tech-solution/build-a-chatbot-for-your-website-or-chat-system#1a8f16674edv0)这一方案，构造一个网页版 AI 助手。

<a href="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8936289171/p816074.gif" target="_blank">
<img src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8936289171/p816074.gif" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">
</a>




你也可以尝试其他解决方案，将 AI 助手快速嵌入钉钉或微信公众号中。

|在钉钉中添加一个 AI 问答机器人|让微信公众号成为 AI 助手|在企业微信中集成一个 AI 助手|
|----|----|----|
|<img src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2120582271/p830568.gif" width="220" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;"> |<img src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9763691271/p825777.gif" width="220" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">|<img src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7752553271/p834112.gif" width="220" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">|
|[立即部署一个钉钉群机器助理](https://www.aliyun.com/solution/tech-solution/build-a-chatbot-for-your-website-or-chat-system#c3982bca67jqn)|[立即部署一个微信公众号客服](https://www.aliyun.com/solution/tech-solution/build-a-chatbot-for-your-website-or-chat-system#9b3e0c1c88c6k)|[立即部署一个企业微信客服](https://www.aliyun.com/solution/tech-solution/build-a-chatbot-for-your-website-or-chat-system#56befd5038eti)|

> 参考本解决方案的步骤，你只需要提供相关配置信息，无需编写代码就可以实现各类端应用和百炼AI应用的关联。
> 而在百炼上，你可以构建和优化专属AI助理，并提供私域知识库问答服务，从而为你的端应用提供AI能力。

### 1.4 与AI实时音视频通话
具备视频交互能力的 AI 应用，拥有了帮助人们解决生活中各类问题的巨大潜力。无论是健身、做菜等日常需求，还是助残、导盲等更具社会意义的场景，视频通话能力已经成为 AI 应用跨界创新的利器。通过阿里云推出的[AI 实时音视频互动](https://www.aliyun.com/solution/tech-solution/real-time-interaction)解决方案，你可以快速搭建与大模型进行视频聊天的应用。同时，依托视频云 ARTC 网络，整个交互过程稳定高效，延迟极低，完全满足商业化场景的需求。

<a href="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7372426371/p900862.gif" target="_blank">
<img src="https://img.alicdn.com/imgextra/i2/O1CN01gMa86k1sRVZDs7jYO_!!6000000005763-1-tps-700-438.gif" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">
</a>

你也可以选择搭建音频对话助手，看哪种更适合你的业务需求。

<a href="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7372426371/p900861.gif" target="_blank">
<img src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7372426371/p900861.gif" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">
</a>


现在就[部署一个实例](https://www.aliyun.com/solution/tech-solution/real-time-interaction)，开启你的未来之旅！


### 1.5 与AI程序员结伴编程，秒变全栈开发
你可能想在你的电商系统中快速添加一项新功能，但却苦于人手不足？灵码AI程序员就是你24小时随叫随到的编程伙伴！它能：
- **一键生成全流程**
从需求实现到单元测试，从代码修复到批量修改，复杂代码编写"一键生成”，AI全程智能协作
- **全栈需求零压力**
前后端开发同步推进——前端界面交互、后端服务逻辑，AI自动完成多文件联调，开发效率翻倍
- **解放双手创价值**
你专注架构设计与核心逻辑，重复性代码、配置维护、测试用例等琐事交给AI自主完成


<a href="https://cloud.video.taobao.com/vod/Fio3xBNUr52SZQ0NNbg0KzlRVzeHoA0BpLBjnyyG6vA.mp4" target="_blank">
<img src="https://img.alicdn.com/imgextra/i2/O1CN01l2Losi1ljdwOoa054_!!6000000004855-1-tps-600-336.gif" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">
</a>

详细流程请参考[灵码AI程序员与开发者结伴编程](https://developer.aliyun.com/article/1658034)，现在就让 AI 程序员成为你的左膀右臂，[立即下载体验](https://help.aliyun.com/zh/lingma/user-guide/download-the-installation-guide)！


> 如果你想实现提交代码后自动触发流水线，自动执行代码检测和单元测试，从开发到代码CI/CD全流程管理，阿里云还提供了[企业级智能编码解决方案](https://www.aliyun.com/solution/tech-solution/intelligent-coding?spm=5176.29677750.J_7uZrZlgl1hzBH9MLq1qLS.d_5_action_0.5f02154aSfWf1n)，通过将灵码与云效相结合，进一步提高你对项目的管理能力，确保软件按时高质量交付。


## 🌏 2. AI正在影响着千行百业

AI与大模型已经在很多领域有了成功落地，以下案例涵盖了医疗、娱乐、教育等多个领域，通过了解这些实际应用场景，你不仅可以更直观地感受到 AI 技术的强大能力，还能从中获得灵感，为自己的行业找到创新的突破口和实用的解决方案。


### 2.1 医疗领域：辅助诊断与健康管理
在医疗领域，AI 与大模型的创新项目层出不穷。阿里云与[阿斯利康合作](http://www.djkpai.com/ai/177960.jhtml)，通过融入海量医学知识文献与医疗数据，让大模型可以生成药品的不良反应报告，提升医药研发效率。达摩院的医疗AI团队2020年开发了一款基于AI的大型辅助诊断系统[“达医智影”](https://www.xinhuanet.com/tech/20240223/ba113561f9974296aca94089befed8e1/c.html)，能够通过分析患者的CT影像快速准确地对新冠肺炎疑似病例进行诊断，诊断时间仅需20秒，准确率达到96%以上。此外，阿里巴巴与多家医院合作，通过其AI系统显著提升了肺部疾病的筛查效率，将原本需要几个小时的影像分析缩短到仅需数分钟。

|达医智影|
|:---:|
|<img src="https://img.alicdn.com/imgextra/i4/O1CN01wjYIYH242ZOEA8BAW_!!6000000007333-2-tps-900-487.png" style="height:200;box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">|

> 请注意：AI 建议和 AI 处方仅作为辅助信息，医疗决策应由专业医生根据患者的实际情况综合判断。


### 2.2 娱乐产业：内容创作与虚拟偶像
娱乐产业是另一个受益于大模型技术的重要领域。厘里是一位由AI深度融合技术驱动的虚拟偶像，能够与真人拍摄的场景无缝融合，展现出极高的真实性和拟人化程度。厘里曾出演真人热播剧《异人之下》，并在2023年世界互联网大会乌镇峰会上以全息互动形式亮相，吸引了大批参会人员的关注。此外，数字人技术方面的持续创新，通过AI驱动的方式进行实时互动，如虚拟主播和数字员工的应用，也能帮助品牌打造独具特色的直播场景和营销活动。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01DOzYDY1XFxeJLeuYL_!!6000000002895-2-tps-956-1698.png" height="400" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;"><img src="https://img.alicdn.com/imgextra/i2/O1CN01G7AOmz1RNqmIbhEdd_!!6000000002100-2-tps-864-1437.png" height="400" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;"><img src="https://img.alicdn.com/imgextra/i3/O1CN01PH880m1cG1mojjo6L_!!6000000003572-2-tps-1404-1868.png" height="400" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">

> 虚拟主播技术 （Virtual Youtuber，简称Vtuber）涉及多个领域，而在多模态大模型的加持下虚拟主播走进现实。


### 2.3 教育行业：个性化学习与智能辅导
在教育领域，大模型同样展现出了巨大的潜力。[精准学](https://www.91jzx.cn/)基于阿里巴巴的千问大模型，开发了一款智能辅导系统[超拟人AI一对一老师](https://news.qq.com/rain/a/20240921A03V7N00)，为学生提供个性化的学习方案。该系统能够根据学生的学习进度和薄弱环节，自动调整教学内容和难度，确保每位学生都能获得最适合自己的教育资源。此外，精准学与钉钉、千问合作推出的超拟人一对一AI老师普惠计划，将为偏远地区及弱势群体提供AI辅学资源，进一步推动教育的普惠化。

<img src="https://img.alicdn.com/imgextra/i4/O1CN01Aio9W11Dzx6feTbqT_!!6000000000288-2-tps-3438-1842.png" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">

> AI 个性化辅导有着广泛的应用前景，不论是辅助教师研讨，还是24小时助学答疑，AI应用都在影响着人们的教育理念和教学方式。

## 🎓 3. 不断探索

技术研发工作总是令技术工作者们兴奋不已，大家你追我赶、互相超越，共同推动技术的边界。如今，大模型的应用正在全球范围内掀起一波又一波的技术浪潮。就在不久前，DeepSeek-R1在全球榜单中崭露头角，而Manus AI的问世更是将智能体研究推向了新的高度。

希望你能以本课程为起点，继续探索大模型技术的无限可能，在实践中不断提升自我，创造出更多兼具社会价值与商业价值的应用，与全球开发者一起，共同书写人工智能的新篇章！

### 3.1 扩展阅读：深度思考模型QwQ
QwQ大模型是一款基于Qwen2.5系列训练的强推理能力AI模型，分为商业版和开源版。商业版（如qwq-plus）通过强化学习显著提升了数学、代码及通用任务性能，核心指标媲美DeepSeek-R1满血版，并提供稳定与最新快照版本选择；开源版（如qwq-32b）同样表现出色，超越同类蒸馏模型。模型支持超长上下文（131,072 tokens）、多轮对话功能，可实现连续交流场景，但不支持工具调用、结构化输出等功能。模型设计注重推理效果，适合需要深度思考与高质量回复的应用场景。

你可以在百炼上[体验QwQ系列模型](https://bailian.console.aliyun.com/#/efm/model_experience_center/text?currentTab=textChat&modelId=qwq-plus-latest)，你也可以查阅阿里云帮助中心[获取更多信息](https://help.aliyun.com/zh/model-studio/user-guide/qwq)。


## 🔥 课后小测验
【单选题】在业务环境中快速验证新 AI 工具的有效策略是什么？

- A. 在实施前先进行广泛全面的市场研究
- B. 选择一小群有代表性的用户进行试点
- C. 立即着手进行大规模部署
- D. 待竞争对手先测试该方法，然后跟进

**参考答案**：B

**答案解释**：小规模试点可以有效控制风险，避免因技术不成熟或业务场景不合适而导致项目失败。

---


## **🎊 恭喜！你已经完成了大模型ACP认证课程的学习！👏**

学习贵在持之以恒，感谢你一直坚持到现在。接下来，你可以参加认证考试了。

为了让你能够更顺利的拿到认证，这里有一份认证考试的模拟题，你可以访问阿里云培训中心的[大模型ACP认证模拟考试](https://edu.aliyun.com/clouder/exam/intro/1107)来检验一下你的学习成果。

当然，如果你已经充分掌握了大模型开发的基础知识，你也可以登录阿里云，报名[认证考试](https://edu.aliyun.com/certification/acp26)，预祝你考试顺利！

<img src="https://aliyun-aps-cloud-public.oss-cn-hangzhou.aliyuncs.com/img_946b7422dd46687c5d0c5916e2bc92a5.png?x-oss-process=image/resize,h_400,m_lfit" width="700" style="box-shadow: rgba(99, 99, 99, 0.21) 0px 1px 8px 0px;">



## ✉️ 评价反馈
大模型ACP认证课程的学习内容至此结束，感谢你的支持与帮助，如果你觉得课程有哪里写得好、哪里写得不好，期待你通过问卷[提交评价和反馈](https://survey.aliyun.com/apps/zhiliao/Mo5O9vuie)。

你的批评和鼓励都是我们前进的动力。




