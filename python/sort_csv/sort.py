#!/usr/bin/python
import operator
import csv

def main():
	f = open('sample.csv', 'r')
	data = csv.reader(f,delimiter=',')
	sortedlist = sorted(data, key=operator.itemgetter(0))
	for eachitem in sortedlist:
		print eachitem
		
	x = [(7,5),(4,2),(8,6)]
	print sorted(x)

if __name__ == "__main__":
	main()
