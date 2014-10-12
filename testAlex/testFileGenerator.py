import random

class intersectionForTestSuite:
	def __init__(self,value):
		self.value = value
		self.up = self.value - 3 if (self.value >= 3) else None
		self.left = self.value - 1 if(self.value % 3 != 0) else None
		self.down = self.value + 3 if (self.value < 6) else None
		self.right = self.value + 1 if (self.value % 3 != 2) else None

class startingPoint:
	def __init__(self,next):
		self.next = next

class route:
	def __init__(self,startingPoint):

intersectionArray[None]*9
intersectionArray[0] = intersectionForTestSuite(0)
intersectionArray[1] = intersectionForTestSuite(1)
intersectionArray[2] = intersectionForTestSuite(2)
intersectionArray[3] = intersectionForTestSuite(3)
intersectionArray[4] = intersectionForTestSuite(4)
intersectionArray[5] = intersectionForTestSuite(5)
intersectionArray[6] = intersectionForTestSuite(6)
intersectionArray[7] = intersectionForTestSuite(7)
intersectionArray[8] = intersectionForTestSuite(8)

startingPointArray[None]*4
startingPointArray[0][0] = startingPoint(intersection0)
startingPointArray[0][1] = startingPoint(intersection1)
startingPointArray[0][2] = startingPoint(intersection2)
startingPointArray[1][0] = startingPoint(intersection2)
startingPointArray[1][1] = startingPoint(intersection5)
startingPointArray[1][2] = startingPoint(intersection8)
startingPointArray[2][0] = startingPoint(intersection6)
startingPointArray[2][1] = startingPoint(intersection7)
startingPointArray[2][2] = startingPoint(intersection8)
startingPointArray[3][0] = startingPoint(intersection0)
startingPointArray[3][1] = startingPoint(intersection3)
startingPointArray[3][2] = startingPoint(intersection6)

