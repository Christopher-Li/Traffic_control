def fileToArray(fileName):
	fileData = open(fileName,'r')
	fileDataArray = []
	for line in fileData:
		fileDataArray.append(line.split())
	fileData.close()
	return fileDataArray