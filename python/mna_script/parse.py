#!/usr/bin/python
# Description: Script to parse csv rows that match certain criteria
# Created by: CTR1 Marriotti
# Date: 06/29/2017

import argparse
import os
import sys
import time
import csv
import datetime as dt
import tempfile
import operator
import threading

class WaitIndicator(threading.Thread):
	keepRunning = True
	
	def run(self):
		while self.keepRunning:
			time.sleep(0.1)

	def printing(self, data):
		sys.stdout.write("\r"+data.__str__())
		sys.stdout.flush()

	def stop(self):
		self.keepRunning = False


class Row():
	def __init__(self, row):
		self.row = row
		self.toi = row['dtoi']
		self.src = row['src']
		self.dst = row['dst']
		self.freq = row['freq']
		
	def isNull(self):
		if self.toi is "" or self.src is "" or self.dst is "" or self.freq is "":
			return True
		else:
			return False
		
	def get_toi(self):
		return self.toi
	
	def get_row(self):
		return self.row
		
	def get_src(self):
		return self.src
		
	def get_dst(self):
		return self.dst
		
	def get_freq(self):
		return float(self.freq)
		
	def checkRowsMatch(self, x, y):
		if x == y:
			return True
		else:
			return False
	

class InputFile():
	def __init__(self, inputfile):
		self.fullpath = inputfile
		self.extension = os.path.splitext(inputfile)[1]
		self.outputfile = os.path.splitext(inputfile)[0] + "_parsed.csv"
		self.sorted = os.path.splitext(inputfile)[0] + "_sorted.csv"
		
	def GetSortedFile(self):
		return self.sorted
				
	def CheckFileExtension(self):
		if self.extension == ".csv":
			return True
		else:
			return False
			
	def GetFileExtension(self):
		return self.extension
		
	def GetFullFilePath(self):
		return self.fullpath
		
	def open(self, file_to_open):
		with open(file_to_open, "rU") as csvfile:
			csv_data = csv.DictReader(csvfile)
			for row in csv_data:
				yield row
				
	def printrow(self):
		for row in self.open():
			print row
				
	def GetOutputFile(self):
		return self.outputfile
		
	def cleanUp(self):
		os.remove(self.sorted)


def exit_script():
	print "Exiting..."
	time.sleep(2)
	sys.exit(1)	


def sort(inputfile, tmp, col):
	sys.stdout.write("Sorting file...")
	myfile = open(inputfile, 'r')
	csv_data = csv.reader(myfile,delimiter=',')
	header = next(csv_data)
	sort = sorted(csv_data, key=operator.itemgetter(0))
	with open(tmp, 'w') as outputfile:
		writer = csv.writer(outputfile)
		writer.writerow(header)
		for row in sort:
			writer.writerow(row)
	sys.stdout.flush()
	sys.stdout.write("done")
	return float(len(sort))


fields = ['dtoi','src','dst','freq']
check = True
parser = argparse.ArgumentParser(description="This script parses csv rows that match certain criteria.")
parser.add_argument("-input", type=str, help="input file to parse")
parser.add_argument("-timeinterval", type=int, default=1, help="time interval, default 1.0 sec")
parser.add_argument("-freqinterval", type=float, default=.01, help="frequency interval, default .01")

args = parser.parse_args()  # set arguments

if args.input is None:  # input file was not supplied
	print "input file not found!"
	check = False
	exit_script()

# arguments were found, process file		
if check:
	input_file = InputFile(args.input)  # create input file object
	if not input_file.CheckFileExtension():  # file extension is not .csv
		print "invalid file type, file must be .csv"
		exit_script()


def ValidTimeDifference(x, y):
	a = dt.datetime.strptime(str(x), '%m/%d/%Y %H:%M:%S')
	b = dt.datetime.strptime(str(y), '%m/%d/%Y %H:%M:%S')
	if abs((b-a).total_seconds()) <= args.timeinterval:
		return True
	else:
		return False

		
def ValidFreq(x, y):
	if abs(x-y) <= args.freqinterval:
		return True
	else:
		return False

	
def Process(master, printlist, total):
	if master[0].get_src() == master[1].get_src():
		if ValidTimeDifference(master[0].get_toi(), master[1].get_toi()):
			if ValidFreq(master[0].get_freq(), master[1].get_freq()):
				if not master[0].get_row() in printlist:   # prevent duplicates
					printlist.append(master[0].get_row())  # add matching row to list
					total += 1
				if not master[1].get_row() in printlist:   # prevent duplicates
					printlist.append(master[1].get_row())  # add second matching row to list
					total += 1
	del master[0]
	return master, printlist, total


def CheckReadyToPrint(printlist, outputfile):
	if len(printlist) >= 2:
		printRows(printlist, outputfile)


def printRows(printlist, outputfile):
	with open(outputfile, 'wb') as outfile:
		writer = csv.DictWriter(outfile, fieldnames=fields)
		writer.writeheader()
		for row in printlist:
			writer.writerow(row)
	printlist = []
	return printlist

							
def main():
	length = sort(input_file.GetFullFilePath(), input_file.GetSortedFile(), 1)
	
	master = []
	printlist = []
	total = 0
	allrows = 0
	discard = 0
	
	ProgressStatus = WaitIndicator()  # create progress object
	ProgressStatus.start()
	start = time.time()  # time process started
	
	for row in input_file.open(input_file.GetSortedFile()):
		allrows += 1
		primary = Row(row)
		if not primary.isNull():
			master.append(primary)
		else:
			discard += 1  # required data is missing
			continue
			
		if len(master) is 2:
			master, printlist, total = Process(master, printlist, total)
			CheckReadyToPrint(printlist, input_file.GetOutputFile())
		if allrows % 2:
			ProgressStatus.printing("Checking data...{:0.1f}%".format(float(allrows)/float(length)*100))
	
	
	input_file.cleanUp()  # delete sorted file
	ProgressStatus.printing("\n\aTask completed in {:0.4f} seconds".format(time.time()-start))
	print "\nResults: {:0.4f}% of rows kept ({}/{}) with {} discarded due to missing data".format(float(total)/float(allrows)*100.0, total, allrows, discard)
	
	ProgressStatus.stop()  # stop progress bar

if __name__ == "__main__":
	main()
	

