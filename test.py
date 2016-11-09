import gym
import matplotlib.pyplot as plt
import numpy as np

env = gym.make('HumanoidStandup-v1')
a_samples = []
for i in range(100):
    action = env.action_space.sample()
    a_samples.append(action)
mins = np.min(a_samples, 0)
maxes = np.max(a_samples, 0)
print(mins)
print(maxes)

plt.figure(1)
plt.plot(mins)
plt.plot(maxes)

plt.figure(2)
plt.plot(a_samples)
plt.show()



# for i_episode in range(20):
#     observation = env.reset()
#     for t in range(100):
#         env.render()
#         action = env.action_space.sample()
#
#         if t == 0:
#             print(observation.shape)
#             print(observation)
#             print(action.shape)
#
#         observation, reward, done, info = env.step(action)
#         if done:
#             print("Episode finished after {} timesteps".format(t+1))
#             break
