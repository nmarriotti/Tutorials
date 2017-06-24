def main():
    writer = open("testfile.txt", 'w')
    writer.write("This is sent to the output file.\n")
    writer.close()
    

if __name__ == "__main__":
    main()
