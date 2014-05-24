import copy
import math
import copy

class Grid:
	# Constructor
	def __init__(self):
		self.__gridSize = 4
		self.__grid = [[0 for i in range(self.__gridSize)] for j in range(self.__gridSize)]

	# Adds a new tile at
	# row i, col j
	def addTile(self, tileValue, i, j):
        	if (((i >= 0) and (i < self.__gridSize)) and
			((j >= 0) and (j < self.__gridSize)) and
			(self.__grid[i][j] == 0)):
			self.__grid[i][j] = tileValue
			return True 
		else:
			return False

	def clearGrid(self):
		self.__grid = [[0 for i in range(self.__gridSize)] for j in range(self.__gridSize)]

	# Sets the grid
	def setGrid(self, grid):
		for i in range(self.__gridSize):
			for j in range(self.__gridSize):
				self.__grid[i][j] = grid[i][j]

	# Returns the private grid variable
	def getGrid(self):
		return self.__grid

	# Returns number of open spaces
	def numOfTilesOf(self, number):
		count = 0
		for i in range(self.__gridSize):
			for j in range(self.__gridSize):
				if (self.__grid[i][j] == number):
					count += 1

		return count

	def getHeuristic(self):
		total = 0
		for i in range(self.__gridSize):
			for j in range(self.__gridSize):
				total += self.__grid[i][j]
		
		return total

	# Returns the private gridSize variable
	def getGridSize(self):
		return self.__gridSize

	# Sets the private grid variable
	def setGrid(self, grid):
		self.__grid = copy.copy(grid)

	# Checks if a certain value is in
	# the grid
	def gridContains(self, value):
		for i in range(self.__gridSize):
			for j in range(self.__gridSize):
				if (self.__grid[i][j] == value):
					return True

		return False

	# Checks if the grid is full
	def isFull(self):
		for i in range(self.__gridSize):
			for j in range(self.__gridSize):
				if (self.__grid[i][j] == 0):
					return False
		return True

	# Returns a copy of the Grid Class in the
	# indicated tilt direction
	def tilt(self, direction):
		# Assume no movements and score is
		# zero at beginning
		movement = False
		score = 0

		if (direction == "up"):
			i_inc = -1
			i_start = 0
			i_stop = self.__gridSize
			i_step = 1
			
			j_inc = 0
			j_start = 0
			j_stop = self.__gridSize
			j_step = 1
		elif (direction == "right"):
			i_inc = 0
			i_start = 0
			i_stop = self.__gridSize
			i_step = 1
			
			j_inc = 1
			j_start = self.__gridSize-1
			j_stop = -1
			j_step = -1
		elif (direction == "down"):
			i_inc = 1
			i_start = self.__gridSize-1
			i_stop = -1
			i_step = -1
			
			j_inc = 0
			j_start = 0
			j_stop = self.__gridSize
			j_step = 1
		elif (direction == "left"):
			i_inc = 0
			i_start = 0
			i_stop = self.__gridSize
			i_step = 1
			
			j_inc = -1
			j_start = 0
			j_stop = self.__gridSize
			j_step = 1
		else:	
			return (movement, score)

		for i in range(i_start, i_stop, i_step):
			for j in range(j_start, j_stop, j_step):
				if (self.__grid[i][j] != 0):
					curr_i = i
					curr_j = j

					next_i = i + i_inc
					next_j = j + j_inc

					done = False
					while ((not done) and
						((next_i >= 0) and (next_i < self.__gridSize)) and
						((next_j >= 0) and (next_j < self.__gridSize))):

						if (self.__grid[next_i][next_j] == 0):
							self.__grid[next_i][next_j] = self.__grid[curr_i][curr_j]
							self.__grid[curr_i][curr_j] = 0
							movement = True

						elif (self.__grid[next_i][next_j] ==
								self.__grid[curr_i][curr_j]):
							# Makes it negative so that it tile
							# combinations don't skip turns
							self.__grid[next_i][next_j] = (self.__grid[curr_i][curr_j] * -2)
							self.__grid[curr_i][curr_j] = 0
							done = True
							movement = True
							score += (-1 * self.__grid[next_i][next_j])
						else:
							self.setGrid(self.__grid)
							done = True
					
						if (not done):
							curr_i += i_inc
							curr_j += j_inc

							next_i = curr_i + i_inc
							next_j = curr_j + j_inc

		# Reverting all negatives
		for i in range(self.__gridSize):
			for j in range(self.__gridSize):
				if (self.__grid[i][j] < 0):
					self.__grid[i][j] = self.__grid[i][j] * -1

		return (movement, score)

	# Prints Grid
	def printGrid(self):
		printStr = ""
		for i in range(self.__gridSize):
			for j in range(self.__gridSize):
				printStr += str(self.__grid[i][j]) + "\t"
			print printStr
			printStr = ""
		print ""

	def printGridThis(self, grid):
		printStr = ""
		for i in range(self.__gridSize):
			for j in range(self.__gridSize):
				printStr += str(grid[i][j]) + "\t"
			print printStr
			printStr = ""
		print ""

def main():
	grid = Grid()

	grid.addTile(2, 0, 0)
	grid.addTile(2, 1, 0)
	grid.addTile(4, 3, 0)

	grid.printGrid()

	valud = grid.tilt("up")
	
	if (valud[0] == True):
		print "score = " + str(valud[1])
	
	grid.printGrid()

	valud = grid.tilt("up")
	
	if (valud[0] == True):
		print "score = " + str(valud[1])
	
	grid.printGrid()

if __name__ == "__main__":
	main()
