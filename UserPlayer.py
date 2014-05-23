from Grid import Grid
from UserAI import UserAI

class UserPlayer:
	def __init__(self):
		self.userAI = UserAI()
	
	# Performs a move on behalf
	# of the user, currently
	# prompts for a tile direction
	# and performs it.
	def makeMove(self, grid):
		self.userAI.decisionMaker(grid)

		# AI takes cares of avoiding illegal
		# moves
		return True
			
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
