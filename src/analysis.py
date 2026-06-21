import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "outputs/ppo_results.csv"
)

plt.plot(
    df["Frame"],
    df["Reward"]
)

plt.savefig(
    "outputs/reward_curve.png"
)

print(
    "Graph Generated"
)
