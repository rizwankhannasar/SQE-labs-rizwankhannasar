import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# DATA (UPDATED VALUES)
# -----------------------------
categories = [
    "Functional Suitability",
    "Performance Efficiency",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]

# NEW RATINGS (your given values)
CHATGPT_RATINGS = [5, 4.5, 6, 3.5, 4.5, 6, 5, 4]
CLOUD_AI_RATINGS = [5, 6, 6, 3.5, 4.5, 6, 4.5, 4]

# (Optional) Update scores automatically
CHATGPT_SCORE = round(sum(CHATGPT_RATINGS) / len(CHATGPT_RATINGS), 2)
CLOUD_AI_SCORE = round(sum(CLOUD_AI_RATINGS) / len(CLOUD_AI_RATINGS), 2)

# -----------------------------
# RADAR CHART SETUP
# -----------------------------
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

# Close the loop
CHATGPT_RATINGS += CHATGPT_RATINGS[:1]
CLOUD_AI_RATINGS += CLOUD_AI_RATINGS[:1]
angles += angles[:1]

# -----------------------------
# PLOT
# -----------------------------
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Plot ChatGPT
ax.plot(angles, CHATGPT_RATINGS, linewidth=2,
        label=f"ChatGPT (Score: {CHATGPT_SCORE})")
ax.fill(angles, CHATGPT_RATINGS, alpha=0.1)

# Plot Cloud AI App
ax.plot(angles, CLOUD_AI_RATINGS, linewidth=2, linestyle='dashed',
        label=f"Cloud AI App (Score: {CLOUD_AI_SCORE})")
ax.fill(angles, CLOUD_AI_RATINGS, alpha=0.1)

# Labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# ⚠️ IMPORTANT: Your scale now goes up to 6 (not 5)
ax.set_yticks([1, 2, 3, 4, 5, 6])
ax.set_ylim(0, 6)

# Title
plt.title("Quality Comparison: ChatGPT vs Cloud AI App", size=14)

# Legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Save chart
plt.savefig("radar_chart.png", dpi=300, bbox_inches='tight')

# Show chart
plt.show()