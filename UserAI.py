import sys
import copy
from GridNode import GridNode
from Grid import Grid

BIG_NUMBER = sys.maxint

class UserAI:
	# Internal helper function to facilitate
	# for the recursive construction of the
	# game search space tree
	def __generateGameTreeHelper__(self, userTurn, gridNode, maxDepth, curDepth):
		# If max depth is reached, then
		# break
		if (curDepth == maxDepth):
			return 
              	
		curGrid = gridNode.getGrid()
                
		if (userTurn):
			# Adds all possible user moves
			userLeftMove = copy.deepcopy(curGrid)
		        userRightMove = copy.deepcopy(curGrid)
                        userUpMove = copy.deepcopy(curGrid)
                        userDownMove = copy.deepcopy(curGrid)

			resultLeft = userLeftMove.tilt("left")
			resultRight = userRightMove.tilt("right")
			resultUp = userUpMove.tilt("up")
			resultDown = userDownMove.tilt("down")
			
			if (resultLeft[0] == True):
				gridNode.addChildGrid(userLeftMove,
						gridNode.getScore() + resultLeft[1])

			if (resultRight[0] == True):
                        	gridNode.addChildGrid(userRightMove,
						gridNode.getScore() + resultRight[1])
                        
			if (resultUp[0] == True):
                        	gridNode.addChildGrid(userUpMove,
						gridNode.getScore() + resultUp[1])
                        
			if (resultDown[0] == True):
                        	gridNode.addChildGrid(userDownMove,
						gridNode.getScore() + resultDown[1])

                else:
			# Adds all permutation of 2, 4 tiles at
			# all valid positions of the grid
                        for val in range(1, 3):
                                for i in range(curGrid.getGridSize()):
                                        for j in range(curGrid.getGridSize()):
                                                gameMove = copy.deepcopy(curGrid)

                                                if (gameMove.addTile(val*2, i, j) == True):
                                                        gridNode.addChildGrid(gameMove,
									gridNode.getScore())

		# Recursive calls the helper function on all
		# generated child nodes
		for nodes in range(gridNode.getNumOfChildNodes()):
			self.__generateGameTreeHelper__((not userTurn),
					gridNode.getChildNodeAt(nodes),
					maxDepth, curDepth+1)

	# Given a grid state and depth, this function
	# generates your game search tree
	def generateGameTree(self, grid, depth):
		gridNode = GridNode(grid)

		if (depth % 2 == 0):
			return gridNode
		
		self.__generateGameTreeHelper__(True, gridNode, depth, 0)

		return gridNode

	def __miniMaxTraversalHelper__(self, gridNode, depth, maximizingPlayer):
		if ((depth == 0) or
			(gridNode.getNumOfChildNodes() == 0)):
			return gridNode.getScore()
		
		if (maximizingPlayer == True):
			bestValue = -1 * BIG_NUMBER - 1
			
			for i in range(gridNode.getNumOfChildNodes()):
				val = self.__miniMaxTraversalHelper__(gridNode.getChildNodeAt(i),
							depth-1,
							False)

				if (val > bestValue):
					bestValue = val
			
			return bestValue
		elif (maximizingPlayer == False):
			bestValue = BIG_NUMBER

			for i in range(gridNode.getNumOfChildNodes()):
				val = self.__miniMaxTraversalHelper__(gridNode.getChildNodeAt(i),
							depth-1,
							True)

				if (val < bestValue):
					bestValue = val
			
			return bestValue

	def miniMaxTraversal(self, gridNode, depth):
		return self.__miniMaxTraversalHelper__(gridNode, depth, False)

	def decisionMaker(self, grid):
		gridNode = self.generateGameTree(grid, 5)
	
		bestValue = -1 * BIG_NUMBER - 1

		for i in range(gridNode.getNumOfChildNodes()):
			hu_val = self.miniMaxTraversal(gridNode.getChildNodeAt(i), 3)
			
			if (hu_val > bestValue):
				grid.setGrid(((gridNode.getChildNodeAt(i)).getGrid()).getGrid())
				print "Making following move:"
				grid.printGrid()
				bestValue = hu_val

def traversalHelper(gridNode, depth):
	print "GridNode, depth = " + str(depth)
	gridNode.getGrid().printGrid()
	print "score = " + str(gridNode.getScore())

	for i in range(gridNode.getNumOfChildNodes()):
		traversalHelper(gridNode.getChildNodeAt(i), depth+1)

def main():
	userAI = UserAI()
	grid = Grid()

	grid.addTile(2, 0, 0)
	grid.addTile(2, 1, 0)
	grid.addTile(4, 3, 0)

	print "About to generateGameTree"
	gridNode = userAI.generateGameTree(grid, 5)

	'''traversalHelper(gridNode, 0)'''

	print "num of childnodes = " + str(gridNode.getNumOfChildNodes())

	for i in range(gridNode.getNumOfChildNodes()):
		hu_val = userAI.miniMaxTraversal(gridNode.getChildNodeAt(i), 3)

		print "Heuristic value for child " + str(i) + " is " + str(hu_val)
	
if __name__ == "__main__":
	main()
