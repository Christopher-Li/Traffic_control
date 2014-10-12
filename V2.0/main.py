import mainclasses, fileToArray


file_full_name = raw_input("Where are the car routes!?")
output_file_full_name = raw_input("Output file?")
output = open(output_file_full_name,'w')

vehicleRouteArray = fileToArray.fileToArray(file_full_name)

class test:
	def __init__(self, vehicleRouteArray):
		self.vehicleRouteArray = vehicleRouteArray
		self.time = 0.0 # initialize time at 0
		self.intersections = list()
		self.intersections.append(mainclasses.Intersection())

	def run(self):
		# initialize variables

		lightIsNS = True
		toggleLight = False
		
		# Keep iterating until the vehicleRouteArray is empty
		while self.vehicleRouteArray or self.intersections[0].nsCarLL.isEmpty() or self.intersections[0].ewCarLL.isEmpty():
			while self.vehicleRouteArray and self.vehicleRouteArray[0][0] == str(self.time): # run if the next car's entrance point is equal to 
				if self.vehicleRouteArray[0][1].startswith("B0") or self.vehicleRouteArray[0][1].startswith("D0"): 
					self.vehicleRouteArray[0][1] = self.vehicleRouteArray[0][1][2:] # remove "B0" or "D0"
					#append car to NS
					self.intersections[0].nsCarLL.append(mainclasses.Car(self.vehicleRouteArray[0][1],float(self.vehicleRouteArray[0][0])))
				else:
					self.vehicleRouteArray[0][1] = self.vehicleRouteArray[0][1][2:] # remove "A0" or "C0"
					#append car to EW
					self.intersections[0].ewCarLL.append(mainclasses.Car(self.vehicleRouteArray[0][1],float(self.vehicleRouteArray[0][0])))
				
				self.vehicleRouteArray = self.vehicleRouteArray[1:]
				
			# decide whether the program should iterate and check scores or not
			# complications are for if either linkedlist is empty
			if self.intersections[0].nsCarLL.isEmpty():
				if self.intersections[0].ewCarLL.isEmpty():
					iterate = False
				else:
					iterate = (self.time + 2) >= self.intersections[0].ewCarLL.head.timeCrossSensor
			else:
				if self.intersections[0].ewCarLL.isEmpty():
					iterate = (self.time + 2) >= self.intersections[0].nsCarLL.head.timeCrossSensor
				else:
					iterate = ((self.time + 2) >= self.intersections[0].nsCarLL.head.timeCrossSensor) or ((self.time + 2) >= self.intersections[0].ewCarLL.head.timeCrossSensor)

			# if (self.time + 2) >= nsCarLL.timeCrossSensor and 
			# (self.time + 2) >= ewCarLL.timeCrossSensor:

			if iterate:
				if (self.intersections[0].nsCarLL.getScore() > self.intersections[0].ewCarLL.getScore()) != lightIsNS:
					toggleLight = True

				if toggleLight:
					lightIsNS = not lightIsNS
					stringToWrite = "%r 0" % (self.time)
					print self.time
					output.write(str(stringToWrite) + "\n")
					toggleLight = False

			print self.time
			print self.intersections[0].nsCarLL.head
			# remove elements
			if lightIsNS:
				while not self.intersections[0].nsCarLL.isEmpty() and self.intersections[0].nsCarLL.head.timeCrossSensor <= self.time - 3:
					self.intersections[0].nsCarLL.removeHead()
			else:
				while not self.intersections[0].ewCarLL.isEmpty() and self.intersections[0].ewCarLL.head.timeCrossSensor <= self.time - 3:
					self.intersections[0].ewCarLL.removeHead()

			# increment time
			self.time += 0.1

		# close files
		output.close()

testcase = test(vehicleRouteArray)
testcase.run()