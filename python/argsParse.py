import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', type=str, default='', help='Input file path.')
    parser.add_argument('--o', type=str, default='', help='output file path.')
    args = parser.parse_args()

    print(args.i)
    print(args.o)

