#!/usr/bin/python3.5.2

def readArguments():
	"""read the argument, and check if the arguments are valid"""
	#read arguments
	import argparse, sys
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--temperature_file", help="file name which stores temperature data", required = True)
	parser.add_argument("-e", "--energy_file", help="file name which stores energy data", required = True)
	parser.add_argument("-o", "--output_file", help="file name which stores the output, default = sys.STDOUT")
	parser.add_argument("-w", "--write", action = "store_true", help = "overwrite the file instead of appending")
	args = parser.parse_args()
	
	#check if arguments are valid
	temperFile = open(args.temperature_file, 'r')
	energyFile = open(args.energy_file, 'r')
	if not args.output_file:
		outputFile = sys.stdout
	elif args.write:
		outputFile = open(args.output_file, 'w')
	else:
		outputFile = open(args.output_file, 'a')
	
	#return the file-tuple
	return (temperFile, energyFile, outputFile)

def readEnergyFile(energyFile):
	"""read the energy file, save in two lists: energyDate and energyWh"""
	import datetime, logging
	logging.basicConfig(format='%(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', 
		filename='summary.log',level=logging.WARNING)

	energyDate = []
	energyWh = []
	hasWarning = False
	
	# check if the title exists
	nextLine = energyFile.readline()
	while nextLine and nextLine != "Date/Time,Energy Produced (Wh)\n":
		nextLine = energyFile.readline()
	assert nextLine, "Energy file has no title line"
	
	# read data
	nextLine = energyFile.readline()
	while nextLine:
		# check if line if empty
		if nextLine == '\n':
			nextLine = energyFile.readline()
			continue
			
		# separate time and Wh
		allInfos = nextLine.strip().split(',')
		
		# summary line
		if allInfos[0] == "Total":
			break
		
		# find time
		timeInfos = allInfos[0].split(' ')

		# find the date and check the date is proper
		dateInfo = datetime.datetime.strptime(timeInfos[0], '%Y-%m-%d').date()
		if len(energyDate) != 0:
			assert dateInfo == energyDate[-1]+datetime.timedelta(days = 1), "Not next day: " + str(dateInfo)
		
		# make sure energy is gathering in midnight and in Wisconsin time zone
		if timeInfos[1] != "00:00:00":
			logging.warning("Energy data does not gather in midnight:" + str(dateInfo))
			hasWarning = True
		if timeInfos[2] != "-0500" or timeInfos[2] == "-0600":
			logging.warning("Not in Wisconsin time zone:" + str(dateInfo))
			hasWarning = True
		
		# store infos in lists
		energyDate.append(dateInfo)
		energyWh.append(int(allInfos[1])/1000.0)
		
		# read next possible line
		nextLine = energyFile.readline()
	
	return (energyDate, energyWh, hasWarning)


def readTemperatureFile(temperFile, outputFile, energyDate, energyWh):
	"""read temparature file and write the output file"""
	import datetime, logging
	logging.basicConfig(format='%(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', 
		filename='summary.log',level=logging.WARNING)
	
	hasWarning = False
	
	# check if the title exists
	nextLine = temperFile.readline()
	while nextLine and nextLine != '"#","Date Time, GMT-05:00","K-Type, °F (LGR S/N: 10679014, SEN S/N: 10679014, LBL: water pipe)"\n':
		if nextLine != '\n':
			outputFile.write(nextLine)
		nextLine = temperFile.readline()
	assert nextLine, "Temperature file has no title line"
	outputFile.write(nextLine.strip())
	
	# read data
	nextLine = temperFile.readline()
	currentDate = None
	energyIndex = 0
	while nextLine:
		if nextLine == '\n':
			nextLine = temperFile.readline()
			continue
		allInfos = nextLine.strip().split(',')
		dateInfo = datetime.datetime.strptime(allInfos[1], '%m/%d/%y %H:%M:%S %p').date()
		if currentDate == None:
			currentDate = dateInfo
		elif dateInfo != currentDate:
			assert dateInfo == currentDate+datetime.timedelta(days = 1), "Not next day:" + str(dateInfo)
			
			while energyIndex < len(energyDate) and dateInfo > energyDate[energyIndex]:
				logging.warning("Unmatched Date from energy file: " + str(energyDate[energyIndex]))
				hasWarning = True
				energyIndex += 1
			
			if energyIndex < len(energyDate) and dateInfo < energyDate[energyIndex]:
				logging.warning("Unmatched Date from temperature file: " + str(currentDate))
				hasWarning = True
			
			if energyIndex < len(energyDate) and dateInfo == energyDate[energyIndex]:
				outputFile.write(str(energyWh[energyIndex]))
				energyIndex += 1
					
			currentDate = dateInfo
		outputFile.write('\n' + nextLine.strip() + ',')		
		nextLine = temperFile.readline()			
	outputFile.write('\n')
	return hasWarning

#main function
def main():
	(temperFile, energyFile, outputFile) = readArguments()
	(energyDate, energyWh, hasWarning) = readEnergyFile(energyFile)
	try:
		hasWarning = hasWarning or readTemperatureFile(temperFile, outputFile, energyDate, energyWh)
		if hasWarning:
			print("Warning pops: check summary.log for more details")
	finally:
		outputFile.close()

#called main function
if __name__ == '__main__':
	main()
