from matplotlib import pyplot as plt

# Define a user input prompt and possible next words
prompt = "在大模型ACP课程中，你可以学习"
next_words = ["RAG(token1)", "提示词(token2)", "模型(token3)", "写作(token4)", "画画(token5)"]

# Adjusted probabilities based on temperature settings
probabilities_low_temp = [0.8, 0.1, 0.05, 0.03, 0.02]  # Low temperature: concentrated choice on "jumps"
probabilities_medium_temp = [0.6, 0.2, 0.1, 0.06,
                             0.04]  # Medium temperature: balanced choices among "jumps", "leaps", "hops"
probabilities_high_temp = [0.3, 0.25, 0.2, 0.15, 0.1]  # High temperature: more diverse choices, including "runs" and "dances"

# Set up the figure and subplots
plt.rcParams['font.family'] = 'Alibaba PuHuiTi'
fig, axs = plt.subplots(1, 3, figsize=(25, 6), sharey=True)

# Define plot titles based on temperature scenario
titles = [
    "低温度：temperature=0.1",
    "中温度：temperature=0.7",
    "高温度：temperature=1.2"
]
distributions = [probabilities_low_temp, probabilities_medium_temp, probabilities_high_temp]

# Plot each temperature distribution
for i, ax in enumerate(axs):
    bars = ax.bar(next_words, distributions[i], color='skyblue', edgecolor='black')
    ax.set_title(titles[i], fontsize=14)
    ax.set_xlabel("候选token", fontsize=12, labelpad=20)  # Increase the padding for xlabel
    ax.set_ylabel("概率", fontsize=12)  # Increase the padding for ylabel
    ax.set_ylim(0, 1)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.tick_params(axis='x', rotation=0)  # Ensure x-axis labels are horizontal

    # Add text annotations on top of each bar with some vertical offset
    for bar, prob in zip(bars, distributions[i]):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.01, f'{prob:.2f}', ha='center', va='bottom')

# Add an overall title to explain
fig.suptitle(f"参数temperature对候选token概率分布的影响", fontsize=16)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for rotated labels
plt.show()



