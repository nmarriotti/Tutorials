def GeoLocations():
	# BOX INFORMATIOn
	# Update this file with the TOPLEFT and BOTTOMRIGHT lat/longs
	# to define a box.
    BOX_DICT = { 
		#AREANAME:[[TOPLEFT_LAT, TOPLEFT_LON, BOTTOMRIGHT_LAT, BOTTOMRIGHT_LON]]
	    "FLORIDA":[[31.062,-87.527,25.135,-79.830]],
	       "OHIO":[[41.753,-84.809,38.542,-80.617]],
	     "KANSAS":[[39.989,-102.063,36.966,-94.622]],
	 "WASHINGTON":[[48.996,-125.145,45.951,-116.905]]
	}
	# SEND THIS ARRAY TO THE MAIN SCRIPT	
    return BOX_DICT
	
def RF_AND_PD_RANGES():
	RFPD_DICT = {
		#"NAME":[[RF_MIN, RF_MAX, PD_MIN, PD_MAX]]
		"TEST1":[[0,1000,3000,4000]],
		"TEST2":[[4000,5000,6000,7000]]
	}
	# SEND THIS ARRAY TO THE MAIN SCRIPT
	return RFPD_DICT