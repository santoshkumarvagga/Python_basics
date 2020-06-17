class Hey:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		
	def sum(self):
		return self.a+self.b
	
A = Hey(4,5)
print(A.sum())
