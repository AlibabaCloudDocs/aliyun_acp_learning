import numpy as np
from matplotlib import pyplot as plt

# Define a user input prompt and possible next words
prompt = "在大模型ACP课程中，你可以学习"
next_words = ["RAG(token1)", "提示词(token2)", "模型(token3)", "写作(token4)", "画画(token5)"]
probabilities = [0.5, 0.24, 0.12, 0.09, 0.05]

# Calculate cumulative probabilities to illustrate top-p sampling
cumulative_probabilities = np.cumsum(probabilities)

# Define plot titles based on temperature scenario
titles = ["top_p=0.5", "top_p=0.9"]
top_p_thresholds = [0.5, 0.9]

plt.rcParams['font.family'] = 'Alibaba PuHuiTi'
fig, axs = plt.subplots(1, 2, figsize=(25, 6), sharey=True)

for i, ax in enumerate(axs):
    top_p_threshold = top_p_thresholds[i]

    # Identify which words fall under top-p threshold
    selected_indices = np.where(cumulative_probabilities <= top_p_threshold)[0]
    selected_words = np.array(next_words)[selected_indices]
    selected_probs = np.array(probabilities)[selected_indices]

    # Plot the general probability distribution first
    rects1 = ax.bar(next_words, probabilities, color='lightgrey', edgecolor='black', alpha=0.6, label='未选择的token')

    # Highlight the words chosen under the top-p threshold
    rects2 = ax.bar(selected_words, selected_probs, color='skyblue', edgecolor='black', alpha=0.9, label='已选择的token')

    # Adding labels to the bars
    ax.bar_label(rects1, padding=5)
    ax.bar_label(rects2, padding=5)

    ax.set_title(titles[i], fontsize=14)
    ax.set_xlabel("候选token", fontsize=12, labelpad=13)  # Increase the padding for xlabel
    ax.set_ylabel("概率", fontsize=12)
    ax.set_ylim(0, 1)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.legend()

fig.suptitle("参数top_p对候选token采样范围的影响", fontsize=16)
plt.show()
