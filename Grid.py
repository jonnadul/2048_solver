from collections import deque
import copy

GRID_SIZE = 4

class Grid:
	# Constructor
	def __init__(self):
		self.__grid = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
		self.__numItems = 0

	# Adds a new tile at
	# row i, col j
	def addTile(self, tileValue, i, j):
		if (((i >= 0) and (i < GRID_SIZE)) and
			((j >= 0) and (j < GRID_SIZE))):
			self.__grid[i][j] = tileValue
			return True 
		else:
			return False

	# Returns the private grid variable
	def getGrid(self):
		return self.__grid

	# Sets the private grid variable
	def setGrid(self, grid):
		self.__grid = copy.deepcopy(grid)
	
	# Checks if the grid is full
	def isFull(self, grid):
		for i in range(GRID_SIZE):
			for j in range(GRID_SIZE):
				if (self.__grid[i][j] == 0):
					return False
		return True

	# Returns a copy of the Grid Class in the
	# indicated tilt direction
	def tilt(self, direction):
		retGridClass = copy.deepcopy(self)
		retGrid = retGridClass.getGrid()

		if (direction == "up"):
			i_inc = -1
			i_start = 0
			i_stop = GRID_SIZE
			i_step = 1
			
			j_inc = 0
			j_start = 0
			j_stop = GRID_SIZE
			j_step = 1
		elif (direction == "right"):
			i_inc = 0
			i_start = 0
			i_stop = GRID_SIZE
			i_step = 1
			
			j_inc = 1
			j_start = GRID_SIZE-1
			j_stop = -1
			j_step = -1
		elif (direction == "down"):
			i_inc = 1
			i_start = GRID_SIZE-1
			i_stop = -1
			i_step = -1
			
			j_inc = 0
			j_start = 0
			j_stop = GRID_SIZE
			j_step = 1
		elif (direction == "left"):
			i_inc = 0
			i_start = 0
			i_stop = GRID_SIZE
			i_step = 1
			
			j_inc = -1
			j_start = 0
			j_stop = GRID_SIZE
			j_step = 1
		else:
			return False
		
		for i in range(i_start, i_stop, i_step):
			for j in range(j_start, j_stop, j_step):
				if retGrid[i][j] != 0:
					curr_i = i
					curr_j = j

					next_i = i + i_inc
					next_j = j + j_inc

					done = False
					while ((not done) and
						((next_i >= 0) and (next_i < GRID_SIZE)) and
						((next_j >= 0) and (next_j < GRID_SIZE))):
						if (retGrid[next_i][next_j] == 0):
							retGrid[next_i][next_j] = retGrid[curr_i][curr_j]
							retGrid[curr_i][curr_j] = 0

						elif (retGrid[next_i][next_j] ==
							retGrid[curr_i][curr_j]):
							retGrid[next_i][next_j] = (retGrid[curr_i][curr_j] * 2)
							retGrid[curr_i][curr_j] = 0

						else:
							done = True
					
						if (not done):
							curr_i += i_inc
							curr_j += j_inc

							next_i = curr_i + i_inc
							next_j = curr_j + j_inc
		
		retGridClass.setGrid(retGrid)
		return retGridClass

	# Prints Grid
	def printGrid(self):
		printStr = ""
		for i in range(GRID_SIZE):
			for j in range(GRID_SIZE):
				printStr += str(self.__grid[i][j]) + " "
			print printStr
			printStr = ""
		print ""

'''Test code
def main():
	grid = Grid()

	grid.addTile(4, 1, 0)
	grid.addTile(4, 3, 0)
	grid.addTile(4, 1, 2)
	grid.addTile(4, 3, 2)

	grid.printGrid()

	grid = grid.tilt("up")

	grid.printGrid()

	grid = grid.tilt("down")

	grid.printGrid()

	grid = grid.tilt("left")

	grid.printGrid()

	grid = grid.tilt("right")

	grid.printGrid()
	
	grid = grid.tilt("down")

	grid.printGrid()
	
	grid.addTile(4, 1, 0)
	grid.addTile(4, 3, 0)
	grid.addTile(4, 1, 2)
	grid.addTile(4, 3, 2)
	
	grid.printGrid()
	
	grid = grid.tilt("left")

	grid.printGrid()

	grid = grid.tilt("right")

	grid.printGrid()
	

if __name__ == "__main__":
	main()
'''
