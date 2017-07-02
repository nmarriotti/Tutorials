#!/usr/bin/python
import csv

def main():
	f = open('sample.csv', 'r')
	data = csv.reader(f, delimiter=',')
	for eachline in data:
		print eachline

if __name__ == "__main__":
	main()
