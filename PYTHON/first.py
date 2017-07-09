class Group:
	def __init__(self,first,last):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@gmail.com'

	def fullname(self):
		return ('{} {}' .format(self.first,self.last))

std_1 = Group('Meenu','Agarwal')
print std_1.fullname()
print std_1.email