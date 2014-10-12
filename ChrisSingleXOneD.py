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

# determining if any cars will hits based on direction and time from intersection
def conflict(head):
	if head = None or head.next = None:
		return 0
	else:
		first = head
		while first.car.intersection != 1:
			first = first.next


class linkedListCarNode(object, time, entry, route):
	def __init__(self):
		self.next = None
		self.car = Car(time, entry, route)

# car class
class Car(object, time, entry, route):
	def __init__(self, time):
		self.reachIntersection = 3
		self.entry = entry
		self.route = route




# create an array of arrays of vehicle information
file_full_name = raw_input("Where are the car routes!?")
output_file_full_name = raw_input("Output file?")
output = open(output_file_full_name,'w')

vehicleRouteArray = fileToArray(file_full_name)
initialize
#  time
time = 0.0
head = None
light = True # True is NS, False is EW
toggleLight = False # determines whether the light should be changed
while vehicleRouteArray != []:
	# reset score variables
	NSScore = 0
	EWScore = 0

	# initialize all cars
	Car_initializing(vehicleRouteArray, time)

	# Determining the direction of light
	if #not conflict(): not |a - b| <= 1
		# determine direction of 
		if point.carsum(point.car.entry == ["A0","C0"]) != light:
			toggleLight = True
		else:
			toggleLight = False
	else:
		point = head
		while point != None:
			if point.carsum(point.car.entry == ["A0","C0"]):
				NSScore += min(1 / point.reachIntersection, 10)
			else:
				EWScore += min(1 / point.reachIntersection, 10)
		# based on the scores and current street light, decide on the future light
		if (NSScore > EWScore) != light:
			toggleLight = True

	# determine whether or not to toggle base on lights and write
	if toggleLight:
		light = not light
		stringToWrite = "%r 1\n" % (time)
		output.write(stringToWrite)
		toggleLight = False

	# increment timer
	time += 0.1

	#increment distance
	point = head
	before = point
	while point != None:
		if point.car.reachIntersection != 0:
			point.car.reachIntersection -= 0.1
		else:
			if sum(point.car.entry == ["A0","C0"]) == light: # car is at intersection and light is green
				if head = point:
					head = point.next
				else:
					before.next = point.next
		# increment pointers
		before = point
		point = point.next
