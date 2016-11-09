# HumanoidStandup-v1-rl
RL algorithm for HumanoidStandup-v1 (openai-gym)

## Setups:

* set up python. I used python 2.7.12 Anaconda custum 64-bit
* set up the openai gym 
* set up pycharm ide (optional)
* install [mojoco](https://github.com/openai/mujoco-py)

## About this environment:

* An action is a 17-dimensional vector. So the robot has 17 DOF. 
* An obsevation is 376-dimensional vector. They probably contains positions, speed, acceleration, angular velocities in the joins. It is not interesting to look into these, although Mujoco has some papers (such as [this one](http://homes.cs.washington.edu/~todorov/papers/TassaIROS12.pdf)) to track. It is more interesting to develop an algorithm without knowing what these states are. 

## Range of the action values:

```
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
```
It shows all the actions are "continuous" and are between [-0.4, 0.4].

