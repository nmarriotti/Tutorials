#!/usr/bin/python
import argparse

def main():
    parser = argparse.ArgumentParser(description='This is the description')
    parser.add_argument('-i', '--input', type=str, help='Input file')
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='Output file')
    parser.add_argument('-b', '--birthyear', type=int, help='Birth year')

    args = parser.parse_args()
    
    print args 		 # print all arguments out
    print args.output	 # print output
    print args.birthyear # print birthyear   

    ofile = open(args.output, 'w')
    ofile.write("{}\n".format(args.birthyear))
    ofile.close()

if __name__ == "__main__":
    main()
