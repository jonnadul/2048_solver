from Grid import Grid

GRID_SIZE = 4

class UserPlayer:
	# Performs a move on behalf
	# of the user, currently
	# prompts for a tile direction
	# and performs it.
	def makeMove(self, grid):
		direction = input("up, down, left, right?: ")
		return grid.tilt(direction)

''' Test Code
def main():
	grid = Grid()
	userPlayer = UserPlayer()

	grid.addTile(4, 1, 0)
	grid.addTile(4, 3, 0)
	grid.addTile(4, 1, 2)
	grid.addTile(4, 3, 2)

	while(True):
		grid.printGrid()

		userPlayer.makeMove(grid)

if __name__ == "__main__":
	main()
'''
