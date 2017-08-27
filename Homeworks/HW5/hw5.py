class Node():
	def __init__(self, _value=None, _next=None):
		self.value = _value
		self.next = _next
	
	def __str__(self):
		return str(self.value)

class LinkedList():
	# Takes a number and sets it as the value at the head of the LinkedList
	def __init__(self, node):
		self.head = node
		self.len = 1
	# Display the list in some reasonable way
	def __str__(self):
		result = ""
		checknode = self.head
		while checknode.next != None:
			result += str(checknode.value)
			result += " "
			checknode = checknode.next
		result += str(checknode.value)
		return result
	# Returns the length of the LinkedList
	def length(self):
		return self.len
	# Takes a number and adds it to the end of the LinkedList
	def addNode(self, new_node):
		checklastnode = self.head
		while checklastnode.next != None:
			checklastnode = checklastnode.next
		checklastnode.next = new_node
		self.len += 1
	# Takes a number and adds it after the after_node
	def addNodeAfter(self, new_node, after_node):
		new_node.next = after_node.next
		after_node.next = new_node
		self.len += 1
	# Takes a value and adds it before the before_node
	def addNodeBefore(self, new_node, before_node):
		if before_node == self.head:
			new_node.next = self.head
			self.head = new_node
		else:
			checknode = self.head
			while checknode.next != before_node:
				checknode = checknode.next
			checknode.next = new_node		
			new_node.next = before_node
		self.len += 1
	# Remove a node from the list
	def removeNode(self, node_to_remove):
		try:
			if node_to_remove == self.head:
				self.head = self.head.next
				node_to_remove.next = None
				self.len -= 1
			else:
				checknode = self.head
				while checknode.next != node_to_remove:
					checknode = checknode.next
				checknode.next = node_to_remove.next
				self.len -= 1
		except:
			raise TypeError, "Node to remove is not in the linked list!"			
	# Takes a value, removes all nodes with that value
	def removeNodesByValue(self, value):
		checknode = self.head
		while checknode != None:
			if checknode.value == value:
				self.removeNode(checknode)
				checknode = checknode.next
			else:
				checknode = checknode.next		
	# A helper function for reverse()
	def findNodeBefore(self, before_node):
		checknode = self.head
		while checknode.next != before_node:
			checknode = checknode.next
		return checknode
	# Reverse the order of the linked list
	def reverse(self):
		checknode = self.head
		while checknode.next != None: 
			checknode = checknode.next
		new_head = checknode
		while checknode != self.head:
			checknode.next = self.findNodeBefore(checknode)
			checknode = checknode.next
		self.head.next = None
		self.head = new_head
		return self


# -------- Test --------
node1 = Node(5)
node2 = Node(12)
node3 = Node(9)
node4 = Node(2)

test1 = LinkedList(node1)
test1.length()
test1.addNode(node2)
test1.addNode(node3)
test1.addNode(node4)
print test1
test1.head.next.next.next.value

node5 = Node(10)
test1.addNodeAfter(node5, node3)
test1.head.next.next.value
test1.head.next.next.next.value
test1.head.next.next.next.next.value

node0 = Node(0)
test1.addNodeBefore(node0, node1) # Add a node at the very beginning
test1.head.value
test1.head.next.value
node6 = Node(6)
test1.addNodeBefore(node6, node3) # Add a node in the middle
test1.head.next.value
test1.head.next.next.value
test1.head.next.next.next.value

node7 = Node(7)
test1.removeNode(node7) # Expect a type error
test1.removeNode(node0) # Remove the head
test1.removeNode(node3) # Remove a node in the middle

test1.removeNodesByValue(5) # Remove the head value
test1.removeNodesByValue(2) # Remove the tail value

print test1.reverse()
test1.head.value
test1.head.next.value
