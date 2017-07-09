import random

class Blob:

	def __init__(self, color, x_bounds, y_bounds):

		self.size = random.randrange(5,15)
		self.color = color
		self.x_bounds = x_bounds
		self.y_bounds = y_bounds
		self.x = random.randrange(0,x_bounds)
		self.y = random.randrange(0,y_bounds)

	def move(self):
		self.move_x = random.randrange(-2,3)
		self.move_y = random.randrange(-2,3)
		self.x += self.move_x
		self.y += self.move_y

		#Restricting our blob object to the environment boundary
		if (self.x < 0):self.x = 0
		elif (self.x >self.x_bounds):self.x = self.x_bounds
		if (self.y < 0):self.y = 0
		elif (self.y > self.y_bounds):self.y = self.y_bounds
