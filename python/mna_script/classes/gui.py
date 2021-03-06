import Tkinter as tk
import tkFileDialog
from classes.gui import *
from classes.kml import *
from classes.row import *
from classes.imputfile import *
from classes.parsefile import *
from classes.stationcheck import *
import time

class Gui(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.grid()
		self.var1 = tk.IntVar(value=1)
		#classification
		self.topclass = tk.Label(self, text="UNCLASSIFIED", font="helvetica 8 bold", bg="green", fg="white").grid(row=0, column=0, sticky='WE')
		
		#title		
		self.master.title("CSV Scanner v1.0")
		
		#input file
		self.entry = tk.Entry(self, text="", width=50, font="helvetica 10")
		self.label2 = tk.Label(self, text="Input file:", font="helvetica 10").grid(row=1, column=0, sticky='W', padx=5)
		self.entry.grid(row=2, column=0, padx=5, pady=5)
		
		#time interval
		self.timelabel = tk.Label(self, text="Time interval (sec):", font="helvetica 10").grid(row=3, column=0, padx=5, sticky='W')
		self.timeentry = tk.Entry(self, text="1.0", width=5, font="helvetica 10")
		self.timeentry.grid(row=5, column=0, padx=5, sticky='W')
		self.timeentry.insert(0, "1.0")
		
		#freq interval
		self.freqlabel = tk.Label(self, text="Frequency interval (MHz):", font="helvetica 10").grid(row=6, column=0, padx=5, sticky='W')
		self.freqentry = tk.Entry(self, text="0.011", width=8, font="helvetica 10")
		self.freqentry.grid(row=7, column=0, padx=5, sticky='W')
		self.freqentry.insert(0, "0.011")
		
		#file dialog
		self.browse = tk.Button(self, text="Browse", font="helvetica 10", command=self.open_file).grid(row=3, column=0, padx=5, sticky='E')
		
		# create kml checkbutton
		self.createKML = tk.Checkbutton(self, text="Create KML", font="helvetica 10", variable=self.var1).grid(row=8, sticky='W')
		
		#start button
		self.button = tk.Button(self, text="Scan File", font="helvetica 10 bold", command=self.start)
		self.button.grid(row=9, column=0, padx=5)
		
		#results
		self.label4 = tk.Label(self, text="Results:", font="helvetica 10").grid(row=10, column=0, sticky='W', padx=5)
		self.T = tk.Text(self, width=50, height=10, font="Courier 10", bg="black", fg="white")
		self.T.grid(row=11, column=0, pady=5, padx=5)
		
		#created by
		self.by = tk.Label(self, text="Created by: CTR1(IW) Nicholas Marriotti", font="helvetica 7").grid(row=12, column=0, padx=5, sticky='W')

	
	def open_file(self):
		self.filename = tkFileDialog.askopenfilename(title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
		self.entry.delete(0, 'end')
		self.entry.insert(0, self.filename)
		
	def start(self):
		timeint = self.timeentry.get()
		freqint = self.freqentry.get()
		
		inputfile = InputFile(self.entry.get())
		if inputfile.CheckFileExtension():
			if self.isNumeric(timeint) and self.isNumeric(freqint):
				#self.T.delete(1.0, 'end')
				#self.T.insert(1.0, "Sorting data...")	
				#self.master.update_idletasks()
				#inputfile.sort(col=0, save=True)  # sort the file
				self.T.insert(1.0, "Checking data, please wait...\n")
				self.master.update_idletasks()
				InitialScan = ParseFile(fileObj=inputfile, timeinterval=float(timeint), freqinterval=float(freqint), gui=True)  # create object to scan the file
				CreateKML = KMLScan(fileObj=inputfile, timeinterval=float(timeint))
				try:  # try to read the file
					InitialScan.run() # process the file
					self.T.insert('end', InitialScan.printResults())  # print the final results
					if self.var1.get() is 1:
						try:
							CreateKML.run()
							self.T.insert('end', "\nKML saved to: {}".format(inputfile.GetKML()))
						except:
							print "Error occurred while creating KML..."
				except:
					#  file is not meant for this script
					self.T.delete(1.0, 'end')
					self.T.insert(1.0, "Input file not formatted properly.")						
			else:
				self.T.delete(1.0, 'end')
				self.T.insert(1.0, "Invalid time/frequency interval.")			
		else:
			self.T.delete(1.0, 'end')
			self.T.insert('end', "Input file must be a .csv")
			
	def isNumeric(self, value):
		try:
			float(value)
			return True
		except:
			return False
		
	
