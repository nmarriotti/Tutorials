################################################################################
# TITLE:       Error Handling in Python
# DESCRIPTION: How to detect and output errors to the user
################################################################################
# A try statement will TRY to run the code inside. 
# If it encounters an error it will run what is in the EXCEPT block.

def main():
    # Call the openFile method and pass it Files/file1.txt
    openFile('file2.txt')
    print('Done reading the file.')

def openFile(filename):
    try:
        # Create variable and set it to the contents of the file
        fh = open(filename)
        # Output each line in the file
        for line in fh:
            print(line.strip())
    except FileNotFoundError:
        print('Unable to locate file specified: ' + filename)

if __name__ == "__main__": 
    main()
