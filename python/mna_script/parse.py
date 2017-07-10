#!/usr/bin/python
# Description: Script to parse csv rows that match certain criteria using both CLI and GUI
# Created by: CTR1 Marriotti
# Date: 06/29/2017

import argparse
import sys
from classes.gui import *
from classes.imputfile import *
from classes.parsefile import *
from classes.stationcheck import *
				

# Exit the script
def exit_script():
	print "Exiting..."
	time.sleep(2)
	sys.exit(1)	


# Main method		
def main():
	print "CSV Scanner v1.0 - Developed by CTR1(IW) Nicholas Marriotti"
	parser = argparse.ArgumentParser(description="This script checks csv rows that match certain criteria.\nIf no arguments are supplied GUI will be used.")
	parser.add_argument("-input", type=str, help="input file to parse")
	parser.add_argument("-timeinterval", type=float, default=1.0, help="time interval, default 1.0 sec")
	parser.add_argument("-freqinterval", type=float, default=0.011, help="frequency interval, default .011")

	args = parser.parse_args()  # set arguments

	if args.input is None:  # input file was not supplied
		# run GUI version
		print "Running GUI version."
		root = tk.Tk()
		root.resizable(width=False, height=False)
		app = Gui(root)
		app.mainloop()
	else:
		# run command-line version
		print "Running CLI version."
		input_file = InputFile(args.input)  # create input file object
		if not input_file.CheckFileExtension():  # file extension is not .csv
			exit_script()
		# Process file 
		#input_file.sort(col=0, save=True)
		run = ParseFile(fileObj=input_file, timeinterval=args.timeinterval, freqinterval=args.freqinterval, gui=False)
		run.run()
		run = KMLScan(fileObj=input_file, timeinterval=args.timeinterval)
		run.run()
	

if __name__ == "__main__":
	main()
