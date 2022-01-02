import os
import sys
import pathlib
import cv2
from matplotlib import pyplot as plt
import matplotlib  
matplotlib.use('Agg')
import numpy as np

def assertations():
    if not os.path.exists(str(pathlib.Path(__file__).parent.absolute()) + "/movieClips"):
        os.makedirs(str(pathlib.Path(__file__).parent.absolute()) + "/movieClips")
    assert len(sys.argv) > 2, "** ERROR ** : not enough arguments have been passed"
    nameScript, videoPath, folderName, mod = (arg for arg in sys.argv) 
    videoPath =  str(pathlib.Path(__file__).parent.absolute()) + "/" + videoPath
    assert os.path.exists(videoPath), str( "** ERROR ** :"+ videoPath +"does not exist")
    return (videoPath,folderName,mod)

def generateFolder(folderTitle):
    path = str(pathlib.Path(__file__).parent.absolute()) + "/outputs/" +folderTitle
    if not os.path.exists(path):
        print("Generating folder ", folderTitle)
        os.makedirs(path)
        os.makedirs(str(path+"/frames"))
    else: 
        print("Folder '", folderTitle, "' already present")

def initialPrint(): 
    print("                       _      _____  _       _   ")
    print("                      (_)    |  __ \| |     | |  ")
    print("  _ __ ___   _____   ___  ___| |__) | | ___ | |_")
    print(" | '_ ` _ \ / _ \ \ / / |/ _ \  ___/| |/ _ \| __|")
    print(" | | | | | | (_) \ V /| |  __/ |    | | (_) | |_ ")
    print(" |_| |_| |_|\___/ \_/ |_|\___|_|    |_|\___/ \__|")
    print("                                                 ")

def resizeMovieFrame():
    print("hello")

def countTotalFrames(videoPath): 
    cap = cv2.VideoCapture(videoPath)
    nFrames = 0 
    while (1):
        ret,_ = cap.read()
        if not ret:
            break
        nFrames = nFrames+1 
    return nFrames

def countTotalPlots(folderTitle):
    path = str(pathlib.Path(__file__).parent.absolute()) + "/outputs/" +folderTitle + "/frames/" 
    return  len(os.listdir(path))

def generatePlot(videoFrame, folderTitle, nFrame):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    hFrame,wFrame,_ = videoFrame.shape
    deltaH = int(hFrame/10)
    deltaW = int(wFrame/10)
    w,h = (0,0)
    while(h<hFrame):
        while(w<wFrame):
            c = np.array([
                videoFrame[h,w,2]/255.0,
                videoFrame[h,w,1]/255.0,
                videoFrame[h,w,0]/255.0])
            ax.scatter(videoFrame[h,w,0],
                       videoFrame[h,w,1],
                       videoFrame[h,w,2],
                       color = c,
                       s=2,marker='.')
            w = w+deltaW
        h = h+deltaH
        w = 0
    ax.scatter(255,0,0, color=[1,1,1])
    ax.scatter(0,255,0, color=[1,1,1])
    ax.scatter(0,0,255, color=[1,1,1])
    filename = str(pathlib.Path(__file__).parent.absolute()) + "/outputs/" +folderTitle + "/frames/" 
    filename = filename + "F_" + str(nFrame) + ".png"
    # Save 
    plt.tight_layout()
    #plt.savefig(fname=filename)
    plt.gca()
    plt.close(fig)
