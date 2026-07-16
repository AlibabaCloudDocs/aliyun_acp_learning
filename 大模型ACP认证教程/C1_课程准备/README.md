## 🚄 前言 

学习大模型应用开发，最重要的是把代码跑起来，再理解每一步为什么这样做。本课程准备了完整的示例代码，你可以先在自己的电脑上下载课程代码，安装 `requirements.txt` 中的依赖，再用 VSCode、PyCharm 等熟悉的 IDE 打开和运行；课程代码不绑定某一种运行环境。

如果你还不熟悉 Python 环境配置，也可以使用在线 Notebook，这样可以少花时间搭环境，把注意力放在课程内容上。ModelScope Notebook 免费，但单次实例连续使用 4 小时后会自动关闭；PAI-DSW 不会随意删除你的实例，更适合连续学习，但要先确认免费试用资格和计费规则。PAI-DSW 只是可选学习环境，不是本课程的强制购买项。请先阅读“**环境选择**”，再决定使用哪种环境。

<img src="https://img.alicdn.com/imgextra/i4/O1CN01jh8Sp41NNc4S3fp4u_!!6000000001558-1-tps-512-176.gif" alt="PAI DSW Notebook Demo" width="500px">


## 开始

### 视频教程
<video width="960" height="540" controls playbackRate="1.2">
    <source src="https://cloud.video.taobao.com/vod/lWmQQxay0s-puVoWV5rdJy7Rm3hwLvQXN797pj87LeY.mp4" type="video/mp4">
</video>

