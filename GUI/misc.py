

class Person():
	def __init__(self):
		self.name = "milo"

	def printName(self):
		print(self.name)




cells = []

for row in range(10):
	for col in range(10):
		newPerson = Person()
		cells.append({str(row)+str(col) : newPerson})