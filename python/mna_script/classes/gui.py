import Tkinter as tk
from classes.gui import *
from classes.kml import *
from classes.row import *
from classes.imputfile import *
from classes.parsefile import *

class Gui(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.pack()
		self.master.title("CSV Scanner v1.0")
		self.label = tk.Label(self, text="Open a CSV file to begin", font="helvetica 10").pack(pady=10)
		self.entry = tk.Entry(self, text="", width=50, font="helvetica 10")
		self.entry.pack(padx=10)
		self.button = tk.Button(self, text="Start", font="helvetica 12", command=self.start)
		self.button.pack(pady=10, padx=10)
		self.status = tk.Label(self, text="", font="helvetica 8")
		self.status.pack()
	
	def start(self):
		#print self.entry.get()
		inputfile = InputFile(self.entry.get())
		if inputfile.CheckFileExtension():
			inputfile.sort(col=0, save=True)
			run = ParseFile(fileObj=inputfile, timeinterval=1, freqinterval=0.011, gui=True)
			run.run()
			if run.isComplete(): # check if process completed and pass True since using Gui version
				self.status.config(text=run.printResults(), fg="green")				
		else:
			self.status.config(text="Error: input file must be .csv", fg="red")
		
	
