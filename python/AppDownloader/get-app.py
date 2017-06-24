import sys, configparser
from pathlib import Path
import urllib.request
import os, csv

def main():
    os.system('cls')
    print('Application Downloader')
    config_file = './settings.cfg'
    if checkFileExists(config_file):
        LoadApps(config_file)
    else:
        result = input('Configuration file does not exist. Create it? (y/n): ')
        if result == 'y':
            createConfigFile(config_file)

def checkFileExists(ifile):
    x = os.path.isfile(ifile)
    return x

def createConfigFile(config_file):
    writer = open(config_file, 'w')
    writer.write('[Files]\n')
    writer.write('path = C:\\Users\\Nick\\Desktop\\apps.csv')
    writer.close()
    if checkFileExists(config_file):
        print('Config file created')
        LoadApps(config_file)
    else:
        print('Something went wrong. Unable to continue...')

def LoadApps(config_file):
    cfg = configparser.ConfigParser()
    cfg.read(config_file)
    filePath = cfg['Files']['Path']
    if checkFileExists(filePath):
        OutputFiles(filePath)
    else:
        print('{} is invalid!'.format(filePath))

def OutputFiles(filePath):
    appFile = open(filePath, 'r')
    reader = csv.reader(appFile, delimiter=',')
    appList = dict(reader)
    i = 1
    for key in appList.items():
        print('{}. {}'.format(i, key))
        i+=1

    print('Type q to quit.')

    userInput = input('-> ')
    CheckSelection(appList, userInput, len(appList))
    #while userInput != 'q':
        #menu(appList)

def menu(appList):
    os.system('cls')
    print('Application Downloader')
    i=1
    for key in appList.items():
        print('{}. {}'.format(i, key))
        i+=1
    userInput = input('-> ')
    CheckSelection(appList, userInput, len(appList))

def CheckSelection(appList, userInput, listLength):
    if userInput == 'q':
        print('Exiting...')
    else:
        if (int(userInput) > listLength):
            print('Invalid option!')
            menu(appList)
        else:
            item_to_download = list(appList.values())[int(userInput)-1]
            item_key = list(appList.keys())[int(userInput)-1]
            download(appList, item_to_download, item_key)

def download(appList, fileURL, item_key):
    if os.path.exists('Downloaded Files') == False:
        os.mkdir('Downloaded Files')

    print('Downloading ' + fileURL + '...')
    saveFilename = 'Downloaded Files\\' + item_key + '.exe'
    urllib.request.urlretrieve(fileURL, saveFilename)
    os.system('cls')
    menu(appList)





if __name__ == "__main__":
    main()
