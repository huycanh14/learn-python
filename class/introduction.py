# class Test():
class Test(object):
	def __init__(self, name, age): #khai bao constructor
		self.name = name
		self.age = age

	def sit(self): #khai bao method
		print(self.name.title() + ' is now sitting')

	def sit2(self):
		print(self.name.title(), str(self.age))


# def test(name, age):
# 	pass #ket thuc

m = Test('kain', 22)
# m.sit()
# m.sit2()
persion1 = Test('Canh', 22)
persion2 = Test('Jack', 22)

persion1.sit()