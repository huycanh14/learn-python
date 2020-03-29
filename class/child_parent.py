class Parent(object):
	"""docstring for Parent"""
	def __init__(self, name, age):
		self.name = name
		self.age = age


	def print_info(self):
		full_name = self.name + " " + str(self.age)
		print(full_name.title())



class Child(Parent):	 #goi ke thua claa Parent
	# pass
	def __init__(self, name, age):
		super().__init__(name, age) #super ke thua Parent va khai bao tai su dung param =>python 3.x
		#Cach khai bao khac: Parent.__init__(self, name, age)
		# python 2.x, khai bao:
		# super(Parent, self).__init__(name, age)
		self.gender = 'Boy'
		self.people = People()
	

	def print_info(self):
		print(self.gender)
		# print("Ke thua phuong thuc, ket qua:" )


class People():
	def __init__(self, height = 170):
		self.height = height


	def show_heigt(self):
		print('Height: ' + str(self.height))


m = Parent('kain', 22)
m.print_info()

t2 = Child('canh', 18)
t2.print_info()

t2.people.show_heigt()
