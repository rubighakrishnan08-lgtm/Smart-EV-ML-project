from stable_baselines3 import PPO
from env import EVChargingEnv

env = EVChargingEnv()

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

model.save("ev_agent")

print("RL training complete!")