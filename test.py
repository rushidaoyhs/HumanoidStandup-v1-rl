import gym
import sys

print(sys.executable)


env = gym.make('HumanoidStandup-v1')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()

        if t == 0:
            print(observation.shape)
            print(observation)
            print(action.shape)

        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
