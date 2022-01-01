'''This class is used to represent the race track as the environment'''
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle
import itertools
from tqdm import tqdm
import random

class Race:
    def __init__(self, file_path, reward=10):
        #reading track file
        with open(file_path,'r') as file:
            track_string = file.readlines()
            
        self.track = self.build_track(track_string)
        self.m, self.n = self.track.shape[0], self.track.shape[1]
        self.reward = reward
    
    def build_track(self, track_string):
        ''' Mapping : 
        0: Start State (S)
        1: Other State (O)
        2: Obstacles State(X)
        3: Finish State(F) 
        '''
        if track_string[-1]=='\n':
            track_string.pop()

        m = len(track_string)

        track_arr = []

        for i in range(m-1,-1,-1):
            temp = []
            for j in range(len(track_string[i])):
                if track_string[i][j]!='\n':
                    if track_string[i][j] =='S':
                        temp.append(0)
                    elif track_string[i][j] =='O':
                        temp.append(1)
                    elif track_string[i][j] == 'X':
                        temp.append(2)
                    elif track_string[i][j] == 'F':
                        temp.append(3)
            track_arr.append(temp)

        track_arr = np.array(track_arr)
        return track_arr
  
    def plot_track(self):
        m,n = self.m,self.n
        colors = ListedColormap(['r','white','k','g'])
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111)
        ax.matshow(self.track[::-1],cmap = colors)
        for i in range(n):
            for j in range(m):
                ax.add_patch( Rectangle((i-0.5, j-0.55),1, 1,
                                        fc ='none', 
                                        ec ='black',
                                        lw = 1) )
        plt.xticks([])
        plt.yticks([])
        plt.grid()
        plt.show()

    def plot_episode(self,episode, end_state):
        temp = self.track.copy()
        m, n = self.m, self.n
        for ep in episode:
            state = ep[0]
            i,j = state
            temp[i,j] = 4

        if (end_state[0] >= (self.m-1)) and (0 <= end_state[1] < self.n):
            temp[self.m-1,end_state[1]] = 4
            
        elif (0<=end_state[0]<self.m) and (0<=end_state[1]<self.n):
            temp[end_state[0], end_state[1]] = 4

        colors = ListedColormap(['r','white','black','g','blue'])
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111)
        ax.matshow(temp[::-1],cmap = colors)
        for i in range(n):
            for j in range(m):
                ax.add_patch( Rectangle((i-0.5, j-0.55),1, 1,
                                        fc ='none', 
                                        ec ='black',
                                        lw = 1) )
        plt.xticks([])
        plt.yticks([])
        plt.grid()
        plt.show()
        
    def update_state(self, state, action):      
        new_state = (state[0] + action[0], state[1] + action[1])
        return new_state

    def is_terminal(self, state):            #
        i = state[0]
        j = state[1]
        if i < 0 or j < 0 or j >= self.n or i >= self.m:     #went out of racetrack
            return True
        if self.track[i,j]==2 or (self.track[i,j]==3):       #hitting an obstacle or reaching goal
            return True
        return False

    def get_reward(self,state, hit_obstacle=False):       
        if hit_obstacle == True:
            return -(self.reward)

        i,j = state[0], state[1]
        if i < 0 or j < 0 or j >= self.n: #went out of racetrack (not from finishing line)
            return -(self.reward)
        
        elif i >= self.m: #went out of racetrack (from finishing line)
            return self.reward
        
        elif self.track[i,j] == 3: #hitting finishing line
            return self.reward
        
        elif self.track[i,j] == 2: #hitting an obstacle
            return -(self.reward)
        
        return -1  #default reward if no action


    def start(self):
        j = np.random.randint(0,self.n)
        return 0,j #start from any place on red line