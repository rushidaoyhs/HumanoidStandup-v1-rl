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

\pi(s, a) is a now a Gaussian Distribution. 

Previously it was Exp(linear) parametric form. Now it is a Exp(quadratic) form. It will give a better approximation than Bolzman machine. Interesting.  

What about \sigma?

What about 1D? The action variable is only 1D and continuous. It is still advantageous than Bolzman in terms of approximation power, and continuous action. 


