import copy
from GridNode import GridNode
from Grid import Grid

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

			if (userLeftMove.tilt("left") == True):
				gridNode.addChildGrid(userLeftMove)

			if (userRightMove.tilt("right") == True):
                        	gridNode.addChildGrid(userRightMove)
                        
			if (userUpMove.tilt("up") == True):
                        	gridNode.addChildGrid(userUpMove)
                        
			if (userDownMove.tilt("down") == True):
                        	gridNode.addChildGrid(userDownMove)

                else:
			# Adds all permutation of 2, 4 tiles at
			# all valid positions of the grid
                        for val in range(1, 3):
                                for i in range(curGrid.getGridSize()):
                                        for j in range(curGrid.getGridSize()):
                                                gameMove = copy.deepcopy(curGrid)

                                                if (gameMove.addTile(val*2, i, j) == True):
                                                        gridNode.addChildGrid(gameMove)

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

def traversalHelper(gridNode, depth):
	print "GridNode, depth = " + str(depth)
	gridNode.getGrid().printGrid()

	for i in range(gridNode.getNumOfChildNodes()):
		traversalHelper(gridNode.getChildNodeAt(i), depth+1)

def main():
	userAI = UserAI()
	grid = Grid()

	grid.addTile(2, 0, 0)
	grid.addTile(2, 1, 0)
	grid.addTile(4, 3, 0)

	gridNode = userAI.generateGameTree(grid, 5)

	traversalHelper(gridNode, 0)

if __name__ == "__main__":
	main()
