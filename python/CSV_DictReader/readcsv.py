import csv, sys

class NewCSV():

    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        with open(self.filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)

def main():
    try:
        mycsv = NewCSV(sys.argv[1])
        mycsv.read()
    except:
        print("Error reading file.")


if __name__ == "__main__":
    main()