>注：本视频教程基于以下图文教程生成。[【如果演示视频不能正常播放，请点击这里】](https://cloud.video.taobao.com/vod/lWmQQxay0s-puVoWV5rdJy7Rm3hwLvQXN797pj87LeY.mp4)

### 图文教程
接下来将指引你准备学习环境。本文会重点演示 PAI-DSW 的创建步骤，是为了给不熟悉本地开发环境配置的学员提供一条可以照着操作的路径；如果你选择本地 IDE 或 ModelScope Notebook，可以跳过 PAI-DSW 创建步骤，直接从“**步骤二：获取课程代码并安装依赖环境**”开始。

### **环境选择**
 
本课程代码对运行环境没有强绑定，PAI-DSW 也不是必选项。你可以先根据自己的情况选择学习环境：

| 如果你... | 建议选择 | 需要注意 |
| --- | --- | --- |
| 已有 Python 环境，习惯在自己电脑上开发 | **本地 IDE** | 下载代码、安装 `requirements.txt` 后即可运行 |
| 不想配置本地环境，又希望零成本学习 | **ModelScope 免费 Notebook** | 免费使用，但单次连续运行 **4 小时**后会自动关闭，需要重新启动 |
| 希望实例保留、连续学习，并且确认自己有免费试用资格 | **PAI-DSW** | 需要主动管理实例和账单；学习结束后必须停止或删除实例 |
| 不确定自己有没有 PAI-DSW 免费试用资格 | **本地 IDE** 或 **ModelScope 免费 Notebook** | 先不要创建 PAI-DSW 实例 |

> ### **【PAI-DSW 费用提醒｜创建实例前请确认】**
>
> **创建实例前，请先确认这 4 件事。** 任意一项不确定，都建议先使用 **本地 IDE** 或 **ModelScope 免费 Notebook**。
>
> 1. **我已经领取 PAI-DSW 免费试用额度。**
> 2. **我创建的是“免费试用”页签里的实例规格。**
> 3. **我优先选择 CPU 实例，没有随手创建 GPU 实例。**
> 4. **我知道学习结束后要停止或删除实例。**
>
> **同时，请特别注意以下费用和实例规则：**
>
> - **3 个月有效期不等于 3 个月无限免费。** 免费试用按“计算时”抵扣：领取后 3 个月内，每月发放 250 计算时，总计可享 750 计算时；当月额度用尽后，超出部分会按量计费。
> - **课程费用不包含 PAI-DSW 资源费用。** PAI-DSW 是阿里云产品资源，免费试用资格、额度、地域和实例规格以控制台实际页面为准。
> - **初学者建议先用 CPU 实例。** 本课程大多数内容使用 CPU 实例即可完成。只有《4.1 用蒸馏让小模型掌握专业能力》和《4.2 部署模型》两个课程建议使用 GPU 实例。为了减少 GPU 依赖安装等待时间，课程提供了预置 GPU 镜像；如果你要学习 4.1 或 4.2，可以参考本课时后面的 GPU 实例与镜像配置说明单独创建 GPU 实例。GPU 实例消耗计算时更快，也更容易在额度用尽后产生较高费用。
> - **关闭浏览器不等于停止实例。** 不学习时必须回到 DSW 实例列表，手动执行“停止”或“删除”。

> **本教程将以 <u>PAI-DSW</u> 为例演示云端环境的创建步骤，不代表必须使用 PAI-DSW。** 如果你选择 **本地 IDE**，可以在本地终端中参考 **[步骤二：获取课程代码并安装依赖环境]** 下载代码并安装依赖；如果你选择 **ModelScope Notebook**，可以访问 [魔搭社区我的Notebook](https://modelscope.cn/my/mynotebook) 自行创建实例后，再参考步骤二继续操作。

<br>


### 步骤一：创建 PAI DSW 实例

这一节只做一件事：创建一个 DSW 实例，然后打开 JupyterLab。

如果你只是跟着课程跑代码，先用 CPU。等学到 4.1、4.2 微调和部署时，再单独创建 GPU 实例。

#### 1. 先确认要不要用 DSW

PAI-DSW 不是必选项。如果你想零成本学习，可以使用 [ModelScope 免费 Notebook](https://modelscope.cn/my/mynotebook) 或本地 IDE。

如果你决定使用 PAI-DSW，先确认这几件事：

| 确认项 | 建议 |
| --- | --- |
| 免费试用额度 | 不确定有没有额度时，先不要创建实例 |
| 实例规格 | 课程 1.x、2.x、3.x 用 CPU；课程 4.1、4.2 再用 GPU |
| 计费风险 | 学完及时停止或删除实例 |

如果你是已完成认证的阿里云用户，且是 PAI-DSW 产品新用户，可以尝试通过[阿里云免费试用频道](https://free.aliyun.com/?searchKey=%E4%BA%A4%E4%BA%92%E5%BC%8F%E5%BB%BA%E6%A8%A1+PAI-DSW)领取免费试用额度。免费试用通常按计算时抵扣，不是无限免费；当月额度用完后，超出部分会按量计费。

> 免费试用资格、额度、可用机型和活动规则可能调整，请以控制台实际展示为准。创建实例前，请确认页面上显示的是“免费试用”页签中的可用规格，并确认计费提示符合你的预期。

<img src="https://scms-prod-sh-public.oss-cn-shanghai.aliyuncs.com/course_picture/eswmhiaayvhezjzedlrf.png" width="260px" alt="免费试用">

如果你遇到**没有免费 CPU 资源**的情况，可以在 PAI-DSW 控制台左上角切换地域到杭州或张家口等地。

<img src="https://img.alicdn.com/imgextra/i3/O1CN013fGAf41dmNTgcpcpM_!!6000000003778-2-tps-1922-872.png" width="700px" alt="免费试用">
<br/>
<img src="https://img.alicdn.com/imgextra/i3/O1CN01ea56RX24SDffLjf07_!!6000000007389-2-tps-1310-526.png" width="500px" alt="免费试用">

#### 2. 选择 CPU 还是 GPU

先看你学到哪一章：

| 学习内容 | 推荐实例 | 镜像 | 说明 |
| --- | --- | --- | --- |
| 1.x、2.x、3.x：普通代码开发、RAG、Agent、评测等 | `ecs.g6.xlarge` | 官方镜像 | 默认选择 |
| 4.1、4.2：模型蒸馏、微调、部署 | `ecs.gn7i-c8g1.2xlarge` | 课程 GPU 预置镜像 | 只在学习这两节时创建 |

> 经验建议：不要一开始就开 GPU。GPU 费用更高，也消耗免费额度更快。前面章节用 CPU 学习即可。

#### 3. 进入 DSW 创建页

1. 前往 [PAI 控制台](https://pai.console.aliyun.com/?regionId=cn-hangzhou#/workspace/overview)。
2. 如果页面提示未开通 PAI，按提示点击**一键开通**。开通完成后，点击**进入控制台**。

<img src="https://img.alicdn.com/imgextra/i4/O1CN01RWJ2Qr1Q17YDtnLKp_!!6000000001915-2-tps-1672-1014.png" width="600px">

3. 点击左侧边栏的**交互式建模（DSW）**，点击**新建实例**。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01CrbZLb1OEk0wgkBQe_!!6000000001674-0-tps-846-1076.jpg" width="300px">

#### 4. 填写实例信息

在新建实例页面，先填写实例名称，再选择资源规格和镜像。

| 配置项 | 填写建议 |
| --- | --- |
| 实例名称 | 可以填写 `aliyun_acp_learning`，或其他方便记忆的名称 |
| 地域 | 优先选择有可用资源和免费额度的地域 |
| 资源规格 | 按第 2 节选择 CPU 或 GPU |
| 镜像 | 按下面的说明选择 |

<img src="https://img.alicdn.com/imgextra/i1/O1CN01COwYFj1ERQtap4LW4_!!6000000000348-2-tps-2198-1388.png" width="500px">

#### 5. 如果你选 CPU

适用于 1.x、2.x、3.x 课程，也是默认推荐路径。

| 配置项 | 选择 |
| --- | --- |
| 资源规格 | 优先选择**免费试用页签**中的 `ecs.g6.xlarge` |
| 镜像类型 | 官方镜像 |
| 镜像版本 | 推荐使用 `modelscope:1.38.0.1-pytorch2.10.0-gpu-py312-cu128-ubuntu22.04` |

如果页面没有“免费试用”页签、没有可用免费规格，或计费提示不符合预期，先不要创建实例。可以改用 ModelScope Notebook 或本地 IDE。

<img src="https://img.alicdn.com/imgextra/i4/O1CN01eRCLAY1rPO7SxGEfr_!!6000000005623-0-tps-1434-772.jpg" width="500px">
<br/>
<img src="https://img.alicdn.com/imgextra/i2/O1CN01ZVCibE1es9zqe9BPv_!!6000000003926-0-tps-1886-1240.jpg" width="800px">

#### 6. 如果你选 GPU

只在学习《4.1 用蒸馏让小模型掌握专业能力》和《4.2 部署模型》时使用。创建前再确认一次计费方式和免费额度。

| 配置项 | 选择 |
| --- | --- |
| 资源规格 | `ecs.gn7i-c8g1.2xlarge`（8 vCPU，30 GiB，NVIDIA A10 * 1） |
| 镜像类型 | 自定义镜像 |
| 镜像地址 | `crpi-mh4e7zguxmvd98wb.cn-hangzhou.personal.cr.aliyuncs.com/aly-llm-acp/aly-llm-acp:aly-llm-acp-gpu01` |

这份镜像已经预装 GPU 依赖，可以省掉约 1.5 小时的安装等待。下载模型文件后，就可以开始微调实验。如果当前地域没有 GPU 库存，可以切换地域，或选择同等/更高显存的 GPU 规格。

<img src="https://img.alicdn.com/imgextra/i1/O1CN01jPlDOb1Sf5PYIKQvh_!!6000000002273-2-tps-2444-1762.png" width="800px" alt="从镜像创建 DSW GPU 实例">

#### 7. 创建并打开实例

1. 创建前再次检查资源规格、镜像、地域和计费提示。
2. 确认无误后，单击**确定**。实例创建通常不超过 5 分钟。

<img src="https://img.alicdn.com/imgextra/i3/O1CN013NKRsk1EFyyI9Sw3C_!!6000000000323-0-tps-1852-962.jpg" width="600px">

3. 当实例状态为运行中时，单击**操作**列中的**打开**，进入 DSW 开发环境。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01S61kqY29kbYF456Pq_!!6000000008106-0-tps-1916-596.jpg" width="600px">

4. 首次进入 DSW 时，会看到欢迎页面（启动台）。点击 **JupyterLab**，进入 Notebook 开发环境。

<img src="https://img.alicdn.com/imgextra/i4/O1CN016y1uAW26W0BPLWNLF_!!6000000007668-2-tps-1790-1018.png" width="800px" alt="DSW启动台：点击顶部+号回到欢迎页面，再点击JupyterLab进入开发环境">

如果你已经进入了 Terminal 或其他工具，可以点击顶部的 **"+"** 号回到启动台，再选择 JupyterLab。步骤二会用到 Terminal，后面也可以用同样的方法打开。

#### 8. 完成标准

看到 JupyterLab 页面，就说明步骤一完成。接下来进入步骤二，在 Terminal 中获取课程代码并安装依赖。

> ### **学习结束后，请及时停止或删除 PAI-DSW 实例**
>
> 只关闭浏览器、Notebook 页面或电脑盖子，都不会停止云端实例。不学习时，请回到 DSW 实例列表，执行 **停止** 或 **删除**。
>
> | 操作 | 作用 |
> | --- | --- |
> | 停止 | 中止计算资源（CPU/GPU）的计费，保留存储 |
> | 删除 | 彻底释放所有资源，中止所有计费，包括可能产生的存储费用 |
>
> 建议每天学习结束后立即停止实例；如果后续不再使用，直接删除实例。更多规则、资源释放的详细步骤，请参阅官方文档：[**PAI 免费试用领取、使用和释放**](https://help.aliyun.com/zh/pai/getting-started/free-trial-guide)。


### 步骤二： 获取课程代码并安装依赖环境

无论你使用本地 IDE、ModelScope Notebook 还是 PAI-DSW，后续都需要先获取课程代码，并安装 Python 依赖。

如果你使用 PAI-DSW，可以点击顶部的 **"+"** 号回到欢迎页面（顶部标签为"启动台"），然后点击 **Terminal** 卡片打开命令行终端。建议在 Terminal 中输入 `python --version` 查看当前 Python 版本，并输入 `pwd` 确认当前所在目录为 <mark>/mnt/workspace</mark>。

```bash
python --version
pwd
```

<img src="https://img.alicdn.com/imgextra/i4/O1CN01wPwQH11shzpMyeyDb_!!6000000005799-0-tps-1718-384.jpg" width="600px">

如果你使用 PAI-DSW，且当前不在 **/mnt/workspace** 目录中，请输入如下命令，保证后续安装顺利：

```bash
cd /mnt/workspace
```

如果你使用本地 IDE，请在本地终端中进入你希望保存课程代码的目录；不需要切换到 `/mnt/workspace`。

接下来你可以通过 **自动或手动** 两种方式完成课程所需的**环境配置**和**课程文件的下载**。

#### 1. 自动安装
如果你使用 PAI-DSW，可以在 DSW 的 Terminal（终端）中执行如下命令，下载安装文件。本地 IDE 或 ModelScope Notebook 用户也可以直接参考后面的“手动安装”步骤。

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

完成安装步骤后，点击顶部的 **"+"** 号回到欢迎页面（顶部标签为"启动台"），再点击 **JupyterLab** 卡片进入 Notebook 环境，你就可以在文件树中看到aliyun_acp_learning文件夹了。
<img src="https://img.alicdn.com/imgextra/i1/O1CN01bSnCEt204coVVMcUE_!!6000000006796-2-tps-2514-1430.png" width="800px" alt="DSW启动台：点击顶部+号回到欢迎页面，再点击JupyterLab进入开发环境">
<img src="https://img.alicdn.com/imgextra/i3/O1CN01w44E5Q1P94lxtv9Bo_!!6000000001797-0-tps-1682-486.jpg" width="600px">

接下来你可以在文件树中依次进入 aliyun_acp_learning-大模型ACP认证教程-**C2_构造问答系统** 文件夹，就能看到下一章的教程内容。

<img src="https://img.alicdn.com/imgextra/i3/O1CN01Woep6N1OMWt6MBpYH_!!6000000001691-2-tps-894-976.png" width="320px">

课程内容安装完成后，你还需要在 Notebook课程（.ipynb 文件）右上角**选择内核**（默认内核为：Python 3 (ipykernel)），切换到刚刚创建的Python环境。如上面的创建的 `Python(llm_learn)` 环境。<br>
<img src="https://img.alicdn.com/imgextra/i4/O1CN01BrM5xg1oig3BTXEJR_!!6000000005259-2-tps-2884-930.png" width="800px"><br>
<img src="https://img.alicdn.com/imgextra/i3/O1CN01bUaGH01bC4kupRQWN_!!6000000003428-0-tps-778-632.jpg" width="320px"><br>
<img src="https://img.alicdn.com/imgextra/i1/O1CN01RUqHeu1CoDLI7526r_!!6000000000127-0-tps-780-344.jpg" width="320px"><br>

> 通常你需要手动指定每个课件的 Python 环境。Python的版本很多，不同项目使用的组件版本也不一样。本课程中使用的venv虚拟环境可以为每个项目创建独立的Python环境，避免版本冲突，简化依赖管理。

顺利执行上述步骤后，就可以开始学习课程了。祝你在之后的学习之旅中一切顺利！<br>

## 扩展阅读
为了方便阅读，你可以通过左侧菜单，打开当前文档的导读界面：

<img src="https://img.alicdn.com/imgextra/i1/O1CN01Ep5AcP1Z7NSeB2ztS_!!6000000003147-0-tps-1960-980.jpg" alt="导读" width="600px">

如果你不习惯深色主题，也可以在顶部的 Settings 菜单中调整：

<img src="https://img.alicdn.com/imgextra/i3/O1CN016P9Mrh27rMG0XUuZN_!!6000000007850-2-tps-1342-716.png" alt="设置" width="600px">

### DSW 的常见问题

#### Q1：选择 `Python (llm_learn)` 内核后，Notebook 一直显示 Connecting，或者很快断开，怎么办？

**答：** 这通常说明 Jupyter 内核注册信息和当前实例中的 `llm_learn` 环境没有正确对应。课程安装脚本会自动处理内核注册；如果你使用的是课程 GPU 预置镜像，或实例由镜像复制而来，偶尔也可能遇到内核连接异常。

可以先在 DSW 的 Terminal 中重新执行安装脚本；如果你只需要重新注册内核，也可以在 Terminal 中执行：

```bash
source llm_learn/bin/activate
python -m ipykernel install --user --name llm_learn --display-name "Python (llm_learn)"
deactivate
```

执行完成后，回到 Notebook 页面，重新选择 `Python (llm_learn)` 内核。如果仍然连接不上，可以重启当前 DSW 实例后再试。

---

#### Q2：为什么 DSW 里的 WebIDE 和 Notebook 交互输入框位置不一样？

**答：** 在 2.1 教程中，你会输入 API Key。如果你使用 Notebook，输入框会显示在运行代码块的下方，比较容易看到。

<img src="https://img.alicdn.com/imgextra/i1/O1CN01bNeIzG1PJ9SjOilw7_!!6000000001819-0-tps-1642-286.jpg" width="500px" alt="切换kernel">

如果你使用 WebIDE，那么输入框会出现在代码文件的正上方。

<img src="https://img.alicdn.com/imgextra/i4/O1CN016iD5sy1mMZhotjZ2g_!!6000000004940-2-tps-1502-540.png" width="500px" alt="切换kernel">

---

#### Q3：在 Notebook 中能够直接看到图片，可是为什么双击图片所在的 Markdown 块后，图片就显示不出来了？

**答：** 这是因为双击图片所在的 Markdown 块后就进入了编辑模式。点击 Markdown 块之外的代码块，回到查看模式后，图片就会重新显示。

<img src="https://img.alicdn.com/imgextra/i4/O1CN012mnKlz1Q5hRev3onD_!!6000000001925-1-tps-1240-372.gif" width="500px" alt="切换kernel">

---

#### Q4：我注意到 Git 仓库有更新，应该怎么拉取到最新代码？

**答：** 你可以在命令行（Terminal）中操作。

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

---

#### Q5：我在执行 `git clone` 命令时，速度很慢，并且报了超时的错误，应该怎么办？

**答：** 你可以停止该实例，在切换到其它地域后，重新创建一个实例并拉取代码。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01BSl0Ku1Hef8xRAm9Q_!!6000000000783-0-tps-958-1112.jpg" width="300px" alt="切换region">

---

#### Q6：我已经在线下课程、DSW、ModelScope 或本地 Notebook 中学完并运行了代码，为什么课程网页里没有显示“已学完”？

**答：** 本课程主要面向线下学习场景。DSW、ModelScope 和本地 IDE 是代码运行环境，不会自动把你的学习和运行记录同步到课程网页。

线上页面是否显示“已学完”不影响认证考试。如果你已经完成学习并准备报名考试，可以直接前往[阿里云大模型ACP认证页面](https://edu.aliyun.com/certification/acp26)报名。

<img src="https://img.alicdn.com/imgextra/i4/O1CN011MrGFo1cHrTc76j1Q_!!6000000003576-2-tps-2678-1280.png" width="900px" alt="阿里云大模型ACP认证报名页面">

---

#### Q7：如果 PAI-DSW 已经产生费用或欠费，应该怎么处理？

**答：** PAI-DSW 是阿里云产品资源，费用和欠费处理以阿里云控制台为准，课程内容无法代为处理账单、退费或欠费恢复。

如果账号已经欠费，相关云资源可能会自动停机，需要按阿里云控制台提示完成付费或充值后才能继续使用。你可以到费用中心查看账单明细，确认费用来自哪个地域、实例规格和运行时段；如对扣费有疑问，请通过阿里云控制台提交工单或联系阿里云客服处理。

为避免继续产生费用，请检查 PAI-DSW 实例列表中是否还有运行中的实例；如果不再使用，请及时停止或删除。后续如果不确定自己是否有免费试用资格，建议改用本地 IDE 或 ModelScope 免费 Notebook 完成课程学习。
