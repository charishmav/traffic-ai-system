from stable_baselines3 import PPO
from src.environment import TrafficEnv


env = TrafficEnv()

model = PPO(
    "MlpPolicy",
    env,
    verbose=1
)

model.learn(
    total_timesteps=50000
)

model.save(
    "models/ppo_train_model"
)

print(
    "Training Complete"
)
