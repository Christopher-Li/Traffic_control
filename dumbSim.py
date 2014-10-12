class DumbSim:
    def run(self,vehicleRouteFileName):
        inputData = fileToArray(vehicleRouteFileName)
        file_full_name = raw_input("Give output file unique file name: ")
        f = open(file_full_name,'w')
        timeInterval = 30
        lastTimeChange = timeInterval
        f.write(str(lastTimeChange) + ' 1')
        for arrival in self.inputData:
            if arrival[0] > (lastTimeChange-3):
                lastTimeChange += timeInterval
                f.write(str(lastTimeChange) + ' 1')  
        lastTimeChange += timeInterval
        f.write(str(lastTimeChange) + ' 1')
        