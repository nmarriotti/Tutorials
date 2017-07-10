import time
import sys
import datetime as dt
import csv
from classes.row import *

class ParseFile():
	# Initializer
	def __init__(self, fileObj, timeinterval, freqinterval, gui):
		self.master = []
		self.printlist = []
		self.total = 0
		self.allrows = 0
		self.discard = 0
		self.startTime = time.time()
		self.stopTime = None
		self.timeint = timeinterval
		self.freqint = freqinterval
		self.gui = gui
		self.message = None
		self.fileObj = fileObj
	
	def isComplete(self):
		if self.gui is True:
			return True
		else:
			return False
			
	# Print out the final results
	def printResults(self):
		if not self.gui:
			print "\a\nResults:\n\tTime elapsed: {:0.2f} seconds\n\tFound: {}/{} ({:0.2f}%)\n\tDiscarded: {}".format(time.time()-self.startTime, self.total, self.allrows, float(self.total)/float(self.allrows)*100.0, self.discard)
		else:
			return "Completed in {:0.2f} seconds. \nFound: {}/{} ({:0.2f}%) and Discarded: {}\nOutput saved to: {}".format(time.time()-self.startTime, self.total, self.allrows, float(self.total)/float(self.allrows)*100.0, self.discard, self.fileObj.GetOutputFile())
	
	# Start processing the file	
	def run(self):
		print "Checking data, please wait..."
		for row in self.fileObj.open(self.fileObj.GetFullFilePath()):  # loop through each row in file
			#print row
			self.allrows +=1  # count the rows
			try:
				NewRow = Row(row)  # create row object
			except:
				if not self.gui:
					print "Input file not formatted properly"
					print "Exiting"
					sys.exit(1)
			if not NewRow.isNull():  # check if row is missing data
				self.master.append(NewRow)  # add row to list
			else:
				self.discard += 1  # row was missing data
				continue  # keep looping
			
			if len(self.master) == 2:  # We got two rows
				self.master, self.printlist, self.total = self.CheckRows(self.master, self.printlist, self.total)  # Compare the two rows
			
		if self.CheckReadyToPrint(self.printlist, self.fileObj.GetOutputFile(), self.fileObj.getHeaders()):  # Check if there's something to print
			self.printRows(self.printlist, self.fileObj.GetOutputFile(), self.fileObj.getHeaders())  # Print the rows
			print "\nOutput saved to: \n\t{}".format(self.fileObj.GetOutputFile())  # display output file path
			self.printResults() # print the final results
		else:
			print "NO RESULTS FOUND"
		#self.fileObj.cleanUp()

	# Check two rows
	def CheckRows(self, master, printlist, total):
		if master[0].get_src() == master[1].get_src():  # Source fields match
			if master[0].get_dst() == master[1].get_dst():  # Dest fields match			
				if self.ValidTimeDifference(master[0].get_toi(), master[1].get_toi()):  # Time is within given interval
					if self.ValidFreq(master[0].get_freq(), master[1].get_freq()):  # Frequency is within given interval
						if not master[0].get_row() in printlist:   # prevent duplicates
							printlist.append(master[0].get_row())  # add matching row to list
							total += 1
						if not master[1].get_row() in printlist:   # prevent duplicates
							printlist.append(master[1].get_row())  # add second matching row to list
							total += 1
		del master[0]
		return master, printlist, total		
	
	# Print output to file
	def printRows(self, printlist, outputfile, headers):
		with open(outputfile, 'wb') as outfile:
			writer = csv.DictWriter(outfile, fieldnames=headers)
			writer.writeheader()
			#print "printlist:"
			#print printlist
			for row in printlist:
				writer.writerow(row)
		printlist = []
		
	# Check if there's anything to print
	def CheckReadyToPrint(self, printlist, outputfile, headers):
		if len(printlist) >= 1: # there's at least one row to print
			return True
		else:
			return False

	# Check is time falls within the time interval
	def ValidTimeDifference(self, x, y):
		a = dt.datetime.strptime(str(x), '%m/%d/%Y %H:%M:%S')
		b = dt.datetime.strptime(str(y), '%m/%d/%Y %H:%M:%S')
		if abs((a-b).total_seconds()) <= self.timeint:
			return True
		else:
			return False

	# Check if the frequency falls within the freq interval	
	def ValidFreq(self, x, y):
		if abs(y-x) > self.freqint:
			return True
		else:
			return False
		
	
