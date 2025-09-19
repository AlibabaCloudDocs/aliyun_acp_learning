## 🚄 前言 

动手实践是学习大模型的过程中必不可少的环节。为了帮助你更好的掌握相关知识，本课程设计了丰富的示例代码。

建议你通过阿里云人工智能平台 PAI 上的 [DSW](https://help.aliyun.com/zh/pai/user-guide/dsw-overview)进行课程学习，借助 PAI DSW，你可以像下图所示的那样，在阅读课程文档的同时运行代码，以便更好地理解和应用大模型。

<img src="https://img.alicdn.com/imgextra/i4/O1CN01jh8Sp41NNc4S3fp4u_!!6000000001558-1-tps-512-176.gif" alt="PAI DSW Notebook Demo" width="500px">

## 开始

### 视频教程
<video width="960" height="540" controls playbackRate="1.2">
    <source src="https://cloud.video.taobao.com/vod/lWmQQxay0s-puVoWV5rdJy7Rm3hwLvQXN797pj87LeY.mp4" type="video/mp4">
</video>

>注：本视频教程基于以下图文教程生成。[【如果演示视频不能正常播放，请点击这里】](https://cloud.video.taobao.com/vod/lWmQQxay0s-puVoWV5rdJy7Rm3hwLvQXN797pj87LeY.mp4)

### 图文教程
接下来将指引你基于 PAI DSW 准备在线学习环境。


### **环境选择**
 
你可以在自己熟悉的IDE（如 VSCode, PyCharm）中运行本课程所有代码。但为了让你获得**开箱即用**的学习体验，免去**安装IDE、配置Python等搭建本地开发环境的繁琐步骤**，更推荐你使用免费的在线 Notebook 环境。
 
主要有以下两种方案可供选择，你可以根据自己的情况任选其一：

*   **1. 阿里云 PAI-DSW (推荐)**
    *   **优点:** 新用户可领取**长达3个月**的免费额度，实例运行时长更灵活，适合长时间、连续的学习。
    *   **注意:** 免费额度用尽或到期后，**需要手动停止实例**，否则会自动按量付费。

*   **2. ModelScope 免费 Notebook**
    *   **优点:** **完全免费**，不限总使用次数，无需担心忘记关闭实例而产生费用。
    *   **注意:** 实例单次连续使用 **4 小时**后会自动关闭，需要重新启动，适合碎片化的学习。

> **本教程将以 <u>PAI-DSW</u> 为例进行详细的创建步骤演示。** 如果你选择使用 **ModelScope Notebook**，可以访问 [魔搭社区我的Notebook](https://modelscope.cn/my/mynotebook) 自行创建实例后，直接参考 **[步骤二：获取课程代码并安装依赖环境]** 进行操作，以上两种方案的环境配置方法相同。

<br>

### 步骤一：创建 PAI DSW 实例

**免费试用**：如果你是 PAI DSW 的新用户，可以通过[阿里云的免费试用频道](https://free.aliyun.com/?searchKey=%E4%BA%A4%E4%BA%92%E5%BC%8F%E5%BB%BA%E6%A8%A1+PAI-DSW)来领取免费试用额度。从领取免费试用后三个月内，你每月可以免费使用 250 计算时的CPU/GPU实例，即每月免费使用约430小时的 ecs.g6.xlarge CPU型实例或约35小时的 ecs.gn7i-c8g1.2xlarge GPU型实例。

<img src="https://scms-prod-sh-public.oss-cn-shanghai.aliyuncs.com/course_picture/eswmhiaayvhezjzedlrf.png" width="260px" alt="免费试用">

> **注意**：免费试用资源在使用后**必须手动停止**，否则额度耗尽或到期后将**自动转为按量付费**。详细操作见本文末尾的**如何停止实例与避免扣费**。

> 如果你**没有免费试用资格**，或不想使用 PAI DSW，也可以直接使用 [ModelScope 的免费 Notebook 功能](https://modelscope.cn/my/mynotebook) 完成本教程的学习。注意，该免费实例单次连续使用4小时后会自动关闭，但可以不限次数重启使用。

如果你已领取免费试用或计划正常开通，请按以下步骤创建实例：

1.  前往[PAI控制台](https://pai.console.aliyun.com/?regionId=cn-hangzhou#/workspace/overview)。
    
2.  如果你没有开通PAI平台服务，根据指引开通PAI并创建默认工作空间，点击**一键开通**。等待开通完成后，点击**进入控制台**。
    
    <img src="https://img.alicdn.com/imgextra/i4/O1CN01RWJ2Qr1Q17YDtnLKp_!!6000000001915-2-tps-1672-1014.png" width="600px">

3.  点击左侧边栏的**交互式建模（DSW）**，点击**新建实例**。

    <img src="https://img.alicdn.com/imgextra/i2/O1CN01CrbZLb1OEk0wgkBQe_!!6000000001674-0-tps-846-1076.jpg" width="300px">


4. 在新建实例页面，填写实例名称、选择资源规格和镜像：

    <img src="https://img.alicdn.com/imgextra/i1/O1CN01COwYFj1ERQtap4LW4_!!6000000000348-2-tps-2198-1388.png" width="500px">

      *   **实例名称**：可以填写**aliyun\_acp\_learning**，或者其他方便自己记忆和查找的名字。
    
      *   **资源规格**：推荐选择**免费试用页签**中的**ecs.g6.xlarge**。

          <img src="https://img.alicdn.com/imgextra/i4/O1CN01eRCLAY1rPO7SxGEfr_!!6000000005623-0-tps-1434-772.jpg" width="500px">

          > 推荐选择 CPU 实例，该规格足以运行本课程的大多数项目，可以在后续需要用到 GPU 实例的章节时，再创建 GPU 实例以减少免费额度消耗。
    
      *   **镜像**：本例需要选择`CPU类型`的镜像，推荐使用 `python 版本为 3.10` 的镜像方便后续配置，你可以通过下图方式筛选符合条件的最新镜像（如：modelscope:1.23.1-pytorch2.3.1-cpu-py310-ubuntu22.04）。 

          <img src="https://img.alicdn.com/imgextra/i2/O1CN01ZVCibE1es9zqe9BPv_!!6000000003926-0-tps-1886-1240.jpg" width="800px">
          
5. 其它保持默认，单击**确定**，完成实例的创建，实例创建通常不会超过5分钟。

    <img src="https://img.alicdn.com/imgextra/i3/O1CN013NKRsk1EFyyI9Sw3C_!!6000000000323-0-tps-1852-962.jpg" width="600px">

6. 当实例状态为运行中时，单击**操作**列中的**打开**，就可以进入到 DSW 提供的在线 Notebook 界面。

    <img src="https://img.alicdn.com/imgextra/i2/O1CN01S61kqY29kbYF456Pq_!!6000000008106-0-tps-1916-596.jpg" width="600px">

> ### **【必读】如何停止实例与避免扣费**
> 
> 免费试用额度会自动抵扣 DSW 实例的费用，但**额度耗尽或到期后，若不手动停止实例，将自动转为按量付费并产生账单**。
> 
> 因此，在不使用实例时，请**务必**返回 DSW 实例列表页面，对实例执行 **停止** 或 **删除** 操作。
>
> *   **停止**：中止计算资源（CPU/GPU）的计费，保留存储。
> *   **删除**：彻底释放所有资源，中止**所有**计费（包括可能产生的存储费用）。
> 
> 更多规则、资源释放的详细步骤，请参阅官方文档：[**PAI 免费试用领取、使用和释放**](https://help.aliyun.com/zh/pai/getting-started/free-trial-guide)。



### 步骤二： 获取课程代码并安装依赖环境

在DSW中，你可以通过点击顶部的 Terminal 来进入命令行环境.

确认环境变量，在 Terminal 中输入 `python --version` 来确认当前的 python 版本是 3.10 ，输入 `pwd` 确认当前所在目录为 <mark>/mnt/workspace</mark>。

```bash
python --version
pwd
```

<img src="https://img.alicdn.com/imgextra/i4/O1CN01wPwQH11shzpMyeyDb_!!6000000005799-0-tps-1718-384.jpg" width="600px">

如果不在 **/mnt/workspace** 目录中输入如下命令，保证后续安装顺利：

```bash
cd /mnt/workspace
```

接下来你可以通过 **自动或手动** 两种方式完成课程所需的**环境配置**和**课程文件的下载**。

#### 1. 自动安装
在 DSW 的 Terminal（终端）中执行如下命令，下载安装文件。

```bash
wget https://developer-labfileapp.oss-cn-hangzhou.aliyuncs.com/ACP/aliyun_llm_acp_install.sh
```
> 注意：对于新创建的DSW实例，当前目录里应该只有你刚刚下载的```aliyun_llm_acp_install.sh```文件，无其他内容。
> 在命令行输入```ls```命令，可查看当前目录中的内容。

执行下面的命令，自动安装课程所需的环境依赖。
```bash
/bin/bash aliyun_llm_acp_install.sh
```
<img src="https://img.alicdn.com/imgextra/i3/O1CN01xyuBfZ1ps7jnlsDal_!!6000000005415-2-tps-2388-1076.png" width="800px">

如果这一步执行顺利，你可以跳过下面手动安装的步骤。

#### 2. 手动安装

##### 2.1 下载课程代码

在 `Terminal` 中输入以下命令来获取 ACP 课程的代码：

```bash
git clone https://github.com/AlibabaCloudDocs/aliyun_acp_learning.git
```

> 如果遇到网络问题，也可以从atomgit获取：`git clone https://atomgit.com/alibabaclouddocs/aliyun_acp_learning.git`

> 如果你比较熟悉 jupyter notebook，希望在本地运行，建议你使用 python 3.10 环境来运行。

##### 2.2 手动安装依赖项

继续在 `Terminal` 中依次运行以下命令 ，安装本课程所需的依赖环境：

```shell 
# 通过 venv 模块创建名为 llm_learn 的python虚拟环境
python3 -m venv llm_learn

# 进入 llm_learn 虚拟环境
source llm_learn/bin/activate

# 在虚拟环境中更新pip
pip install --upgrade pip

# 安装 ipykernel 内核管理工具
pip install ipykernel

# 将 llm_learn 添加至 ipykernel 中
python -m ipykernel install --user --name llm_learn --display-name "Python (llm_learn)"

# 在 llm_learn 环境中安装代码执行的依赖
pip install -r ./aliyun_acp_learning/requirements.txt

# 退出 llm_learn 虚拟环境
deactivate
```


#### 3. 切换 Python 环境

完成安装步骤后，在顶部切换到Notebook，你就可以在文件树中看到aliyun_acp_learning文件夹了。
 
<img src="https://img.alicdn.com/imgextra/i3/O1CN01w44E5Q1P94lxtv9Bo_!!6000000001797-0-tps-1682-486.jpg" width="600px">

接下来你可以在文件树中依次进入 aliyun_acp_learning-大模型ACP认证教程-**p2_构造大模型问答系统** 文件夹，就能看到下一章的教程内容。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01Rn6o0s22cAwy3QqTr_!!6000000007140-0-tps-978-1408.jpg" width="320px">

课程内容安装完成后，你还需要在 Notebook课程（.ipynb 文件）右上角**选择内核**（默认内核为：Python 3 (ipykernel)），切换到刚刚创建的Python环境。如上面的创建的 `Python(llm_learn)` 环境。<br>
<img src="https://img.alicdn.com/imgextra/i2/O1CN01taOhij1R2KAIVQcts_!!6000000002053-0-tps-2962-976.jpg" width="800px"><br>
<img src="https://img.alicdn.com/imgextra/i3/O1CN01bUaGH01bC4kupRQWN_!!6000000003428-0-tps-778-632.jpg" width="320px"><br>
<img src="https://img.alicdn.com/imgextra/i1/O1CN01RUqHeu1CoDLI7526r_!!6000000000127-0-tps-780-344.jpg" width="320px"><br>

> 通常你需要手动指定每个课件的 Python 环境。Python的版本很多，不同项目使用的组件版本也不一样。本课程中使用的venv虚拟环境可以为每个项目创建独立的Python环境，避免版本冲突，简化依赖管理。

顺利执行上述步骤后，就可以开始学习课程了。祝你在之后的学习之旅中一切顺利！<br>


## 扩展阅读
为了方便阅读，你可以通过左侧菜单，打开当前文档的导读界面：

<img src="https://img.alicdn.com/imgextra/i1/O1CN01Ep5AcP1Z7NSeB2ztS_!!6000000003147-0-tps-1960-980.jpg" alt="导读" width="600px">

如果你不习惯深色主题，也可以在顶部的 Settings 菜单中调整：

<img src="https://img.alicdn.com/imgextra/i4/O1CN01E7kH2F1fBqzPMkkoZ_!!6000000003969-2-tps-961-279.png" alt="设置" width="600px">

### DSW 的常见问题

Q1: 为什么 DSW 里的 WebIDE 和 Notebook 交互输入框位置不一样？

A1: 在 2.1 教程中，你会输入 API Key，如果你使用 Notebook，那么输入框会非常容易看到（就在运行代码块的下方）；

<img src="https://img.alicdn.com/imgextra/i1/O1CN01bNeIzG1PJ9SjOilw7_!!6000000001819-0-tps-1642-286.jpg" width="500px" alt="切换kernel">

如果你使用 WebIDE，那么输入框会出现在代码文件的正上方。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01horPgp1foKH3nnLW8_!!6000000004053-0-tps-1660-604.jpg" width="500px" alt="切换kernel">

Q2: 在 Notebook 中能够直接看到图片，可是为什么双击图片所在的 Markdown 块后，图片就显示不出来了？

A2: 这是因为双击图片所在的 Markdown 块后就进入了编辑模式，你只要点击 Markdown 块之外的代码块进入查看模式，图片就会显示出来了。

<img src="https://img.alicdn.com/imgextra/i4/O1CN012mnKlz1Q5hRev3onD_!!6000000001925-1-tps-1240-372.gif" width="500px" alt="切换kernel">

Q3: 我注意到 Git 仓库有更新，应该怎么拉取到最新代码？

A3: 你可以在命令行（ Terminal ）中操作。

请先确认你所在的文件夹，通常是 “aliyun_acp_learning”
在命令行中通过 “cd” 指令切换当前目录，如：
```shell
cd aliyun_acp_learning
```

接着，你可以在命令行（ Terminal ）中依次运行以下命令：
```shell
git checkout .
git pull
```

请注意：该动作会覆盖本地代码，如果你需要保留本地的运行结果，请备份后再运行。

Q4: 我在执行 `git clone` 命令时，速度很慢，并且报了超时的错误，应该怎么办？

A4: 你可以停止该实例，在切换到其它地域后，重新创建一个实例并拉取代码。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01BSl0Ku1Hef8xRAm9Q_!!6000000000783-0-tps-958-1112.jpg" width="300px" alt="切换region">

