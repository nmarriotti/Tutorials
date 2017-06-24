################################################################################
# TITLE:       Reading files in Python
# DESCRIPTION: Open a text file and read the contents of it.
################################################################################


def main():

    try: 
        fh = open("test.txt", "r")
        for line in fh:
            print(line.strip())
    except:
        print("Unable to open file.")

if __name__ == "__main__":
    # Here we start the program by calling the main method
    main()
