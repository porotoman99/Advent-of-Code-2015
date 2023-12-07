import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2015_day_2_input.txt"

paperSizes = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		dimensions = line.split("x")
		dimensions = [int(dimension) for dimension in dimensions]
		sides = [dimensions[0] * dimensions[1], dimensions[0] * dimensions[2], dimensions[1] * dimensions[2]]
		slack = min(sides)
		paperSizes.append(2 * sum(sides) + slack)

print(sum(paperSizes))