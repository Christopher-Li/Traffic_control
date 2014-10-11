import random

file_full_name = raw_input("What file would you like to create a test suite for?")

f = open(file_full_name, 'w')

#initialize time variable
time = 0.0
while time < 200:
	# Randomly determine entry points, times, and route
	entryPointInt = random.randint(0,3)
	timeInt = random.randint(0,20)
	flag = 1 # determines whether you should run at this loop or not.

	if entryPointInt == 0:
		entryPoint = "A0"
	elif entryPointInt == 1:
		entryPoint = "B0"
	elif entryPointInt == 2:
		entryPoint = "C0"
	elif entryPointInt == 3:
		entryPoint = "D0"

	if timeInt == 1:
		time += 1
	elif timeInt >= 2:
		flag = 0
		time += 1

	if flag == 1:
		stringToWrite = "%r %s S" % (time/10, entryPoint)
		f.write(str(stringToWrite) + "\n")


f.close()
