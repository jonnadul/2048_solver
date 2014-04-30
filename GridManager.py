import copy
from Grid import Grid
from GamePlayer import GamePlayer
from UserPlayer import UserPlayer

class GridManager:
	# Constructor
	def __init__(self):
		self.__grid = Grid()
		self.__gamePlayer = GamePlayer()
		self.__userPlayer = UserPlayer()

	# Start Game
	def startGame(self):
		# Will continue toggling between
		# Game and User turns until the
		# Grid is Full (which is a loss)
		# or a 2048 tile is encountered
		# (which is a win)
		while ((not self.__grid.isFull()) and
			(not self.__grid.gridContains(2048))):
			self.__gamePlayer.makeMove(self.__grid)

			self.__grid.printGrid()

			validMove = False
			while(not validMove):
				validMove = not (self.__userPlayer.makeMove(self.__grid))

		if (self.__grid.isFull()):
			print "User Lost!"
		elif (self.__grid.gridContains(2048)):
			print "User Won!"

def main():
	gridManager = GridManager()

	gridManager.startGame()

if __name__ == "__main__":
	main()
