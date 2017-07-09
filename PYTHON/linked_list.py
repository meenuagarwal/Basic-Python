class Node(object):
	def __init__(self,data = None, next_node = None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_nextnode(self):
		return self.next_node

	def set_next(self,new_next):
		self.new_next = new_next


class LinkedList(object):

	def __init__(self,head=None):
		self.head = head

	def insert_node(self,data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def size(self):
		current = self.head
		count = 0 
		while current :
			count += 1
			current = current.get_nextnode()
		return count

	def search(self,data):
		current = self.head
		found = False
		while current and (found is False):
			if current.get_data() == data:
				found = True
			else:
				current = current.get_nextnode()
		if current is None:
			raise ValueError("Data requested is not found")
		return current

