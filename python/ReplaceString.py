# Searching for something in a string

import re

def main():
    source = "Learning how to use Python"

    # sub will replaces all matches with the string or character specified
    # Replace all letter o's with a ? in the source variable
    result = re.sub('o', '?', source)
    print(result)




if __name__ == "__main__":
    main()
