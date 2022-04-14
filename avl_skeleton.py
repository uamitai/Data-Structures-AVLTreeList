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
			self.left.setParent(self)
			self.right.setParent(self)
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
		self.update()

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		if node == None:
			self.right = AVLNode(None)
		else:
			self.right = node
		self.update()

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
	
	def update(self):
		self.updateHeight()
		self.updateSize()
	
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


	"""join operation between left and right with self

	@type left: AVLNode
	@param left: left subtree to join with
	@type right: AVLNode
	@param right: right subtree to join with
	@pre: left.height < right.height
	"""
	def joinLR(self, left, right):
		self.setLeft(left)
		left.setParent(self)

		node = right
		h = left.getHeight()
		while node.getHeight() > h:
			node = node.left

		parent = node.getParent()
		parent.setLeft(self)
		self.setParent(parent)
		node.setParent(self)
		self.setRight(node)

	"""join operation between left and right with self

	@type left: AVLNode
	@param left: left subtree to join with
	@type right: AVLNode
	@param right: right subtree to join with
	@pre: left.height > right.height
	"""
	def joinRL(self, left, right):
		self.setRight(right)
		right.setParent(self)

		node = left
		h = right.getHeight()
		while node.getHeight() > h:
			node = node.right

		parent = node.getParent()
		parent.setRight(self)
		self.setParent(parent)
		node.setParent(self)
		self.setLeft(node)
	
	"""join operation between left and right with self

	@type left: AVLNode
	@param left: left subtree to join with
	@type right: AVLNode
	@param right: right subtree to join with
	@pre: left.height = right.height
	"""
	def joinEq(self, left, right):
		self.setLeft(left)
		self.setRight(right)
		left.setParent(self)
		right.setParent(self)
	
	def join(self, left, right):
		if left.getHeight() > right.getHeight():
			self.joinRL(left, right)
			return left
		if left.getHeight() < right.getHeight():
			self.joinLR(left, right)
			return right
		if left.getHeight() == right.getHeight():
			self.joinEq(left, right)
			return self
	
	"""turns node into an AVLTreeList type object, with self as root

	@rtpye: AVLTreeList
	@returns: the subtree of self as a list
	"""
	def toTreeList(self):
		"construct an empty tree and set self as the root"
		treeList = AVLTreeList()
		if not self.isRealNode():
			return treeList
		treeList.root = self
		self.setParent(None)

		"get first and last nodes of the tree"
		first, last = self, self
		while first.getLeft() != None:
			first = first.getLeft()
		while last.getRight() != None:
			last = last.getRight()
		treeList.first, treeList.last = first, last
		
		return treeList



"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = AVLNode(None)
		self.first = self.root
		self.last = self.root


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
			if abs(node.balanceFactor()) < 2:
				node = node.getParent()
				continue
			else:
				rotation()
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
		node = self.select(i + 1)
		res = self.deleteNode(node)
		del(node)
		return res


	"""deletes a node in the list
	
	@type node: AVLNode
	@param node: the node to be deleted
	@pre: node is in the tree
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def deleteNode(self, node):
		parent = node.getParent()

		if (self.length() == 1 and node is self.root) or self.empty():
			"edge case for empty tree"
			self.root = AVLNode(None)
			return 0
		
		if node.getLeft() == None:
			"node has no left child, bypass it for its right child"

			if node is self.first:
				"update first node"
				self.first = self.successor(node)
			
			"set the child of node's parent"
			if parent != None:
				if node is parent.getLeft():
					parent.setLeft(node.right)
				elif node is parent.getRight():
					parent.setRight(node.right)
			else:
				self.root = node.right
			
			"set the parent of node's child"
			node.right.setParent(parent)
		
		elif node.getRight() == None:
			"node has no right child, bypass it for its left child"

			if node is self.last:
				"update last node"
				self.last = self.predecessor(node)
			
			"set the child of node's parent"
			if parent != None:
				if node is parent.getLeft():
					parent.setLeft(node.left)
				elif node is parent.getRight():
					parent.setRight(node.left)
			else:
				self.root = node.left
			
			"set the parent of node's child"
			node.left.setParent(parent)
		
		else:
			"node has two children, replace node with its successor"
			"find successor and delete its node from the tree"
			"since it has no left child the recursion stops immediately"
			succ = self.successor(node)
			self.deleteNode(succ)

			"set all pointers of children, successor and parent"
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
		
		return self.balance(parent) #TODO balance tree


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
		return None if self.empty() else self.last.getValue()


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
		node = self.select(i + 1)
		val = node.getValue()
		left = node.left
		right = node.right
		parent = node.getParent()

		while node is not self.root:
			if node is parent.getRight():
				node = parent
				parent = parent.getParent()
				left = node.join(node.left, left)
			elif node is parent.getLeft():
				node = parent
				parent = parent.getParent()
				right = node.join(right, node.right)

		return [left.toTreeList(), val, right.toTreeList()]



	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		if lst.empty():
			return self.root.getHeight() + 1
		if self.empty():
			self = lst
			return lst.root.getHeight() + 1

		diff = abs(self.root.getHeight() - lst.root.getHeight())
		node = self.last
		self.deleteNode(node)
		self.root = node.join(self.root, lst.root)
		self.last = lst.last
		return diff


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
