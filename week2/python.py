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

# Ratings (converted approx to 1–5 scale)
CHATGPT_RATINGS = [3.75, 2.4, 3.0, 1.9, 3.0, 3.0, 1.6, 1.75]
CLOUD_AI_RATINGS = [3.75, 3.6, 3.25, 1.9, 3.0, 4.5, 2.0, 1.75]

# Weighted Scores (your actual totals)
CHATGPT_SCORE = round(sum([0.75,0.48,0.6,0.38,0.6,0.6,0.32,0.35]), 2)
CLOUD_AI_SCORE = round(sum([0.75,0.72,0.65,0.38,0.6,0.9,0.4,0.35]), 2)

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

# Scale (1–5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_ylim(0, 5)

# Title
plt.title("Quality Comparison: ChatGPT vs Cloud AI App", size=14)

# Legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Save chart
plt.savefig("radar_chart.png", dpi=300, bbox_inches='tight')

# Show chart
plt.show()