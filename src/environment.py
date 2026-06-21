import gymnasium as gym
import numpy as np
from gymnasium import spaces


class TrafficEnv(gym.Env):

    def __init__(self, frame_range=(0, 100)):

        super().__init__()

        self.frame_start, self.frame_end = frame_range
        self.current_frame = self.frame_start

        self.num_lanes = 4

        self.action_space = spaces.Discrete(2)

        self.observation_space = spaces.Box(
            low=0,
            high=100,
            shape=(self.num_lanes,),
            dtype=np.float32
        )

        self.state = np.zeros(
            self.num_lanes,
            dtype=np.float32
        )

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.current_frame = self.frame_start

        self.state = np.random.randint(
            5,
            50,
            size=self.num_lanes
        ).astype(np.float32)

        return self.state, {}

    def step(self, action):

        self.current_frame += 1

        reward = -float(
            np.sum(self.state)
        )

        terminated = (
            self.current_frame
            >= self.frame_end
        )

        return (
            self.state,
            reward,
            terminated,
            False,
            {}
        )
