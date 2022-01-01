# AML-Assignment-3
[Link](https://www.cmi.ac.in/~madhavan/courses/aml2021/assignment3/)
## Content

## By- Yash Jain (MDS202048), Yash Raj (MDS202049)
### 1. Race.py
This class is used to represent the race track.
- **Attributes**
  - build_track : take string input and creates a track based on mapping\
  Start State (S) = 0\
  Other State (O) = 1\
  Obstacles State(X) = 2\
  Finish State(F) = 3
  
  - plot_track : to plot track as in assignment.
  - plot_episode : to plot an episode of the car.
  - update_state : to get the new state of the car based on it's past state and action chosen.
  - is_terminal : to check if a given state is a terminal state\
  True if either car went out of track or hit obstacles or reached finish line.
  - get_reward : to get reward for current state as per rules set in assingment.
  - start : to choose a starting point for the car.
 
 ### 2. Car.py
This class is used to represent the car.
 - **Attributes**
    - actions : to build possible actions of the agent based on the problem statement.\
  -1 : decrease velocity by one\
  0 : keep velocity unchanged\
  1 : increase velocity by one
    - initialize : initialize  q(s,a) arbitrarily (from normal distribution) for each state and action except the target state which has q(s,a) = 0, where s is state and a is action.
    - get_action : to get the possible actions for a given state.
    - is_valid_action :  to check if action chosen is a valid action with respect to constraints.
    - update_velocity : to update velocity of car.
    - reset : to reset the car velocity to (0,0).
    - get_best_action : to chose greedily the action for a given state.
    
### 3. track-1.txt
This is text file which represent track-1 (as given in assignment)
### 4. track-2.txt
This is text file which represent track-2 (as given in assignment)
### 5. track-own.txt
This is text file which represent our own track.
### 6. Reinforcement_Learning.ipynb
Uses [Q-Learning](https://en.wikipedia.org/wiki/Q-learning) algorithm, where agent is a car and environment is a track.
