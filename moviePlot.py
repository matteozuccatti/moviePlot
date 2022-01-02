import sys
from lib import *
from classes import OutputFrame
import matplotlib 
from matplotlib import pyplot as plt
matplotlib.use('Agg') 
import cv2
import numpy as np
import time 


def main():
    initialPrint()
    # Instantiate initial elements 
    videoPath,folderName,mod = assertations()
    generateFolder(folderName)

    # Output frame object 
    outputFrame = OutputFrame
    NFrame = countTotalFrames(videoPath)
    cap = cv2.VideoCapture(videoPath)
    savedPlots = countTotalPlots(folderName)

    # Loop over every remaining frame
    for nFrame in range(savedPlots,NFrame,1):
        ret,videoFrame = cap.read()
        if ret:
            cv2.imshow('Video Frame',videoFrame)
            cv2.waitKey(1)
            #generatePlot(videoFrame,folderName,nFrame)
        print(f'nFrame : {nFrame} out of {NFrame}')
    
    
    # Closing operations
    cap.release()
    cv2.destroyAllWindows()

    
    





if(__name__== '__main__'):
    main()


