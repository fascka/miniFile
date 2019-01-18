import os
import sys
relativePath = os.getcwd()
inputPath = sys.argv[1]
outputPath = sys.argv[2]
removeSpace = sys.argv[3]
inputFile = open(relativePath + '\\' + inputPath,"r")
outputFile = open(relativePath + '\\' + outputPath,"w")
lastChar = ''
while True:
	char=inputFile.read(1)
	if not char: break
	if char=='\n': char = ''
	if char=='\t': char = ''
	if char=='\v': char = ''
	if removeSpace=="t" and lastChar==' ' and char == ' ': char = ''
	outputFile.write(char)
	lastChar = char
outputFile = open(relativePath + '\\' + outputPath,"r")
inputSize = os.fstat(inputFile.fileno()).st_size
outputSize = os.fstat(outputFile.fileno()).st_size
print("Input size: ", end='');
print(inputSize)
print("Output size: ", end='');
print(outputSize)
print(relativePath + '\\' + outputPath)