class Kml():
	def __init__(self):
		self.points = []
		
	def addPoint(self, name, description, x, y):
		pt = '''<Placemark>
	<name> NAME </name>
	<description> DESCRIPTION </description>
	<Point>
		<coordinates> LATITUDE, LONGITUDE </coordinates>
	</Point>
</Placemark>'''
		pt = pt.replace("NAME", name).replace("DESCRIPTION", description).replace("LATITUDE",str(x)).replace("LONGITUDE",str(y))
		self.points.append(pt)

	
	def save(self, filename):
		headers = '''<?xml version='1.0' encoding='UTF-8'?>
<kml xmlns='http://earth.google.com/kml/2.1'>
<Document>'''
		with open(filename, "w") as kmlfile:
			kmlfile.write(headers)
			for item in self.points:
				kmlfile.write(item)
			kmlfile.write("</Document>\n</kml>")
