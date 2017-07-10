import math

class Kml():
	def __init__(self):
		self.kml = []
	
	def getLineString(self, coordinates):
		linestring = '''    <Placemark id="track1">
        <name>path</name>
        <styleUrl>#style1</styleUrl>
        <LineString>
        	<tessellate>1</tessellate>
            <coordinates>COORDINATES</coordinates>
        </LineString>
    </Placemark>'''
    
		list_coords = ','.join(map(str, coordinates))
		linestring = linestring.replace("COORDINATES",list_coords)
		#print "Writing LineString for {}".format(coordinates)
		self.kml.append(linestring)
		return linestring

	
	def getPoint(self, name, coordinates):
		point = '''  <Placemark>
    <name>NAME</name>
    <Point>
      <coordinates>COORDINATES</coordinates>
    </Point>
  </Placemark>'''
  		point = point.replace("NAME",str(name)).replace("COORDINATES",coordinates)
		#print "Writing point... for {}".format(coordinates)
		self.kml.append(point)
  		return point

	
	def save(self, filename):
		headers = '''<?xml version='1.0' encoding='UTF-8'?>
<kml xmlns='http://earth.google.com/kml/2.1'>
<Document>
        <Style id="style1"> 
                <LineStyle> 
                        <colorMode>random</colorMode> 
                        <width>2</width> 
                </LineStyle> 
                <PolyStyle> 
                        <color>ff7faa55</color>
                        <colorMode>random</colorMode>
                        <fill>1</fill>
                        <outline>1</outline>
                </PolyStyle> 
        </Style>'''
		with open(filename, "w") as kmlfile:
			kmlfile.write(headers)
			for item in self.kml:
				kmlfile.write(item)
			kmlfile.write("</Document>\n</kml>")
			
	def CreateEllipse(self, lat, lon, smajor, sminor, orient):
		convert = lambda x: x*1852 # meters per nautical mile
		# Values must be in radians
		smajor = convert(smajor) 
		sminor = convert(sminor)
		lat = math.radians(float(lat))
		lon = math.radians(float(lon))
		n = 36  # Number of points to approximate the ellipse. Increase for more precision.
		earth_in_meters = 6378137.0  # Radius of earth in meters
		deg2rad = math.pi/180
		orient = deg2rad*float(orient)
		clat = math.cos(lat)
		slat = math.sin(lat)
		clon = math.cos(lon)
		slon = math.sin(lon)
		cosorient = math.cos(orient)
		sinorient = math.sin(orient)
		ecf1 = earth_in_meters * clat * clon
		ecf2 = earth_in_meters * clat * slon
		ecf3 = earth_in_meters * slat
		points = []
		for i in range(n):
			angle = i*2*math.pi/n
			x0 = smajor * math.cos(angle)
			y0 = sminor * math.sin(angle)
			x = x0 * cosorient + y0 * sinorient
			y = -x0 * sinorient + y0 * cosorient
			xecf1 = -slon * y + clon * slat * x + ecf1
			xecf2 = clon * y + slon * slat * x + ecf2
			xecf3 = -clat * x + ecf3
			sa = math.sqrt(xecf1*xecf1 + xecf2*xecf2)
			xlat = math.atan2(xecf3, sa) / deg2rad
			xlon = math.atan2(xecf2, xecf1) / deg2rad
			points.append("{},{} ".format(xlon, xlat))
		
		#print points
		line = "<Placemark><styleUrl>#style1</styleUrl><Polygon><outerBoundaryIs><LinearRing><coordinates>" + ','.join(map(str, points)) + "</coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark>"
		self.kml.append(line)
		return line
