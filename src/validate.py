from stable_baselines3 import PPO
from src.environment import TrafficEnv


env = TrafficEnv()

model = PPO.load(
    "models/ppo_train_model"
)

obs, _ = env.reset()

while True:

    action, _ = model.predict(
        obs
    )

    obs, reward, done, _, _ = (
        env.step(action)
    )

    if done:
        break

print(
    "Validation Finished"
)
