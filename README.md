# AML-Assignment-3
## Content
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
  - initialize : Initialize  q(s,a) arbitrarily for each state and action except the target state which has q(s,a) = 0, where s is state and a is action.
  - get_action : to get the possible actions for a given state.
  - is_valid_action :  to check if action chosen is a valid action with respect to constraints.
  - update_velocity : to update velocity of car.
  - reset : to reset the car velocity to (0,0).
  - get_best_action : to chose greedily the action for a given state.
  - 
