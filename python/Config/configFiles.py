# Searching for something in a string

import configparser

def main():

    config_file = 'settings.cfg'
    checkFileExists(config_file)

def checkFileExists(input):
    if input.is_file():
        print('True')




if __name__ == "__main__":
    main()
