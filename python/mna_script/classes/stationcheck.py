import time
import sys
import datetime as dt
import csv
from classes.row import *
from classes.kml import *

class KMLScan():
			
	def __init__(self, fileObj, timeinterval):
		self.fileObj = fileObj # inputfile object
		self.timeint = timeinterval
		self.master = [] # hold row objects
		self.coordinate_list = [] # used for creating LineStrings
		self.KML = Kml()  # create kml object

	def run(self):
		nextIsTheSame = False
		for row in self.fileObj.open(self.fileObj.GetOutputFile()):
			#print row
			NewRow = Row(row)
			self.master.append(NewRow)
			
			if len(self.master) is 2: # Got two rows
				self.master, nextIsTheSame = self.CheckRows(self.master)
				
			if not nextIsTheSame and len(self.coordinate_list) > 0:
				# Print out the results
				self.KML.getLineString(self.coordinate_list) # create LineString
				self.coordinate_list = []
				nextIsTheSame = False
				
		self.KML.getLineString(self.coordinate_list)  # reached end of file, print the final coordinates
		self.coordinate_list = []		
		
		self.KML.save(self.fileObj.GetKML()) # save the kml file
		print "\tKML saved as {}".format(self.fileObj.GetKML())
				
	def CheckRows(self, master):
		isSame = False  # Used to tell the main loop if it should print the coordinates or not
		priRow = master[0]
		nextRow = master[1]
		
		if self.ValidTimeDifference(priRow.get_toi(), nextRow.get_toi(), self.timeint):
			#print "Times are valid"
			if self.isSame(priRow.get_src(), nextRow.get_src()):  # check if rows have the same source
				if self.isSame(priRow.get_dst(), nextRow.get_dst()):  # check if rows have same destination
					# add first row coordinates
					#print "Adding coordinates to list"
					coordinate = "{}{} ".format(priRow.get_coordinates(),",0")
					if coordinate not in self.coordinate_list:
						self.KML.getPoint(priRow.get_freq(), coordinate) # create LineString
						self.KML.CreateEllipse(priRow.get_lat(), priRow.get_long(), priRow.get_smajor(), priRow.get_sminor(), priRow.get_orient()) # create ellipse
						self.coordinate_list.append(coordinate)  # add lat/long with 0 for altitude
					#if self.isBase(priRow.get_station()):
						#print "Found a BS"
					# add second row coordinates
					coordinate = "{}{} ".format(nextRow.get_coordinates(),",0")
					if coordinate not in self.coordinate_list:
						self.KML.getPoint(nextRow.get_freq(), coordinate) # create LineString
						self.KML.CreateEllipse(nextRow.get_lat(), nextRow.get_long(), nextRow.get_smajor(), nextRow.get_sminor(), nextRow.get_orient()) # create ellipse
						self.coordinate_list.append(coordinate)  # add lat/long with 0 for altitude
					#if self.isBase(nextRow.get_station()):
						#print "Found a BS"	
					isSame = True
				else:
					isSame = False
			else:
				isSame = False
		else:
			isSame = False
					
		del master[0]
		return master, isSame

			

	def ValidTimeDifference(self, x, y, interval):  # Check is time falls within the time interval
		a = dt.datetime.strptime(str(x), '%m/%d/%Y %H:%M:%S')
		b = dt.datetime.strptime(str(y), '%m/%d/%Y %H:%M:%S')
		if abs((b-a).total_seconds()) <= interval:
			return True
		else:
			return False
			
	def isBase(self, station):  # check station type
		if "B" in station:
			return True
		else:
			return False
	
	def isSame(self, x, y):  # Check if values are the same
		if x is y:
			return True
		else:
			return False