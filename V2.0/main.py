####### Documentation #############
# Current problems: Doesn't account for multiple intersections
#
#
#






#import a bunch of crap

file_full_name = raw_input("Where are the car routes!?")
output_file_full_name = raw_input("Output file?")
output = open(output_file_full_name,'w')

#vehicleRouteArray = fileToArray(file_full_name)

class test(vehicleRouteArray):
	def __init__(self, vehicleRouteArray):
		self.vehicleRouteArray = vehicleRouteArray
		self.time = 0.0 # initialize time at 0

	def run(self):
		# Keep iterating until the vehicleRouteArray is empty
		while (self.vehicleRouteArray):
			while self.vehicleRouteArray[0][0] == self.time: # run if the next car's entrance point is equal to 
				if self.vehicleRouteArray[0][1].startswith("B0") or
				self.vehicleRouteArray[0][1].startswith("D0"): 
					self.vehicleRouteArray[0][1] = self.vehicleRouteArray[2:] # remove "B0" or "D0"
					#append car to NS
				else:
					self.vehicleRouteArray[0][1] = self.vehicleRouteArray[2:] # remove "A0" or "C0"
					#append car to EW

				#self.vehicleRouteArray.pop[0]

			#initialize variables
			# NSScore = 0
			# EWScore = 0
			# toggleLight =

			# if (self.time + 2) >= NScarLL.timeCrossSensor and 
			# (self.time + 2) >= EWcarLL.timeCrossSensor:
				# iterate through NScarLL
				point = NScarLL.head
				# while point != None:
					#NSScore += 1 / ((self.time + 4) - point.timeCrossSensor
					point = point.next

				# iterate through EWcarLL
				point = EWcarLL.head
				# while point != None:
					#EWScore += 1 / ((self.time + 4) - point.timeCrossSensor
					point = point.next

				if (NSScore > EWScore) != light:
					toggleLight = True

				if toggleLight:
					light = not light
					stringToWrite = "%r 1\n" % (self.time)
					output.write(stringToWrite)
					toggleLight = False

			# increment time
			self.time += 0.1

