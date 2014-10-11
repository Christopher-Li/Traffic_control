def calcSingleXOneWayTotalWaitTimeSquared(vehicleRouteFileName,trafficLightFileName):
	vehicleRouteArray = fileToArray(vehicleRouteFileName)
	trafficLightArray = fileToArray(trafficLightFileName)
	isNS = True	#boolean
	for i in range(0,len(vehicleRouteArray)):
		j = 0;
		
		while((int(vehicleRouteArray[i][0]) + 3)<)