import gym
from gym import spaces
import numpy as np

class HospitalEnv(gym.Env):

    def __init__(self):
        super(HospitalEnv, self).__init__()

        # State: beds, ICU, patients, severity
        self.observation_space = spaces.Box(
            low=0, high=100, shape=(4,), dtype=np.float32
        )

        # Actions: 0 = Bed, 1 = ICU, 2 = Wait
        self.action_space = spaces.Discrete(3)

        self.reset()

    def reset(self):
        self.beds = 50
        self.icu = 10
        self.patients = np.random.randint(1, 10)
        self.severity = np.random.randint(0, 3)  # 0 low, 2 critical

        return np.array([self.beds, self.icu, self.patients, self.severity])

    def step(self, action):
        reward = 0

        if action == 0 and self.beds > 0:
            self.beds -= 1
            reward += 10

        elif action == 1 and self.icu > 0:
            self.icu -= 1
            reward += 15

            if self.severity == 2:
                reward += 10  # critical patient handled correctly

        else:
            reward -= 10  # penalty

        # New patient arrives
        self.patients = np.random.randint(1, 10)
        self.severity = np.random.randint(0, 3)

        state = np.array([self.beds, self.icu, self.patients, self.severity])
        done = False

        return state, reward, done, {}