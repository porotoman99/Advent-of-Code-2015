import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2015_day_1_input.txt"

with open(inputFilePath) as inputFile:
	for line in inputFile:
		upCount = line.count("(")
		downCount = line.count(")")

print(upCount - downCount)