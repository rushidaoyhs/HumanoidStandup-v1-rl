# HumanoidStandup-v1-rl
RL algorithm for HumanoidStandup-v1 (openai-gym)

## Setups:

* set up python. I used python 2.7.12 Anaconda custum 64-bit
* set up the openai gym 
* set up pycharm ide (optional). Make sure you use the right python interpreter.
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
It shows all the actions are "continuous" and are all between [-0.4, 0.4].

## Goal

Note the environment gives a reward. How is this reward calculated (curious)?
Looking at zdx3578's [solution](https://gym.openai.com/evaluations/eval_w6uskkQOTxG3G0o3pT8q6w). This reward function helps. It increases when the robot stands up. 

## Actor-Critic
The actor critic algorithm uses Bolzman machine, and only works for discrete action space. 


## A new algorithm
For multi-dimensional continuous action space, I believe you can do some Gaussian algorithms. For example, maintain a distribution function $\pi(s, a)$ in such a way that the mean and variance depend on (s, a). 

If some (s, a) has a large reward, adjust the parameters so that similar state action pairs will have a large reward. 

$mu(s)$ is a distribution function. Given a state s, generate a vector mu(s). It has same dimention with action variables. In this case, 17.   

$sigma(s)$ is a covariance matrix. Give a state s, generate a matrix sigma(s), 17 by 17 in this case.   

then this method will adjust parameters theta and v. 

* mu is converging to the optimal control. 
* sigma should decrease to zero as learning becomes optimal. 
* the algorithm is novel in that it allows large exploration in the beginning, and decrease exploration gradually as it becomes more confident. 


[Multi-variatiate Gaussian](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)

The x is a, mu and Sigma depends on s. So we should still learn for the parameters to be used with the features of s. 

\pi(s, a) is a now a the CDF of Gaussian Distribution. 

why do you need the Critic? Aha. in the policy gradient of J, there is a Q. so you need the Critic. 

this ideas has been explored by [Hado](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.75.7658&rep=rep1&type=pdf)
The mean is updated and the Sigman is hand set. This algorithm doesn't look good. If the TD error is positive, then basically update the action parameter to favor this action. It should be done in a policy gradient way. 

[book chapter](http://oai.cwi.nl/oai/asset/19689/19689B.pdf)

[more papers](https://scholar.google.com/scholar?client=ubuntu&channel=fs&oe=utf-8&um=1&ie=UTF-8&lr&cites=6846849656859318086)

not a lot. you can always publish. the point is good paper. good algorithm. 

[simple algorithm](http://papers.nips.cc/paper/3318-reinforcement-learning-in-continuous-action-spaces-through-sequential-monte-carlo-methods.pdf)

If seeing a large reward at state (s, a), similar states to s should take similar action to a. 

How about taking multiple actions at a single state? Trying out many possible actions. This is possible with a simulation model. 
