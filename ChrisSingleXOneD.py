def fileToArray(vehicleRouteFileName):
	vehicleRouteData = open(vehicleRouteFileName,'r')
	vehicleRouteDataArray = []
	for line in vehicleRouteData:
		vehicleRouteDataArray.append(line.split())
	vehicleRouteData.close()
	return vehicleRouteDataArray

# Initializing cars when they hit the sensor
def Car_initializing(vehicleRouteArray, time):
	for vehicles in vehicleRouteArray:
		if vehicles[0] == time:
			if head == None:
				global head
				head = linkedListCarNode(vehicles[0], vehicles[1], vehicles[2])
			else:
				temp = head
				while temp.next != None:
					temp = temp.next
				global temp
				temp.next = linkedListCarNode(vehicles[0], vehicles[1], vehicles[2])
			#initialize the car

class linkedListCarNode(object, time, entry, route):
	def __init__(self):
		self.next = None
		self.value = Car(time, entry, route)

# car class
class Car(object, time, entry, route):
	def __init__(self, time):
		self.reachIntersection = 3
		self.intersection = 1
		self.entry = entry
	def changeIntersection(self):
		self.timeLeftIntersection = 0


# create an array of arrays of vehicle information
file_full_name = raw_input("Where are the car routes!?")

vehicleRouteArray = fileToArray(file_full_name)

# initialize time
time = 0.0
head = None
while vehicleRouteArray != []:
	# initialize all cars
	Car_initializing(vehicleRouteArray, time)
	for # cars in linkedlist
		# increment formula for determining importance of direction
	# based on formula, decide whether to change lights
	# increment timeLeftIntersection if the car is traveling through the intersection
	# increment wait time if car is waiting
	# if timeLeftIntersection = 1 the delete the car
