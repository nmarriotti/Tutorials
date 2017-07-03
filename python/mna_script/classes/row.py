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
