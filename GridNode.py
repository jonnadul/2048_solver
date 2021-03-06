from Grid import Grid

class GridNode:
	# Constructor
	def __init__(self, grid, score=0):
		self.__grid = grid
		self.__score = score
		self.__childNodes = []

	# Returns grid state
	def getGrid(self):
		return self.__grid

	# Returns grid score
	def getScore(self):
		return self.__score

	# Adds a new child grid node
	def addChildGridNode(self, gridNode):
		self.__childNodes.append(gridNode)
	
	# Adds a new child grid node
	def addChildGrid(self, grid, score=0):
		self.__childNodes.append(GridNode(grid, score))

	# Returns number of child nodes
	def getNumOfChildNodes(self):
		return len(self.__childNodes)

	# Returns child node at index
	def getChildNodeAt(self, idx):
		return self.__childNodes[idx]
''' Test Code
def main():
	grid1 = Grid()
	grid2 = Grid()
	grid3 = Grid()
	
	grid1.addTile(2, 0, 0)
	grid1.addTile(2, 1, 0)
	grid1.addTile(4, 3, 0)
	
	grid2.addTile(2, 0, 0)
	grid2.addTile(2, 1, 1)
	grid2.addTile(4, 3, 3)
	
	grid3.addTile(8, 0, 0)
		
	GridNode1 = GridNode(grid1, 0)
	GridNode2 = GridNode(grid2, 1)
	GridNode3 = GridNode(grid3, 2)

	GridNode1.addChildGridNode(GridNode2)
	GridNode1.addChildGridNode(GridNode3)
	GridNode1.addChildGrid(grid2, 1)
	GridNode1.addChildGrid(grid3, 2)

	print "Parent Grid: "
	GridNode1.getGrid().printGrid()
	print "Grid Score = " + str(GridNode1.getScore())

	for i in range(GridNode1.getNumOfChildNodes()):
		print "Grid state at: " + str(i)
		GridNode1.getChildNodeAt(i).getGrid().printGrid()
		print "Grid Score = " + str(GridNode1.getChildNodeAt(i).getScore())

if __name__ == "__main__":
	main()
'''
