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





• removeNode(self, node_to_remove): Removes a node from the list
• removeNodesByValue(self, value): Takes a value, removes all nodes
with that value
• reverse(self): Reverses the order of the linked list
• 
• hasCycle(self): Bonus: Returns true if this linked list has a cycle. This
is non-trivial

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



