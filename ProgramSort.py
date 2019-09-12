fileIn = 'unsorted-names-list.txt'
dataReverse = [] #declare array

#Read and convert
with open(fileIn,'r') as fIn:
	lines = fIn.readlines()
	for noLine in range(0, len(lines)):
		linesBreak = lines[noLine].replace("\n","")
		linesBreak = linesBreak.split(" ")
		dataReverseBreak = linesBreak[::-1]
		dataReverseLines = " ".join(dataReverseBreak)
		dataReverse.append ( dataReverseLines ) 

# SortData
dataReverse.sort()

# Write 
fileOutput = open('sorted-names-list.txt', "w") #write file
for noLine in range(0, len(dataReverse)):
	dataReverseBreak = dataReverse[noLine].split(" ")	
	linesBreak = dataReverseBreak[::-1]
	lines =  ( " ".join(linesBreak))
	fileOutput.write(lines)
	print(lines)
	fileOutput.write("\n")
fileOutput.close()
