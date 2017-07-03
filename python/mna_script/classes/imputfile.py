import os
import sys
import csv
import operator

class InputFile():
	def __init__(self, inputfile):
		self.fullpath = inputfile
		self.extension = os.path.splitext(inputfile)[1]
		self.outputfile = os.path.splitext(inputfile)[0] + "_parsed.csv"
		self.sorted = os.path.splitext(inputfile)[0] + "_sorted.csv"
		self.length = 0
		
	def GetSortedFile(self):
		return self.sorted
				
	def CheckFileExtension(self):
		if self.extension == ".csv":
			return True
		else:
			print "invalid file type, file must be .csv"
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
		
	def sort(self, col, save):  # sort the file by value of (col) and save to file if (save) is True
		sys.stdout.write("Sorting file...")
		f = open(self.fullpath, 'r')
		data = csv.reader(f,delimiter=',')
		header = next(data)
		sort = sorted(data, key=operator.itemgetter(col))
		
		if save:
			with open(self.sorted, 'w') as outputfile:
				writer = csv.writer(outputfile)
				writer.writerow(header)
				for row in sort:
					writer.writerow(row)
				sys.stdout.write("done\n")
		self.length = float(len(sort))
		
	def getHeaders(self):
		f = open(self.fullpath, 'r')
		data = csv.reader(f,delimiter=',')
		headers = next(data)
		return headers
