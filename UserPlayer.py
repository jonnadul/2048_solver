from Grid import Grid

class UserPlayer:
	def __init__(self):
		self.userAI = UserAI()
		self.score = 0
	
	# Performs a move on behalf
	# of the user, currently
	# prompts for a tile direction
	# and performs it.
	def makeMove(self, grid):
		'''direction = raw_input("up, down, left, right?: ")

		result = grid.tilt(direction)

		if (result[0] == True):
			self.score += result[1]
			print "Current score = " + str(self.score)

		return result[0]'''
		
		userAI.decisionMaker(grid)

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
