#username - complete info
#id1      - 325541878 
#name1    - Amitai Wolf 
#id2      - 214208704
#name2    - Eivi Katz

from printree import *

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):

		"virtual nodes only have value and size fields"
		self.value = value
		self.parent = None

		if value != None:

			"create two children, since they are virtual the recursion stops immediatly"
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
		self.left = AVLNode(None) if node is None else node
		self.update()


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = AVLNode(None) if node is None else node
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
	

	"""updates both size and height fields

	@rtype: int
	@returns: the change in height
	"""
	def update(self):
		if self.isRealNode():
			height = self.getHeight()
			self.updateHeight()
			self.updateSize()
			return abs(self.getHeight() - height)
		return 0

	
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
	def notBalanced(self):
		return abs(self.balanceFactor()) >= 2

	
	"""join operation between left and right with self

	@type left: AVLNode
	@param left: left subtree to join with
	@type right: AVLNode
	@param right: right subtree to join with
	@rtype: AVLNode
	@returns: the root of the new tree
	"""
	def join(self, left, right):

		"divide by cases to get a balanced tree"
		if abs(left.getHeight() - right.getHeight()) < 2:
			"roughly equal height"
			self.joinEq(left, right)
			return self

		if left.getHeight() > right.getHeight():
			"left tree is bigger"
			self.joinRL(left, right)
			root = left

		elif left.getHeight() < right.getHeight():
			"right tree is bigger"
			self.joinLR(left, right)
			root = right
		
		node = self
		while node is not root:
			node = node.parent
			node.update()
		return root
	

	"""join operation between left and right with self

	@type left: AVLNode
	@param left: left subtree to join with
	@type right: AVLNode
	@param right: right subtree to join with
	@pre: difference in height is -1, 0 or 1
	"""
	def joinEq(self, left, right):

		"join trees the naive way"
		self.setLeft(left)
		self.setRight(right)
		left.setParent(self)
		right.setParent(self)


	"""join operation between left and right with self

	@type left: AVLNode
	@param left: left subtree to join with
	@type right: AVLNode
	@param right: right subtree to join with
	@pre: left.height < right.height
	"""
	def joinLR(self, left, right):

		"set left root as child of self"
		self.setLeft(left)
		left.setParent(self)

		"find node on the left side of right tree with similar height"
		node = right
		h = left.getHeight()
		while node.getHeight() > h:
			node = node.left

		"connect the right tree to self at the found node"
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

		"set right root as child of self"
		self.setRight(right)
		right.setParent(self)

		"find node on the right side of left tree with similar height"
		node = left
		h = right.getHeight()
		while node.getHeight() > h:
			node = node.right

		"connect the left tree to self at the found node"
		parent = node.getParent()
		parent.setRight(self)
		self.setParent(parent)
		node.setParent(self)
		self.setLeft(node)
	

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

		"get head and tail nodes of the tree"
		head, tail = self, self
		while head.getLeft() != None:
			head = head.getLeft()
		while tail.getRight() != None:
			tail = tail.getRight()
		treeList.head, treeList.tail = head, tail
		
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
		self.head = self.root
		self.tail = self.root


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return not self.root.isRealNode()


	"""does rotations to balance the AVL tree
	
	@type node: AVLNode
	@param node: node to start fixing up from
	@type roll: bool
	@param roll: allow rotating unbalanced nodes, True by default
	@pre: node is in the tree
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing 
	"""
	def balance(self, node, roll=True):
		balance_ops = 0
		while node is not None:

			"""update a node on the way to the root
			when balancing a tree the most a height can change is by 1"""
			balance_ops += node.update()

			if roll and node.notBalanced():

				"save the parent, roll node and continue upwards"
				parent = node.parent
				balance_ops += self.rotate(node)
				node = parent

			else:
				node = node.parent

		return balance_ops

	"""rotate the node to balance the tree

	@type node: AVLNode
	@param node: node to perform rotation from
	@pre: balance factor of node is either 2 or -2
	@rtype: int
	@returns: number of rotations needed (either 1 or 2)
	"""
	def rotate(self, node):
		if node.balanceFactor() == 2:

			"rotate to the right"
			if node.left.balanceFactor() in [0, 1]:
				self.rotateR(node)
				return 1
			elif node.left.balanceFactor() == -1:
				self.rotateLR(node.left)
				self.rotateR(node)
				return 2
		
		elif node.balanceFactor() == -2:

			"rotate to the left"
			if node.right.balanceFactor() in [-1, 0]:
				self.rotateL(node)
				return 1
			elif node.right.balanceFactor() == 1:
				self.rotateRL(node.right)
				self.rotateL(node)
				return 2
		
		"shouldn't have come here"
		return 0


	"""perform rotation right
	
	"""
	def rotateR(self, node):
		parent = node.parent
		left = node.left

		"change node's left child to left's right child"
		node.setLeft(left.right)
		left.right.setParent(node)

		"change left's right child to node"
		left.setRight(node)
		node.setParent(left)

		"change left's parent to node's parent"
		left.setParent(parent)
		if node is self.root:
			self.root = left
		else:
			if parent.left is node:
				parent.setLeft(left)
			else:
				parent.setRight(left)


	"""perform rotation left
	
	"""
	def rotateL(self, node):
		parent = node.parent
		right = node.right
		
		"change node's right child to right's left child"
		node.setRight(right.left)
		right.left.setParent(node)

		"change right's left child to node"
		right.setLeft(node)
		node.setParent(right)

		"change right's parent to node's parent"
		right.setParent(parent)
		if node is self.root:
			self.root = right
		else:
			if parent.right is node:
				parent.setRight(right)
			else:
				parent.setLeft(right)


	"""perform small rotation left
	
	"""
	def rotateLR(self, node):
		parent = node.parent
		right = node.right

		"change node's right child to right's left child"
		right.left.setParent(node)
		node.setRight(right.left)

		"change right's left child to node"
		right.setLeft(node)
		node.setParent(right)

		"change right's parent to node's parent"
		parent.setLeft(right)
		right.setParent(parent)

	
	"""perform small rotation right
	
	"""
	def rotateRL(self, node):
		parent = node.parent
		left = node.left

		"change node's left child to left's right child"
		left.right.setParent(node)
		node.setLeft(left.right)

		"change left's right child to node"
		left.setRight(node)
		node.setParent(left)

		"change left's parent to node's parent"
		parent.setRight(left)
		left.setParent(parent)


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		return None if self.empty() else self.select(i + 1).getValue()


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
			self.head = z
			self.tail = z
			return 0

		if i == self.length():

			"find the maximum and make z its right child"
			self.tail.setRight(z)
			z.setParent(self.tail)
			self.tail = z
		
		else:

			"find the node of rank i+1"
			node = self.select(i + 1)
			if node.getLeft() == None:

				"if it has no left child make z its left child"
				node.setLeft(z)
				z.setParent(node)
				if i == 0:
					self.head = z
		
			else:

				"find its predecessor and make z its right child"
				node = self.predecessor(node)
				node.setRight(z)
				z.setParent(node)

		return 1 + self.balance(z)


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		if self.empty():
			return 0
		
		"find node at index i, remove it from the tree and delete"
		node = self.select(i + 1)
		res = self.remove(node)
		del(node)
		return res


	"""deletes a node in the list
	
	@type node: AVLNode
	@param node: the node to be deleted
	@type roll: bool
	@param roll: rotate unbalanced nodes after deleting, True by default
	@pre: node is in the tree
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def remove(self, node, roll=True):
		parent = node.getParent()

		if self.length() == 1 and node is self.root:
			"empty the tree"
			self.root = AVLNode(None)
			self.head = self.root
			self.tail = self.root
			return 0
		
		if node is self.head:
			self.head = self.successor(node)
			
		if node is self.tail:
			self.tail = self.predecessor(node)
		
		if node.getLeft() == None:
			"node has no left child, bypass it for its right child"
			"set the child of node's parent"
			if node is self.root:
				self.root = node.right
			else:
				if node is parent.getLeft():
					parent.setLeft(node.right)
				elif node is parent.getRight():
					parent.setRight(node.right)
			
			"set the parent of node's child"
			node.right.setParent(parent)
			return self.balance(parent, roll)
		
		elif node.getRight() == None:
			"node has no right child, bypass it for its left child"
			"set the child of node's parent"
			if node is self.root:
				self.root = node.left
			else:
				if node is parent.getLeft():
					parent.setLeft(node.left)
				elif node is parent.getRight():
					parent.setRight(node.left)
			
			"set the parent of node's child"
			node.left.setParent(parent)
			return self.balance(parent, roll)
		
		else:
			"node has two children, replace node with its successor"
			"find successor and delete its node from the tree"
			"since it has no left child the recursion stops immediately"
			succ = self.successor(node)
			res = self.remove(succ, roll)
			parent = node.parent
			if node is self.tail:
				self.tail = succ

			"set successor's children"
			succ.setLeft(node.left)
			succ.setRight(node.right)
			node.left.setParent(succ)
			node.right.setParent(succ)

			"set successor's parent"
			succ.setParent(parent)
			if node is self.root:
				self.root = succ
			else:
				if node is parent.getLeft():
					parent.setLeft(succ)
				elif node is parent.getRight():
					parent.setRight(succ)
			return res
	

	"""removes the last node in the tree for concat operation

	if you find why this method is different than calling the standard remove method with self.tail
	please send your answers to amitaiwolf@mail.tau.ac.il
	"""
	def removeTail(self):
		tail = self.tail
		if tail is self.root:
			self.root = tail.left
			self.tail = self.root
			tail.left.setParent(None)
		else:
			self.tail = self.predecessor(tail)
			tail.parent.setRight(tail.left)
			tail.left.setParent(tail.parent)
		return self.balance(tail.parent, False)


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return None if self.empty() else self.head.getValue()


	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return None if self.empty() else self.tail.getValue()


	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		if self.empty():
			return []
			
		array = []
		node = self.head

		for i in range(self.length()):
			"append value to array"
			array.append(node.getValue())

			"go to successor node"
			node = self.successor(node)
		
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

		"get node to split from"
		node = self.select(i + 1)
		val = node.getValue()
		left = node.left
		right = node.right
		parent = node.getParent()

		while node is not self.root:
			if node is parent.getRight():

				"join left trees"
				node = parent
				parent = parent.getParent()
				left = node.join(node.left, left)

			elif node is parent.getLeft():

				"join right trees"
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

		"if self or lst are empty, no joining is required"
		if lst.empty():
			return self.root.getHeight() + 1
		if self.empty():
			self.root = lst.root
			self.head = lst.head
			self.tail = lst.tail
			return lst.root.getHeight() + 1

		diff = abs(self.root.getHeight() - lst.root.getHeight())

		"delete the tail of self to use in join op"
		tail = self.tail
		self.removeTail()
		tail.setParent(None)
		self.root = tail.join(self.root, lst.root)
		self.tail = lst.tail

		"lst cannot be used by this point"
		return diff


	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		i = 0
		node = self.head

		for i in range(self.length()):
			"compare node's value to val"
			if node.getValue() == val:
				return i

			"go to successor node"
			i += 1
			node = self.successor(node)
		return -1


	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return None if self.empty() else self.root
	

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
				node = node.left

			if i > rank:
				"search in the right subtree with i-rank"
				node = node.right
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
		
		"get the head parent on the right of node"
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
		
		"get the head parent on the left of node"
		pred = node.getParent()
		while pred is not None and node is pred.getLeft():
			node = pred
			pred = node.getParent()
		return pred
	
	
	"""methods for tester, delete when done"""
	def append(self, val):
		return self.insert(self.length(), val)
	def getTreeHeight(self):
		return self.root.getHeight()