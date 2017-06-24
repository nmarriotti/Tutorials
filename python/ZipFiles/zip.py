import zipfile

def main():
    
    z = zipfile.ZipFile("test.zip", "w")


    try:
        z.write("readme.txt")
    except:
        print("File doesn't exist.")
    finally:
        z.close()


if __name__ == "__main__":
    main()