import math

class Row():
	def __init__(self, row):
		self.row = row
		self.toi = row['dtoi']
		self.src = row['src']
		self.dst = row['dst']
		self.freq = row['freq']
		self.colorcode = row['colorcode']
		self.station = row['station']
		self.lat = row['lat']
		self.long = row['long']
		self.smajor = row['smajor']
		self.sminor = row['sminor']
		self.orient = row['orient']
		
	def isNull(self):
		if self.toi is "" or self.src is "" or self.dst is "" or self.freq is "":
			return True
		else:
			return False
		
	def get_toi(self):
		return self.toi
	
	def get_smajor(self):
		return float(self.smajor)
		
	def get_sminor(self):
		return float(self.sminor)
		
	def get_orient(self):
		return self.orient

	def get_row(self):
		return self.row
		
	def get_src(self):
		return self.src
		
	def get_lat(self):
		return self.lat

	def get_long(self):
		return self.long
		
	def get_dst(self):
		return self.dst
		
	def get_freq(self):
		return float(self.freq)
		
	def get_colorcode(self):
		return self.colorcode
		
	def get_station(self):
		return self.station
		
	def get_coordinates(self):
		return "{},{}".format(self.long, self.lat)
		
	def checkRowsMatch(self, x, y):
		if x == y:
			return True
		else:
			return False
