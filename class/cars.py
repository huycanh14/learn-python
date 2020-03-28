class Car():
	"""info car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.km_reading = 0

	def get_des(self):
		"""printing info"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name

	def read_km(self):
		#print info about km
		print('This car has ' + str(self.km_reading) + ' km on it')

	def update_km(self, km):
		# update km
		self.km_reading = km

my_new_car = Car('audi', 'a4', 2016)

print (my_new_car.get_des())
my_new_car.update_km(300)
my_new_car.read_km()