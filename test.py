import gym
import matplotlib.pyplot as plt
import numpy as np

env = gym.make('HumanoidStandup-v1')
for i_episode in range(1):
    observation = env.reset()
    for t in range(1000):
        env.render()
        action = env.action_space.sample()

        observation, reward, done, info = env.step(action)

        if t == 0:
            print(observation.shape)
            print(action.shape)
        print(reward)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
