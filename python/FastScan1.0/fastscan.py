#=================================================================
#title           :FastScan
#description     :Scans and outputs CSV rows based on ellipse 
#                 size, geographic locations, frequency ranges
#                 and pulse duration
#author          :CTR1(IW) Nicholas Marriotti
#date            :20170408
#version         :1.1
#usage           :python process.py
#notes           :
#python_version  :2.7 
#==================================================================

import csv, time, sys, threading, time, os
from datetime import datetime
from settings import *

class cSpinner(threading.Thread):
	# DESCRIPTION: 
	# This function is for the loading indiator.
	
    chars = ["Working \\","Working |","Working /","Working -"]
    index = 0
    keeprunning = True 

    def run(self):
        while self.keeprunning:
            self.printing(self.chars[self.index%len(self.chars)])
            time.sleep(0.1)
            self.index +=1

    def printing(self,data):
        sys.stdout.write("\r"+data.__str__())
        sys.stdout.flush()

    def stop(self):
        self.keeprunning = False



def open_csv(filename):
	# DESCRIPTION:
	# This function is opening the input file and is used in the main
	# loop to scan each row.

    with open(filename, "rU") as csvfile:
        csv_data = csv.DictReader(csvfile)
        count = 0
        for row in csv_data:
            yield row




def checkEllipse(input, ELLIPSE_SIZE):
	# DESCRIPTION:
	# Here we are checking to see if the ELLIPSE(input) is not equal to ZERO
	# then check to see if blank and finally check to see if its less than 
	# the ELLIPSE_SIZE value that was passed in in the main loop.
	
	if input is not 0:
		# VALUE IS NOT 0
		if input < ELLIPSE_SIZE:
			# VALUE IS LESS THAN THE ELLIPSE SIZE
			if input is not None:
				#VALUE IS NOT BLANK. SEND TRUE 
				return True
			else:
				# VALUE IS BLANK
				return False
		else:
			# ELLIPSE IS TOO BIG
			return False
	else:
		# VALUE IS 0
		return False

		
		
		
		
def checkLocations(inputLat, inputLon):
	# DESCRIPTION:
	# This function takes in the rows latitude and longitude and first checks
	# to see if the latitude falls within the box range. If it does
	# it will then check the longitude. If that's also in the range then 
	# foundLocation becomes True and the value is returned to the main loop.
	
	# READ IN THE LOCATION BOX ARRAY
	BOX_DICT = GeoLocations()
	
	# USED TO CHECK IF A COORDINATE FALLS IN THE BOX
	foundLocation = False
	
	# LOOP THROUGH KEYS AND VALUES OF THE BOX_DICT ARRAY
	for key, value in BOX_DICT.items():
		# CHECK LATITUDE
		if float(inputLat) <= float(value[0][0]) and float(inputLat) >= float(value[0][2]):
			# CHECK LONGITUDE
			if float(inputLon) >= float(value[0][1]) and float(inputLon) <= float(value[0][3]):
				# COORDINATE IS INSIDE THE BOX
				foundLocation = True
	
	if foundLocation:
		return True
	else:
		return False




def checkRFPD(RF, PD):
	# DESCRIPTION:
	# This function takes in the rows RF and PD values and checks to
	# see if they fall within any of the ranges set in settings.py
	# if they do then True is returned to the main loop
	
	# READ IN THE RF/PD RANGE ARRAY
	RFPD_DICT = RF_AND_PD_RANGES()
	
	# USED TO CHECK IF THE RF AND PD VALUES ARE GOOD
	goodToGo = False
	
	for key, value in RFPD_DICT.items():
		# CHECK VALUES AGAINST RANGES
		# RF
		if float(RF) >= float(value[0][0]) and float(RF) <= float(value[0][1]):
			# RF IS WITHIN THE RANGE
			# PD
			if float(PD) >= float(value[0][2]) and float(PD) <= float(value[0][3]):
				# PD IS ALSO WITHIN THE RANGE
				goodToGo = True
				# EXIT THE LOOP TO PREVENT ANY OTHER RANGE TESTS FROM RETURNING FALSE
				break
	
	if goodToGo:
		return True
	else:
		return False

		

	
