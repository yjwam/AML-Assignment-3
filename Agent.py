'''This class is used to represent the car as an agent for Q-L algorithm'''
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle
import itertools
from tqdm import tqdm
import random

class Car:
    def __init__(self, epsilon = 0.2):
        #Building the agent(car) with parameters epsilon, the action space possible and initial velocity
        self.epsilon = epsilon
        self.actions = self.actions()
        self.velocity = (0,0)

    def actions(self):
        ''' Possible operations:
        1:decrease velocity by one
        0: keep velocity unchanged
        1: increase velocity by 1'''
        possible_actions = [-1, 0, 1] 
        return (list(itertools.product(possible_actions, possible_actions)))
    
    def initialize(self, states, track):
        '''Initialize q(s,a) arbitrarily (from normal distribution)
        for each state and action except the target state which has q(s,a) = 0'''
        self.q = {}
    
        for state in states:
            for action in self.actions:
                if (not track.is_terminal(state)):
                    self.q[(state,action)] = np.random.normal(-1,1)
                else:
                    self.q[(state,action)] = 0                 
  
    def get_action(self,state, learn = True):
        '''learn parameter is used to control if the action sampled should be with respect to if the agent is learning or if it is learnt.
        If agent is learning policy is an epsilon greedy policy. Else, we take the greedy approach of chosing action with max(q(s,a)).
        '''
        if learn == True:
            temp = -1
            prob_sample = np.random.uniform(0,1)
            
            if prob_sample <= self.epsilon:     #to explore
                while True:
                    action = random.choice(self.actions)
                    if self.is_valid_action(action):
                        new_action = action
                        break

            else:           #to exploit
                temp = -999 
                best_actions = []
                for action in self.actions:
                    x = (state, action)

                    if (self.q[x] > temp) and (self.is_valid_action(action)):
                        best_actions = []
                        temp = self.q[x]
                        best_actions.append(action)
                    elif (self.q[x] == temp) and (self.is_valid_action(action)):
                        temp = self.q[x]
                        best_actions.append(action)

                if len(best_actions)>1:
                  #t = np.random.randint(0, len(best_actions))
                  #a = best_actions[t]
                    new_action = random.choice(best_actions)
                else:
                    new_action = best_actions[0]

        else:       #sample action based on learnt agent
            temp = -999 
            best_actions = []
            for action in self.actions:
                x = (state, action)

                if (self.q[x] > temp) and (self.is_valid_action(action)):
                    best_actions = []
                    temp = self.q[x]
                    best_actions.append(action)
                elif (self.q[x] == temp) and (self.is_valid_action(action)):
              #t = self.policy[x]
                    best_actions.append(action)

            if len(best_actions)>1:
            #t = np.random.randint(0, len(best_actions))
            #a = best_actions[t]
                new_action = random.choice(best_actions)
            else:
                new_action = best_actions[0]
        return new_action

    def is_valid_action(self, action):
        v_x = self.velocity[0] + action[0]
        v_y = self.velocity[1] + action[1]
        if (v_x == 0 and v_y == 0):   #velocity cannot be zero except at start position
            return False
        if (np.abs(v_x) < 5) and (np.abs(v_y) < 5):   #absolute value of each velocity component must be less than 5
            return True
        
        return False

    def update_velocity(self, action):
        v_x = self.velocity[0] + action[0]
        v_y = self.velocity[1] + action[1]
        self.velocity = (v_x, v_y)

    def reset(self):
        self.velocity = (0,0)

    def get_best_action(self, state):
        temp = -999
        best_actions = []
        for action in self.actions:
            x = (state,action)
            if self.q[x] > temp:
                best_actions = []
                temp = self.q[x]
                best_actions.append(action)
            elif self.q[x] == temp:
                best_actions.append(action)
        if len(best_actions) > 1:  #if multiple maximas.
            best_action = random.choice(best_actions)
        else:
            best_action = best_actions[0]
        return best_action