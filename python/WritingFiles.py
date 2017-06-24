################################################################################
# TITLE:       Writing to Files in Python
# DESCRIPTION: How to detect and output errors to the user
################################################################################

def main():
    # Call the openFile method and pass it Files/file1.txt
    outputFile = input('Save as: ')
    try:
        writeFile(outputFile)
    except:
        print('Something is wrong with the filename you provided!')


def writeFile(filename):
        writer = open(filename, 'w')

        i=1

        while i<=5:
            writer.write('This is line {}\n'.format(i))  #\n means newline
            i+=1
 
        writer.close()
        print('File created successfully!')




if __name__ == "__main__": 
    main()
