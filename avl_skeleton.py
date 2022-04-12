#username - complete info
#id1      - 325541878 
#name1    - Amitai Wolf 
#id2      - 214208704
#name2    - Eivi Katz



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.parent = None

		if value != None:
			self.left = AVLNode(None)
			self.right = AVLNode(None)
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
		if node == None:
			self.left = AVLNode(None)
		else:
			self.left = node
		self.updateHeight()
		self.updateSize()

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		if node == None:
			self.right = AVLNode(None)
		else:
			self.right = node
		self.updateHeight()
		self.updateSize()

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
		return self.value != None
	
	"""updates height with respect to children
	
	"""
	def updateHeight(self):
		self.setHeight(max(self.left.getHeight(), self.right.getHeight()) + 1)
	
	"""updates size with respect to children
	
	"""
	def updateSize(self):
		self.setSize(self.left.getSize() + self.right.getSize() + 1)
	
	"""returns the balance factor of self
	
	@rtype: int
	@returns: balance factor
	"""
	def balanceFactor(self):
		return self.left.getHeight() - self.right.getHeight()
	
	"""returns if the balance factor is good
	
	@rtype: bool
	@returns: is the BF equal to -1, 0 or 1
	"""
	def isBalanced(self):
		return self.balanceFactor() in [-1, 0, 1]



"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = AVLNode(None)
		self.first = None
		self.last = None


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return not self.root.isRealNode()


	"""does rotations to balance the AVL tree
	
	@type node: AVLNode
	@param node: node to start fixing up from
	@pre: node is in the tree
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing 
	"""
	def balance(self, node):
		while node is not None:
			node.updateSize()
			node.updateHeight()
			node = node.getParent()
		return -1


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		return self.select(i + 1).getValue() #TODO self.select()


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
			if i != 0:
				return 0
			self.root = z
			self.first = z
			self.last = z
			return 0

		if i == self.length():

			"find the maximum and make z its right child"
			self.last.setRight(z)
			z.setParent(self.last)
			self.last = z
		
		else:

			"find the node of rank i+1"
			node = self.select(i + 1) #TODO self.select()
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
		node = self.select(i+1)
		parent = node.getParent()

		if (self.length() == 1 and i == 0) or self.empty():
			self.root = AVLNode(None)
			return 0
		
		if node.getLeft() == None:
			if node is self.first:
				self.first = self.successor(node)
			if parent != None:
				if node is parent.getLeft():
					parent.setLeft(node.right)
				elif node is parent.getRight():
					parent.setRight(node.right)
			else:
				self.root = node.right
			node.right.setParent(parent)
			del(node.left)
		
		elif node.getRight() == None:
			if node is self.last:
				self.last = self.predecessor(node)
			if parent != None:
				if node is parent.getLeft():
					parent.setLeft(node.left)
				elif node is parent.getRight():
					parent.setRight(node.left)
			else:
				self.root = node.left
			node.left.setParent(parent)
			del(node.right)
		
		else:
			succ = self.successor(node)
			self.delete(self.rank(succ)-1)
			succ.setLeft(node.left)
			succ.setRight(node.right)
			node.left.setParent(succ)
			node.right.setParent(succ)
			succ.setParent(parent)
			if parent != None:
				if node is parent.getLeft():
					parent.setLeft(succ)
				elif node is parent.getRight():
					parent.setRight(succ)
			else:
				self.root = succ
		
		return self.balance(parent)


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return None if self.empty() else self.first.getValue()


	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return None if self.empty() else self.last


	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		if self.empty():
			return []
			
		array = []
		node = self.first

		while True:
			"append value to array"
			array.append(node.getValue())

			"exit if node is last in list"
			if node is self.last:
				break

			"go to successor node"
			node = self.successor(node) #TODO self.sucessor
		
		return array


	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.root.getSize() if not self.empty() else 0


	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		node = self.select(i + 1) #TODO self.select()
		left = node.getLeft()
		right = node.getRight()

		parent = node
		root = self.getRoot()
		while parent is not root:
			node = parent
			parent = node.getParent()
			if node is parent.getLeft():
				pass # Do some join operations


	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):

		"delete the last node of self to use for join operation"
		x = self.getLast()
		root = self.getRoot()
		self.delete(x) #TODO self.delete()
		
		dif = abs(self.root.getSize() - lst.root.getSize())
		self.join(x, lst)
		self.last = lst.last

		#TODO balance tree
		return dif
	
	"""join operation on self and pther AVL tree

	@type x: AVLNode
	@param x: node to join the trees with
	@type other: AVLTreeList
	@param other: tree to join with
	"""
	def join(self, x, other):

		"join self with x"
		x.setLeft(self.getRoot())
		self.root.setParent(x)

		"find node at other to join with such that the tree is balanced"
		node = other.getRoot()
		h = self.root.getHeight()
		while node.getHeight() > h:
			node = node.getLeft()
		
		"join trees at the found node"
		parent = node.getParent()
		parent.setLeft(x)
		x.setParent(parent)
		x.setRight(node)
		node.setParent(x)
		self.root = other.getRoot()
		

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		i = 0
		node = self.first

		while True:
			"compare node's value to val"
			if node.getValue() == val:
				return i
			
			"exit if node is last in list"
			if node is self.last:
				return -1

			"go to successor node"
			i += 1
			node = self.successor(node) #TODO self.successor()


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
		rank = node.left.getSize() + 1
		root = self.getRoot()
		parent = node

		"go up to the root"
		while parent is not root:
			node = parent
			parent = node.getParent()

			"every time we go up left add the size of parent's left subtree"
			if node is parent.getRight():
				rank += parent.left.getSize() + 1

		return rank
	

	"""returns the i-th node of the tree's in-order list
	
	@type i: int
	@pre: 1 <= i <= self.length()
	@param i: rank to search for
	@rtype: AVLNode
	@returns: node with rank i
	"""
	def select(self, i):
		node = self.getRoot()
		rank = node.left.getSize() + 1
		while i != rank:
			if i < rank:
				"search in the left subtree with i"
				node = node.getLeft()
			if i > rank:
				"search in the right subtree with i-rank"
				node = node.getRight()
				i -= rank
			rank = node.left.getSize() + 1
		return node
	

	"""returns the successor of a given node
	
	@type node: AVLNode
	@pre: node is inside the tree
	@param node: node to start searching from
	@rtype: AVLNode
	@returns: successor of node
	"""
	def successor(self, node):
		succ = node.getRight()

		if succ is not None:
			"return the minimum node of right subtree"
			while succ.getLeft() is not None:
				succ = succ.getLeft()
			return succ
		
		"get the first parent on the right of node"
		succ = node.getParent()
		while succ is not None and node is succ.getRight():
			node = succ
			succ = node.getParent()
		return succ


	"""returns the predecessor of a given node
	
	@type node: AVLNode
	@pre: node is inside the tree
	@param node: node to start searching from
	@rtype: AVLNode
	@returns: predecessor of node
	"""
	def predecessor(self, node):
		pred = node.getLeft()

		if pred is not None:
			"return the maximum node of left subtree"
			while pred.getRight() is not None:
				pred = pred.getRight()
			return pred
		
		"get the first parent on the left of node"
		pred = node.getParent()
		while pred is not None and node is pred.getLeft():
			node = pred
			pred = node.getParent()
		return pred
