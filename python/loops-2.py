def main():
    myList = [1,2,3,4,5,6,7,8,9,10]
    for item in myList:
        print item


    count = 0
    while count < len(myList):
        print myList[count]
        count += 1

if __name__ == "__main__":
    main()
