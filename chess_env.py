# chess_env.py

import gym
import gym_chess

def make_chess_env():
    env = gym.make("Chess-v0")
    return env
