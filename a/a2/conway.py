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
                            continue
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
        # Split the pattern into lines and strip whitespace
        lines = [line.strip() for line in txtString.split("\n")]
            # Skip comment lines (starting with '!'), empty lines, and lines that are just whitespace
            # Also ensure lines only contain valid characters ('.' and 'O')
        valid_lines = []
        for line in lines:
            if not line or line.startswith('!'):
                continue
            # Check if the line contains only valid characters
            if all(char in '.O' for char in line):
                valid_lines.append(line)
            else:
                print(f"Warning: Skipping invalid line in pattern file: '{line}'")

        if not valid_lines:
            print("Error: No valid pattern lines found in the file.")
            return  # No valid lines left to process

        # Determine the dimensions
        height = len(valid_lines)
        width = max(len(line) for line in valid_lines)

        # Normalize lines by padding shorter ones with dead cells ('.')
        normalized_lines = []
        for line in valid_lines:
            if len(line) < width:
                line = line + '.' * (width - len(line))  # Pad with dead cells
            normalized_lines.append(line)

        # Adjust pad for tuple input
        if isinstance(pad, tuple):
            pad_y, pad_x = pad
        else:
            pad_y, pad_x = pad, pad

        # Insert the pattern into the grid
        for i in range(height):
            for j in range(width):
                char = normalized_lines[i][j]
                if char == 'O':
                    self.grid[i + pad, j + pad] = self.aliveValue
                elif char == '.':
                    self.grid[i + pad, j + pad] = self.deadValue
                else:
                    # This should never happen with the validation above, but keep as a fallback
                    self.grid[i + pad, j + pad] = self.deadValue

        return height, width

    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''
        # Parse the RLE string using RunLengthEncodedParser
        parser = rle.RunLengthEncodedParser(rleString)

        # pattern dimensions and data
        pattern = parser.pattern_2d_array
        height = parser.size_y
        width = parser.size_x

        # Convert the pattern to the required format ('.' and 'O')
        # The parser gives 'b' for dead and 'o' for live; we need '.' and 'O'
        normalized_lines = []
        for row in pattern:
            line = ''.join('.' if cell == 'b' else 'O' for cell in row)
            normalized_lines.append(line)

        # Tile the pattern to make it at least 512x512
        # min_size = 512
        # if height < min_size or width < min_size:
        #     tile_x = max(1, (min_size + width - 1) // width)  # Ceiling division
        #     tile_y = max(1, (min_size + height - 1) // height)
        #     tiled_height = height * tile_y
        #     tiled_width = width * tile_x
        #     tiled_lines = []

        #     for row in range(tile_y):
        #         for i in range(height):
        #             # Repeat each line `tile_x` times in the x direction
        #             line = ''.join(normalized_lines[i] for _ in range(tile_x))
        #             tiled_lines.append(line)

        #     normalized_lines = tiled_lines
        #     height = tiled_height
        #     width = tiled_width

        # Adjust pad for tuple input (if pad is a tuple, e.g., (pad_y, pad_x))
        if isinstance(pad, tuple):
            pad_y, pad_x = pad
        else:
            pad_y, pad_x = pad, pad

        #  Insert the pattern into the grid
        for i in range(height):
            for j in range(width):
                if i + pad_y < self.N and j + pad_x < self.N:  # Ensure we don't go out of bounds
                    char = normalized_lines[i][j]
                    if char == 'O':
                        self.grid[i + pad_y, j + pad_x] = self.aliveValue
                    elif char == '.':
                        self.grid[i + pad_y, j + pad_x] = self.deadValue

        return height, width
