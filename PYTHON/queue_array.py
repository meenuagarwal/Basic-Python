class QueueArray():
	def __init__(self,size):
		self.my_list = []
		self.size = size

	def Enqueue(self,data):
		if isFull():
			raise ValueError("Queue is full")
		else:
			self.my_list.appned(data)
			return self.my_list

	def Dequese(self):
		if isEmpty():
			raise ValueError("Empty queue")
		else:
			return my_list.pop(0)

	def isEmpty(self):
		if len(self.my_list) == 0:
			return True
		else:
			return False