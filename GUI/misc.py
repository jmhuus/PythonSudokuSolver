class Animal():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def PrintDetais(self):
		print("Hello my name is {} and I am {} years old.".format(self.name, self.age))





class Dog(Animal):
	def __init__(self, name, age, breed):
		Animal.__init__(self, name, age)
		self.breed = breed

	def printBreed(self):
		print("I am a {}.".format(self.breed))



milo = Dog("milo", 2, "German Shepherd")
milo.PrintDetais()
milo.printBreed()