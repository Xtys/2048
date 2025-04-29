# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
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

    def evolve(self):
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
                # Count live neighbors (8 surrounding cells: up, down, left, right, diagonals)
                live_neighbors = 0
                for dy in [-1, 0, 1]:  # Vertical offsets: up (-1), same (0), down (1)
                    for dx in [-1, 0, 1]:  # Horizontal offsets: left (-1), same (0), right (1)
                        if dy == 0 and dx == 0:
                            continue  # Skip the cell itself (center of 3x3 region)
                        # Compute neighbor coordinates
                        ny, nx = y + dy, x + dx
                        # Handle boundaries based on self.finite
                        if self.finite:
                            # Finite boundaries: only count neighbors within grid
                            if 0 <= ny < N and 0 <= nx < N:
                                live_neighbors += self.grid[ny, nx]
                        else:
                            # Periodic boundaries: wrap around using modulo
                            ny = ny % N
                            nx = nx % N
                            live_neighbors += self.grid[ny, nx]

                #implement the GoL rules by thresholding the weights
                #PART A CODE HERE
                # Apply GoL rules
                if self.grid[y, x] == self.aliveValue:
                    if live_neighbors < 2:  # Underpopulation
                        new_grid[y, x] = self.deadValue
                    elif live_neighbors in [2, 3]:  # Survival
                        new_grid[y, x] = self.aliveValue
                    else:  # Overpopulation
                        new_grid[y, x] = self.deadValue
                else:  # Dead cell
                    if live_neighbors == 3:  # Reproduction
                        new_grid[y, x] = self.aliveValue

        #update the grid
        self.grid = new_grid

    def evolve_fast(self):
        '''
        Evolve the current generation to the next using the rules of game of life
        '''
        # Define the kernel for counting neighbors (3x3 with center 0)
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
        # Split the string into rows
        rows = txtString.strip().split('\n')
        if not rows:
            return  # Empty string, nothing to insert

        # Filter out comment lines (starting with # or !)
            pattern_rows = [row for row in rows if not row.startswith(('#', '!'))]
            if not pattern_rows:
                return  # No valid pattern rows after removing comments

        # Determine pattern dimensions
        num_rows = len(rows)
        num_cols = max(len(row) for row in rows)  # Longest row determines width

        # Grid dimensions
        N = self.grid.shape[0]  # Assuming square grid (N x N)

        # Insert pattern into grid starting at (pad, pad)
        for i in range(num_rows):
            row = rows[i]
            for j in range(len(row)):
                # Calculate grid position with padding
                grid_y = pad + i
                grid_x = pad + j

                # Skip if position is outside grid bounds
                if grid_y >= N or grid_x >= N:
                    continue

                # Map character to cell state
                char = row[j]
                if char in ('O', '*'):
                    self.grid[grid_y, grid_x] = self.aliveValue
                elif char in ('.', ' '):
                    self.grid[grid_y, grid_x] = self.deadValue


    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''
