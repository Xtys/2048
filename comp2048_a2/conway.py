# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
from matplotlib.figure import figaspect
import numpy as np
from scipy import signal
import rle


class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.int64)
        self.neighborhood = np.ones((3,3), np.int64) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        self.N = N

    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid

    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()

    def evolve(self, fastMode=False):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''
        #get weighted sum of neighbors
        #PART A & E CODE HERE
        N = self.grid.shape[0]
        new_grid = np.zeros_like(self.grid)

        for y in range(N):
            for x in range(N):
                live_neighbors = 0
                for dy in [-1, 0, 1]:  # Vertical up (-1), same (0), down (1)
                    for dx in [-1, 0, 1]:  # Horizontal left (-1), same (0), right (1)
                        if dy == 0 and dx == 0:
                            continue  # center of 3x3 region
                        # Compute neighbor coordinates
                        ny, nx = y + dy, x + dx
                        # Handle boundaries based on self.finite
                        if self.finite:
                            if 0 <= ny < N and 0 <= nx < N:
                                live_neighbors += self.grid[ny, nx]
                        else:
                            # wrap around using modulo
                            ny = ny % N
                            nx = nx % N
                            live_neighbors += self.grid[ny, nx]

                #implement the GoL rules by thresholding the weights
                #PART A CODE HERE
                if self.grid[y, x] == self.aliveValue:
                    if live_neighbors < 2:          # Underpopulation
                        new_grid[y, x] = self.deadValue
                    elif live_neighbors in [2, 3]:  # Survival
                        new_grid[y, x] = self.aliveValue
                    else:                           # Overpopulation
                        new_grid[y, x] = self.deadValue
                else:   # Dead cell
                    if live_neighbors == 3:         # Reproduction
                        new_grid[y, x] = self.aliveValue

        #update the grid
        self.grid = new_grid

    def evolve_two(self, fastMode=True):
        '''
        Evolve the current generation to the next using the rules of game of life
        '''
        # kernel
        kernel = np.ones((3, 3), dtype=np.int64)
        kernel[1, 1] = 0  # Exclude the center cell

        # Compute weights (number of live neighbors) using convolution
        weights = signal.convolve2d(self.grid, kernel, mode='same', boundary='wrap')

        # Apply GoL rules using vectorized operations
        newGrid = np.zeros_like(self.grid)
        newGrid[(self.grid == self.aliveValue) & (weights == 2)] = self.aliveValue
        newGrid[(self.grid == self.aliveValue) & (weights == 3)] = self.aliveValue
        newGrid[(self.grid == self.deadValue) & (weights == 3)] = self.aliveValue

        self.grid = newGrid

    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue

    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue

    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+25] = self.aliveValue

        self.grid[index[0]+2, index[1]+23] = self.aliveValue
        self.grid[index[0]+2, index[1]+25] = self.aliveValue

        self.grid[index[0]+3, index[1]+13] = self.aliveValue
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+21] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+35] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue

        self.grid[index[0]+4, index[1]+12] = self.aliveValue
        self.grid[index[0]+4, index[1]+16] = self.aliveValue
        self.grid[index[0]+4, index[1]+21] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+35] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue

        self.grid[index[0]+5, index[1]+1] = self.aliveValue
        self.grid[index[0]+5, index[1]+2] = self.aliveValue
        self.grid[index[0]+5, index[1]+11] = self.aliveValue
        self.grid[index[0]+5, index[1]+17] = self.aliveValue
        self.grid[index[0]+5, index[1]+21] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue

        self.grid[index[0]+6, index[1]+1] = self.aliveValue
        self.grid[index[0]+6, index[1]+2] = self.aliveValue
        self.grid[index[0]+6, index[1]+11] = self.aliveValue
        self.grid[index[0]+6, index[1]+15] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue
        # Part c, fixed column 18 should be ALIVE
        self.grid[index[0]+6, index[1]+18] = self.aliveValue
        self.grid[index[0]+6, index[1]+23] = self.aliveValue
        self.grid[index[0]+6, index[1]+25] = self.aliveValue

        self.grid[index[0]+7, index[1]+11] = self.aliveValue
        self.grid[index[0]+7, index[1]+17] = self.aliveValue
        self.grid[index[0]+7, index[1]+25] = self.aliveValue

        self.grid[index[0]+8, index[1]+12] = self.aliveValue
        self.grid[index[0]+8, index[1]+16] = self.aliveValue

        self.grid[index[0]+9, index[1]+13] = self.aliveValue
        self.grid[index[0]+9, index[1]+14] = self.aliveValue

    def insertFromPlainText(self, txtString, pad=0):
        '''
        Assumes txtString contains the entire pattern as a human readable pattern without comments
        '''
        # Split the pattern string into lines
        lines = txtString.split('\n')
        # Remove comment lines (starting with '!') and empty lines
        rows = [line for line in lines if line and not line.startswith('!')]
        if not rows:
            return  # No valid rows

        # Determine the dimensions of the pattern
        height = len(rows)
        width = len(rows[0])

        # Insert the pattern into the grid
        for i in range(height):
            for j in range(width):
                if pad + i < self.N and pad + j < self.N:
                    self.grid[pad + i, pad + j] = self.aliveValue if rows[i][j] == 'O' else self.deadValue


    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''
