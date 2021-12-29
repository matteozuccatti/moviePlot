import os
import pathlib

def generateFolder(folderTitle):
    path = str(pathlib.Path(__file__).parent.absolute()) + "/outputs/" +folderTitle
    if not os.path.exists(path):
        print("Generating folder ", folderTitle)
        os.makedirs(path)
    else: 
        print("Folder ", folderTitle, "already present")

def initialPrint(): 
    print("                       _      _____  _       _   ")
    print("                      (_)    |  __ \| |     | |  ")
    print("  _ __ ___   _____   ___  ___| |__) | | ___ | |_")
    print(" | '_ ` _ \ / _ \ \ / / |/ _ \  ___/| |/ _ \| __|")
    print(" | | | | | | (_) \ V /| |  __/ |    | | (_) | |_ ")
    print(" |_| |_| |_|\___/ \_/ |_|\___|_|    |_|\___/ \__|")
    print("                                                 ")
    