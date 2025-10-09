# 1.0 Getting started with LLMs

## 🚄 Preface

Hands-on practice is an essential part of learning about large language models (LLMs). To help you better grasp the relevant knowledge, this course includes a variety of example code.

We recommend that you use [Data Science Workshop (DSW)](https://help.aliyun.com/zh/pai/user-guide/dsw-overview) on Alibaba Cloud's Artificial Intelligence Platform (PAI) to complete your coursework. With PAI DSW, you can run code while reading the course documentation to better understand and apply LLMs.
## Getting Started

### I. Create an Alibaba Cloud account

Please follow the instructions below based on your region:

- **International users**: [Alibaba Cloud International Site](https://www.alibabacloud.com)  
  > If you are an international user, make sure to complete your identity verification and set up your payment method before getting started. Please note that the international site does not offer a free trial, so a valid payment method is required for service usage.

- **Chinese mainland users**: [Aliyun Official Website](https://www.aliyun.com)  
  > If you are a new user of **PAI DSW (Data Science Workshop)**, you can apply for a **free trial quota** through Aliyun's Free Trial program.  
  > After claiming the free trial, you will receive **250 free compute hours per month** of CPU/GPU instances for three months. This is approximately:
  > - **430 hours/month** of usage for an `ecs.g6.xlarge` CPU instance, or  
  > - **35 hours/month** of usage for an `ecs.gn7i-c8g1.2xlarge` GPU instance

### II. Activate PAI and configure your workspace

1. After logging into the [Alibaba Cloud Console](https://home.console.aliyun.com/), search for **Platform for AI (PAI)** in the product list and open the PAI console.
2. If this is your first time using PAI, click **Activate PAI with One Click** and create a default workspace.  
   > ✅ **Recommendation**: Use your primary account for activation to avoid permission issues.
   <img src="https://img.alicdn.com/imgextra/i1/O1CN01XF6LJC1Fwri7TjrGX_!!6000000000552-2-tps-1784-1194.png" width="800px">
3. Once activated, click **Go to Default Workspace**.

### III. Create a PAI DSW Instance

1. In the left sidebar of the PAI console, navigate to **Data Science Workshop** and click **Create Instance**.
    <img src="https://img.alicdn.com/imgextra/i4/O1CN01c5Dehb271bQtHfaPG_!!6000000007737-2-tps-2186-1596.png" width="800px">
2. Fill in the following information:

   - **Instance Name**: e.g., `alibabacloud_acp_learning`
   - **Resource Specifications**: Choose a suitable ECS specification based on your needs. Since there is no free trial, ensure that your account has sufficient balance or a linked credit card.
     > For most course exercises, a CPU-based instance like `ecs.g6.xlarge` is sufficient. You can switch to GPU instances when necessary for specific chapters.

     <img src="https://img.alicdn.com/imgextra/i3/O1CN01pZ8CwZ1PGrXEujG79_!!6000000001814-2-tps-3436-1716.png" width="800px">
   - **Image**: Select a CPU-type image with Python 3.10 support. For example:
     ```
     modelscope:1.23.1-pytorch2.3.1-cpu-py310-ubuntu22.04
     ```

     <img src="https://img.alicdn.com/imgextra/i1/O1CN01QAzZ721ZsYHlNLk9p_!!6000000003250-2-tps-2954-1716.png" width="800px">

3. Leave other settings as default and click **OK** to create the instance. The creation process typically takes up to 5 minutes.
4. Once the instance status shows as **Running**, click **Open** in the **Actions** column to access the online Notebook interface provided by DSW.

> ⚠️ **Important Note**: Charges will apply based on the runtime of the instance. Be sure to stop the instance when not in use to avoid unnecessary costs.
>
> 🔒 **How to Avoid Charges After Free Trial**
> 
> The free trial quota automatically covers DSW instance costs. However, once the quota is exhausted or expires, you must manually stop or delete the instance to prevent pay-as-you-go charges.
> 
> **Stop**: Halts billing for compute resources (CPU/GPU) while preserving storage.
> 
> **Delete**: Fully releases all resources and stops all billing (including potential storage fees).



### IV. Environment setup and course code download

In DSW, you can access the command line environment by clicking Terminal at the top.

Verify the environment variables by entering `python --version` in the Terminal to confirm that the current Python version is 3.10, and enter `pwd` to confirm that the current directory is <mark>/mnt/workspace</mark>.  



```bash
python --version
pwd
```

<img src="https://img.alicdn.com/imgextra/i2/O1CN016v7knf295qKb1IKYO_!!6000000008017-2-tps-1736-378.png" width="600px">

If you are not in the **/mnt/workspace** directory, enter the following command to ensure smooth installation afterward:  



```bash
cd /mnt/workspace
```

You can set up your environment and download course files using either **automatic** or **manual** installation.

#### 1. Automatic Installation
Execute the following command in the DSW Terminal to download a script that automatically installs the environment dependencies required for the course.



```bash
wget https://developer-labfileapp.oss-cn-hangzhou.aliyuncs.com/ACP/LLM/en/alibabacloud_llm_acp_install.sh
bash aliyun_llm_acp_install.sh
```


<img src="https://img.alicdn.com/imgextra/i1/O1CN01iWqgMe1fMqZeWM32D_!!6000000003993-2-tps-2520-554.png" width="800px">

If this step executes successfully, you can skip the following manual installation steps.
#### 2. Manual Installation

##### 2.1 Download Course Code

Enter the following command in the `Terminal` to obtain the code for the ACP course:  



```bash
git clone https://github.com/AlibabaCloudDocs/aliyun_acp_learning.git
```

If you encounter network issues, you can also obtain it from atomgit: `git clone https://atomgit.com/alibabaclouddocs/aliyun_acp_learning.git`

If you are familiar with Jupyter Notebook and wish to run it locally, we recommend using a Python 3.10 environment.

##### 2.2 Manually install dependencies

Continue running the following commands sequentially in the `Terminal` to install the required dependencies for this course:



```shell
# Create a Python virtual environment named llm_learn using the venv module
python3 -m venv llm_learn

# Activate the llm_learn virtual environment
source llm_learn/bin/activate

# Upgrade pip within the virtual environment
pip install --upgrade pip

# Install the ipykernel kernel management tool
pip install ipykernel

# Add llm_learn to ipykernel
python -m ipykernel install --user --name llm_learn --display-name "Python (llm_learn)"

# Install code execution dependencies in the llm_learn environment
pip install -r ./aliyun_acp_learning/requirements.txt

# Exit the llm_learn virtual environment
deactivate
```

#### 3. Switch Python Environment

After completing the installation steps, switch to Notebook at the top, and you will be able to see the aliyun_acp_learning folder in the file tree.

<img src="https://img.alicdn.com/imgextra/i2/O1CN01w80bRU287qSTne6de_!!6000000007886-2-tps-1654-574.png" width="600px">

Next, you can sequentially navigate to the **LLM_ACP_EN -> p2_Build LLM Q&A System** folder in the file tree to access the content of the next chapter's tutorial.

<img src="https://img.alicdn.com/imgextra/i4/O1CN01M456CR1ooAkJrk8tV_!!6000000005271-2-tps-884-1478.png" width="320px">

After the course content installation is complete, you also need to **select the kernel** (default kernel: Python 3 (ipykernel)) in the upper right corner of the Notebook course (.ipynb file) and switch to the Python environment you just created, such as the `Python(llm_learn)` environment created above.<br>
<img src="https://img.alicdn.com/imgextra/i1/O1CN01WXabpz1yRPDS3Br0q_!!6000000006575-2-tps-3808-1360.png" width="800px"><br>
<img src="https://img.alicdn.com/imgextra/i4/O1CN01qRgpMM1MsvbedxeAb_!!6000000001491-2-tps-838-572.png" width="320px"><br>
<img src="https://img.alicdn.com/imgextra/i3/O1CN01cOQpCw1rN6AZmHtfN_!!6000000005618-2-tps-848-356.png" width="320px"><br>

> Typically, you need to manually specify the Python environment for each course material. There are many versions of Python, and the component versions used in different projects vary. The venv virtual environment used in this course can create an independent Python environment for each project, avoiding version conflicts and simplifying dependency management.

Once you have successfully completed the steps above, you can start learning the course. Wishing you a smooth journey ahead in your studies!<br>  


## Further reading

To facilitate reading, you can open the Table of Contents for the current document via the left menu:

<img src="https://img.alicdn.com/imgextra/i3/O1CN01kRbOpl1nh0wMz29TB_!!6000000005120-2-tps-1818-1690.png" width="600px">

If you don't like the dark theme, you can adjust it in the Settings menu at the top:

<img src="https://img.alicdn.com/imgextra/i1/O1CN01Pn587w1sILgnJpHE3_!!6000000005743-2-tps-1842-1640.png" width="600px">

### Common issues with DSW

**Q1: Why are the input box positions for WebIDE and Notebook different in DSW?**

**A1:** In Tutorial 2.1, you will input an API Key. The location of the input box varies by interface:

- **Notebook**: The input box appears directly below the code block, making it easy to find.

<img src="https://img.alicdn.com/imgextra/i3/O1CN01xIZrMU1OBXJWJc4Tu_!!6000000001667-2-tps-1874-294.png" width="800px">

- **WebIDE**: The input box appears directly above the code file.

<img src="https://img.alicdn.com/imgextra/i2/O1CN012Q75ea1MQX3AG4D93_!!6000000001429-2-tps-1858-540.png" width="800px">

**Q2: In Notebook, I can see the images, but why do they disappear when I double-click the Markdown block containing them?**

**A2:** This is because double-clicking a Markdown block enters **edit mode**. In this mode, images are not rendered. Simply click outside the Markdown block (for example, into a code cell) to return to **view mode**, and the image will reappear.

**Q3: I noticed that the Git repository has been updated. How do I pull the latest code?**

**A3:** You can run the following two commands sequentially in the Terminal:

```shell
git checkout .
git pull
```

⚠️ Note: This will overwrite any local changes. If you need to preserve local runtime results or modified files, make sure to back them up before proceeding.

**Q4: When I execute the `git clone` command, it's very slow and reports a timeout error. What should I do?**

**A4:** Stop the current instance, switch to a different region, then create a new instance to pull the code.

<img src="https://img.alicdn.com/imgextra/i3/O1CN01U0MWdZ1qP6HjtBbCW_!!6000000005487-2-tps-1674-1076.png" width="800px">

This often resolves network latency or connectivity issues, especially when accessing repositories from regions with restricted or slow external access.