def main():

        report_numbers = {}

    # CLEAR THE SCREEN (WINDOWS ONLY)
    os.system('cls')
	
    # SET MAX ELLIPSE SIZE
    ELLIPSE_SIZE = 30
	
	# PRINT HEADER
	print "*****************************************************************************************"
	print "* FastScan v1.0                                                                         *"
	print "* Created by: CTR1(IW) Marriotti - Last Updated: 4/8/2017                               *"
	print "* This script scans csv files searching for specific ellipses and geographic locations. *"
	print "*****************************************************************************************"
	print ""
	
	# GET FILE INFORMATION	
	inputfile = raw_input("Input file: ")
	outfile = raw_input("Outfile: ")

	# GET THE TIME WE STARTED PROCESSING THE ROWS
	before = time.time()
	
	# OPEN THE OUTFILE FILE AND SET TO WRITE MODE
	with open(outfile, 'w') as csvfile:
		
		# TRACK TOTAL ROWS
		count = 0
		
		# TRACK ROWS TO KEEP
		keepCount = 0
		
		# SET CSV COLUMNS
		fields = ['ellipse','lat','lon','RF','PD']
		writer = csv.DictWriter(csvfile, fieldnames=fields, delimiter=',', lineterminator='\n')
		
		# OUTPUT THE CSV HEADER
		writer.writeheader()
		
		print ""
		
		# CREATE LOADING INDICATOR OBJECT
		waitIndicator = cSpinner()
		
		# SHOW INDICATOR
		waitIndicator.start()
		
		# LOOP THROUGH EACH ROW IN THE CSV
		for row in open_csv(inputfile):
			
			# EMPTY ARRAY TO HOLD LAT/LONGS AND RF/PD
			LOC_TEST = []
			RFPD_ARRAY = []
			
			# ASSUME WE WANT TO KEEP EVERY ROW
			RowGood = True
			
            # ADD 1 TO TOTAL ROW COUNT
			count+=1
			
			# CHECK THE ELLIPSE
			if checkEllipse(int(row['ellipse']), ELLIPSE_SIZE):

				# LOAD ARRAY WITH CSV LAT/LONGS
				LOC_TEST.append(row['lat'])
				LOC_TEST.append(row['lon'])
				
				# LOAD ARRAY WITH CSV RF/PD VALUES
				RFPD_ARRAY.append(row['RF'])
				RFPD_ARRAY.append(row['PD'])
				
				# CALL CHECKLOCATIONS FUNCTION AND PASS A LAT/LONG
				if checkLocations(float(LOC_TEST[0]), float(LOC_TEST[1])) is True:
					# THIS COORDINATE IS INSIDE A BOX
					RowGood = True
					# CHECK THE RF AND PD VALUES
					if checkRFPD(float(RFPD_ARRAY[0]), float(RFPD_ARRAY[1])) is True:
						# VALUES LOOK GOOD
						RowGood = True
					else:
						# VALUES DIDN'T FALL WITHIN THE RANGES SPECIFIED
						RowGood = False
				else:
					# COORDINATE DIDN'T FALL INSIDE A BOX
					RowGood = False
			else:
				# BAD ELLIPSE
				RowGood = False

			# IF ROWGOOD IS TRUE
			if RowGood:
                                current_report = report_number.get(row['report_num'], None)
                                if current_report is None:
                                    # This is a new report
                                    print "New Report" + row['report_num']
                                else:
                                    # This is the same report

                                report_number[row['report_num']] = current_report
				# SEND THE ROW TO THE OUTPUT FILE
				writer.writerow(row)
				# INCREMENT KEEP COUNTER
				keepCount+=1

	# GET TIME PROCESS FINISHED
	after = time.time()
	
	# STOP THE LOADING INDICATOR
	waitIndicator.stop()
	
	# PRINT OUT THE RESULTS
	print "\n\n********** RESULTS **********"
	print "Found {rowsKeep} valid rows.".format(rowsKeep=keepCount)
	print "{rows} rows processed in {time:0.2f} seconds".format(rows=count, time=after-before)
	

if __name__ == "__main__":
	main()
