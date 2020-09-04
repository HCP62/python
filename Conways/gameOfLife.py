#Conway's game of life
# Rules:
# 1. Any living cell with less than 2 neighbors dies, as if by underpopulation.
# 2. Any living cell with 2 or 3 neighbors lives on to the next generation.
# 3. Any living cell with more than 3 neighbors will die, as if by overpopulation.
#4. Any dead cell with exactly 3 neighbors will become alive, as if by reproduction.

import time
import copy


#grid
def initGrid():
    grid = []
    for i in range(30):
        row = []
        for i in range(60):
            row.append(False)
        grid.append(row)
    return grid


#displays grid with either a tilde or an O on each element depending on whether it is a living or dead cell
def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == False):
                print("~", end = "")
            else:
                print("O", end = "")
        print("")

def initCells(filename, grid): #initializes all cells to the board and sets dead cells to False, and living cells to True
    f = open(filename)
    data = f.readlines()
    f.close()
    coords = []
    for i in range(len(data)):
        coords.append(data[i].split())
    #print(coords)
    for point in coords:
        grid[int(point[0])][int(point[1])] = True
    
    printGrid(grid)
    print("\n")


#initCells("spaceship.txt")

def isValid(a, b, r, c, grid): #finds out whether one of the surrounding elements is a valid neighbor
    #return (0 <= r and r <= len(grid) and 0 <= c and c <= len(grid[0]) and (a != r or b != c) and grid[r][c] == True)
    # print(len(grid))
    # print(len(grid[0]))
    # print(r, " ", c)
    if (0 > r or r >= len(grid)):
        return False
    elif(0 > c or c >= len(grid[0])):
        return False
    elif (a == r and b == c):
        return False
    return grid[r][c]

def getNeighbors(a, b, grid): #returns all the neighbors of any living cell
    neighbors = 0
    for r in range(a-1, a+2):
        for c in range(b-1, b+2):
            if (isValid(a,b,r,c, grid) == True):
                neighbors+=1
    return neighbors
# Rules:
# 1. Any living cell with less than 2 neighbors dies, as if by underpopulation.
# 2. Any living cell with 2 or 3 neighbors lives on to the next generation.
# 3. Any living cell with more than 3 neighbors will die, as if by overpopulation.
#4. Any dead cell with exactly 3 neighbors will become alive, as if by reproduction.

def livingConditions(grid): #checks board for whether or not there are X number of neighbors to dictate whether the cell in question lives or dies
    newGrid = initGrid()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if ((getNeighbors(i,j, grid) == 2 or getNeighbors(i,j, grid) == 3) and grid[i][j] == True): #checks to see if there are 2 or 3 neighbors to keep it alive
                newGrid[i][j] = True
            elif(getNeighbors(i,j, grid) == 3 and grid[i][j] == False):
                newGrid[i][j] = True
            else: #checks to see if there is <2 or >3 neighbors to then kill off the cell in question
                newGrid[i][j] = False
    grid = copy.deepcopy(newGrid)
    printGrid(grid)
    return grid

def displayRules(): #displays rules with a 3 second gap before running the board
    print("1. Any living cell with less than 2 neighbors dies, as if by underpopulation.\n2. Any living cell with 2 or 3 neighbors lives on to the next generation.\n3. Any living cell with more than 3 neighbors will die, as if by overpopulation.\n4. Any dead cell with exactly 3 neighbors will become alive, as if by reproduction.")

def runGame():
    displayRules()
    time.sleep(5)
    grid = initGrid()
    initCells("spaceship.txt", grid)
    time.sleep(1)
    while True:
        grid = livingConditions(grid)
        print("\n")
        time.sleep(1)

runGame()