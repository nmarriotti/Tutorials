import math

def CreateEllipse(lat, lon, smajor, sminor, orient):
	# Values must be in radians
	smajor = math.radians(smajor)
	sminor = math.radians(sminor)
	lat = math.radians(lat)
	lon = math.radians(lon)
	n = 36  # Number of points to approximate the ellipse. Increase for more precision.
	earth_in_meters = 6378137.0  # Radius of earth in meters
	deg2rad = math.pi/180
	orient = deg2rad*orient
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
	return "<Polygon><outerBoundaryIs><LinearRing><coordinates>" + ','.join(map(str, points)) + "</coordinates></LinearRing></outerBoundaryIs></Polygon>"
