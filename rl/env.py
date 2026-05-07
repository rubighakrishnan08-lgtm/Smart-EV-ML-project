import gymnasium as gym
from gymnasium import spaces
import numpy as np

class EVChargingEnv(gym.Env):
    def __init__(self):
        super().__init__()

        # State: [new_priority, lowest_priority, load, is_emergency]
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)

        # Action: 0 = reject, 1 = replace
        self.action_space = spaces.Discrete(2)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = np.random.rand(4).astype(np.float32)
        return self.state, {}

    def step(self, action):
        new_p, low_p, load, emergency = self.state

        reward = 0

        # Good replacement only if new > old and load safe
        if action == 1:
            if new_p > low_p:
                reward += 5
            else:
                reward -= 5
        else:
            if new_p < low_p:
                reward += 3
            else:
                reward -= 3

        done = False
        truncated = False

        self.state = np.random.rand(4).astype(np.float32)

        return self.state, reward, done, truncated, {}