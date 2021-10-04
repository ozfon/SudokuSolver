#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import time

grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
# Properties
row = len(grid)
col = len(grid)

def find_locations(arr):
    #properties
    l = []
    #print(l)
    for r in range(row):
        for c in range(col):
            if (arr[r][c] == 0):
                l.append([r, c])
    return l
        

def check_row(grid, cur_row, cur_col):
    for c in range(col):
        if cur_col != c:
            if grid[cur_row][cur_col] == grid[cur_row][c]:
                good_row = False
                return good_row
    good_row = True
    return good_row

def check_col(grid, cur_row, cur_col):
    for r in range(row):
        if cur_row != r:
            if grid[cur_row][cur_col] == grid[r][cur_col]:
                good_col = False
                return good_col
    good_col = True
    return good_col

def check_block(grid, cur_row, cur_col):
    #find block
    for r in range(row//3):
        for c in range(col//3):
            if cur_row != cur_row//3*3+r and cur_col != cur_col//3*3+c:
                if grid[cur_row][cur_col] == grid [cur_row//3*3+r][cur_col//3*3+c]:
                    good_block = False
                    return good_block
    good_block = True
    return good_block


def check_all(grid, cur_row, cur_col):
    if check_row(grid, cur_row, cur_col) and check_col(grid, cur_row, cur_col) and check_block(grid, cur_row, cur_col):
        all_good = True
    else:
        all_good = False
    return all_good

def print_grid(grid):
    for r in range(row):
        for c in range(col):
            print(grid[r][c], end = ' ' )
        print()

def solver(grid, locations, debug = False):
    counter = 0
    i = 0
    while i < len(locations):
        num = grid[locations[i][0]][locations[i][1]]
        if num < 9:
            grid[locations[i][0]][locations[i][1]] += 1
        
            #check if it fits
            all_good = check_all(grid, locations[i][0], locations[i][1])
        if all_good == False:
            if num > 8:
                grid[locations[i][0]][locations[i][1]] = 0 #reset it
                i -= 1
        if all_good == True:
            i += 1
        if debug:
            time.sleep(0.005) #sleep for 10 milliseconds so the solving can be seen
            print('\n' * 5)
            print_grid(grid)
        counter += 1
    return counter

locations = find_locations(grid)

iterations = solver(grid, locations, debug = True)

print('\n' * 5)
print('Sudoku converged:\n')
print_grid(grid)
print('\niterations = %d' % (iterations))