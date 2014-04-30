from Grid import Grid
from random import Random

GRID_SIZE = 4

class GamePlayer:
	# Constructor
	def __init__(self):
		self.__rand = Random()
	
	# Performs a move on behalf
	# of the computer, inserts
	# a 2 tile into first valid
	# location
	def makeMove(self, grid):
		if (not grid.isFull()):
			done = False

			while(not done):
				i = self.__rand.randint(0, GRID_SIZE-1)
				j = self.__rand.randint(0, GRID_SIZE-1)
				val = self.__rand.randint(1, 2)
				
				done = grid.addTile((val*2), i, j)

		return False

''' Test code
def main():
	grid = Grid()
	gamePlayer = GamePlayer()

	while (True):
		grid.printGrid()

		gamePlayer.makeMove(grid)
		input("NEXT?")
	
if __name__ == "__main__":
	main()
'''
