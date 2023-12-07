import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2015_day_2_input.txt"

ribbonLengths = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		dimensions = line.split("x")
		dimensions = [int(dimension) for dimension in dimensions]
		dimensions.sort()
		ribbonLength = dimensions[0] * 2 + dimensions[1] * 2
		slack = dimensions[0] * dimensions[1] * dimensions[2]
		ribbonLengths.append(ribbonLength + slack)

print(sum(ribbonLengths))