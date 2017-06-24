# Searching for something in a string

import re

def main():
    source = "Learning how to use Python"

    # match will look for characters starting at the beginning of the string
    result = re.match('Learn', source)
    if result:
        print(result.group())

    # search will look for characters that match anywhere in the string
    result = re.search('se', source)
    if result:
        print(result.group())

    # fina all occurences of characters
    result = re.findall('ho', source)
    if result:
        print('Found {} matches'.format(len(result)))




if __name__ == "__main__":
    main()
