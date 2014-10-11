class DumbSim:
    def __init__(self, arrayOfArrivals):
        self.arrivals = arrayOfArrivals
    
    def run(self):
        returnArray = []
        
        lastTimeChange = 30
        returnArray.append([lastTimeChange, 1])
        
        for arrival in self.arrivals:
            if arrival[0] > (lastTimeChange-3):
                lastTimeChange += 30
                returnArray.append([lastTimeChange, 1])
                
        lastTimeChange += 30
        returnArray.append([lastTimeChange, 1])
        