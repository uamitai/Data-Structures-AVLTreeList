#username - complete info
#id1      - 325541878 
#name1    - Amitai Wolf 
#id2      - complete info
#name2    - complete info  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node

	@type is_real: bool
	@param is_real: is node real or virtual
	"""
	def __init__(self, value, is_real=True):
		self.parent = None
		self.is_real = is_real

		if is_real:
			self.value = value
			self.left = AVLNode(None, False)
			self.right = self.left
			self.height = 0
			self.size = 1
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left if self.left.isRealNode() else None


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right if self.right.isRealNode() else None

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value if self.isRealNode() else None

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height if self.isRealNode() else -1
	
	"""returns the size

	@rtype: int
	@returns: the size of self, 0 if the node is virtual
	"""
	def getSize(self):
		return self.size if self.isRealNode() else 0

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		if self.isRealNode():
			if node == None:
				self.left = AVLNode(None, False)
			else:
				self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		if self.isRealNode():
			if node == None:
				self.right = AVLNode(None, False)
			else:
				self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		if self.isRealNode():
			self.value = value

	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		if self.isRealNode():
			self.height = h
	
	"""sets size factor of the node

	@type s: int
	@param s: the size
	"""
	def setSize(self, s):
		if self.isRealNode():
			self.size = s

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return self.is_real
	
	"""updates height with respect to children
	
	"""
	def updateHeight(self):
		self.height = max(self.left.getHeight(), self.right.getHeight()) + 1
	
	"""updates size with respect to children
	
	"""
	def updateSize(self):
		self.size = self.left.getSize() + self.right.getSize() + 1
	
	"""returns the balance factor of self
	
	@rtype: int
	@returns: balance factor
	"""
	def balanceFactor(self):
		return self.left.getHeight() - self.right.getHeight()



"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.first = None
		self.last = None


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return self.length() == 0


	"""does rotations to balance the AVL tree
	
	@type node: AVLNode
	@param node: node to start fixing up from
	@pre: node is in the tree
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing 
	"""
	def balance(self, node):
		return 0


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		return self.select(i + 1).getValue() #TODO self.select


	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		z = AVLNode(val)

		"insert in an empty tree"
		if self.empty():
			self.root = z
			self.first = z
			self.last = z
			return 0

		if i == self.length():

			"find the maximum and make z its right child"
			self.last().setRight(z)
			z.setParent(self.last)
			self.last = z
		
		else:

			"find the node of rank i+1"
			node = self.rank(i + 1) #TODO self.rank
			if node.getLeft() == None:

				"if it has no left child make z its left child"
				node.setLeft(z)
				z.setParent(node)
				if i == 0:
					self.first = z
		
			else:

				"find its predecessor and make z its right child"
				node = self.predecessor(node) #TODO self.predecessor
				node.setRight(z)
				z.setParent(node)

		#TODO fix the tree
		return self.balance(z)


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1
	

	"""deletes a node from the tree
	
	@type node: AVLNode
	@param node: node to be deleted
	@pre: node has at most one child
	"""
	def deleteNode(self, node):
		parent = node.getparent()
		if node.getLeft() == None:

			"node has no left child"
			if node is parent.getLeft():
				parent.setLeft(node.getRight())
			elif node is parent.getRight():
				parent.setRight(node.getRight())
		
		elif node.getRight() == None:

			"node has no right child"
			if node is parent.getLeft():
				parent.setLeft(node.getLeft())
			elif node is parent.getRight():
				parent.setRight(node.getLeft())


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.first


	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.last


	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		array = []
		node = self.first()

		while True:
			"append value to array"
			array.append(node.getValue())

			"exit if node is last in list"
			if node is self.last():
				break

			"go to successor node"
			node = self.successor(node) #TODO self.successor
		
		return array


	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.root.getSize() if self.root != None else 0


	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		return None


	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None


	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		i = 0
		node = self.first()

		while True:
			"compare node's value to val"
			if node.getValue().equals(val):
				return i
			
			"exit if node is last in list"
			if node is self.last():
				break

			"go to successor node"
			i += 1
			node = self.successor(node) #TODO self.successor
			
		return -1


	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return None if self.empty() else self.root
	

	"""returns the rank of a node in the tree
	
	@type node: AVLNode
	@pre: node is inside the tree
	@param node: node to find rank of
	@rtype: int
	@returns: rank of node
	"""
	def rank(self, node):
		r = node.left.getSize() + 1
		y = node

		while y != None:
			if y is y.getparent().getRight():
				r += y.getParent().left.getSize() + 1
			y = y.getParent()
			
		return r
	

	"""returns the i-th node of the tree's in-order list
	
	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: rank to search for
	@rtype: AVLNode
	@returns: node with rank i
	"""
	def select(self, i):
		return None
	

	"""returns the successor of a given node
	
	@type node: AVLNode
	@pre: node is inside the tree
	@param node: node to start searching from
	@rtype: AVLNode
	@returns: successor of node
	"""
	def successor(self, node):
		if node.getRight() != None:
			y = node.getRight()
			while y.getLeft() != None:
				y = y.getLeft()
			return y
		
		x = node
		y = node.getParent()
		while y != None and x is y.getRight():
			x = y
			y = x.getParent()
		return y


	"""returns the predecessor of a given node
	
	@type node: AVLNode
	@pre: node is inside the tree
	@param node: node to start searching from
	@rtype: AVLNode
	@returns: predecessor of node
	"""
	def predecessor(self, node):
		if node.getLeft() != None:
			y = node.getLeft()
			while y.getRight() != None:
				y = y.getRight()
			return y
		
		x = node
		y = node.getParent()
		while y != None and x is y.getLeft():
			x = y
			y = x.getParent()
		return y