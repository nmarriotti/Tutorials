import zipfile

def main():
    
    try:
        z = zipfile.ZipFile("test.zip", "r")
        z.extractall()
    except:
        print("Error extracting file.")


if __name__ == "__main__":
    main()