import Tkinter as tk
import tkFileDialog
from classes.gui import *
from classes.kml import *
from classes.row import *
from classes.imputfile import *
from classes.parsefile import *
import time

class Gui(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.grid()
		self.master.title("CSV Scanner v1.0")
		self.entry = tk.Entry(self, text="", width=50, font="helvetica 10")
		self.label2 = tk.Label(self, text="Input file:", font="helvetica 10").grid(row=0, column=0, sticky='W', padx=5)
		self.entry.grid(row=1, column=0, padx=5, pady=5)
		self.browse = tk.Button(self, text="Browse", font="helvetica 10", command=self.open_file).grid(row=1, column=1, padx=5)
		self.label3 = tk.Label(self, text="Output file:", font="helvetica 10").grid(row=2, column=0, sticky='W', padx=5)
		self.output = tk.Entry(self, text="", width=50, font="helvetica 10")
		self.output.grid(row=3, column=0, padx=5, pady=5)
		self.button = tk.Button(self, text="Start", font="helvetica 10", command=self.start)
		self.button.grid(row=4, column=0, pady=10)
		self.status = tk.Label(self, text="", font="helvetica 10")
		self.status.grid(row=5, column=0, pady=10)
	
	def open_file(self):
		self.filename = tkFileDialog.askopenfilename(title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
		self.entry.delete(0, 'end')
		self.entry.insert(0, self.filename)
		
	def start(self):
		inputfile = InputFile(self.entry.get())
		if inputfile.CheckFileExtension():
			inputfile.sort(col=0, save=True)
			run = ParseFile(fileObj=inputfile, timeinterval=1, freqinterval=0.011, gui=True)
			run.run()
			self.status.config(text=run.printResults(), fg="green")
			self.output.delete(0, 'end')
			self.output.insert(0, inputfile.GetOutputFile())
		else:
			self.status.config(text="Error: input file must be .csv", fg="red")
		
	
