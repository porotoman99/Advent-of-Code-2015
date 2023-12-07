import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2015_day_1_input.txt"

with open(inputFilePath) as inputFile:
	for line in inputFile:
		position = 0
		index = 0
		for char in line:
			if(char == "("):
				position += 1
			elif(char == ")"):
				position -= 1
			index += 1
			if(position == -1):
				print(index)
				break