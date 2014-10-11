def calcSingleXOneWayTotalTime(vehicleRouteFileName,trafficLightFileName):
	vehicleRouteArray = fileToArray(vehicleRouteFileName)
	trafficLightArray = fileToArray(trafficLightFileName)
	totalTime = 0
	for i in range(0,len(vehicleRouteArray)):
		j = 0
		isNS = True
		while (3 + float(vehicleRouteArray[i][0]) > float(trafficLightArray[j][0]) or ((vehicleRouteArray[i][1] == 'B' or vehicleRouteArray[i][1] == 'D') and isNS)):
			j = j + 1
			isNS = not(isNS)
		totalTime += float(trafficLightArray[j][0]) - float(vehicleRouteArray[i][0]) + 7
	return totalTime