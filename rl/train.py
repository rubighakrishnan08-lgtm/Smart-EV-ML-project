from stable_baselines3 import PPO
import gymnasium as gym
import numpy as np

# Custom Environment
class EVEnv(gym.Env):
    def __init__(self):
        super(EVEnv, self).__init__()

        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Box(
            low=0, high=100, shape=(3,), dtype=np.float32
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        return np.array([50, 50, 50], dtype=np.float32), {}

    def step(self, action):
        reward = np.random.random()
        done = np.random.choice([True, False])

        obs = np.random.randint(0, 100, size=(3,), dtype=np.int32)

        return obs, reward, done, False, {}  # (obs, reward, terminated, truncated, info)


# Create environment
env = EVEnv()

# Train model
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

# Save model
model.save("ev_agent")

print("✅ Model trained and saved as ev_agent.zip")