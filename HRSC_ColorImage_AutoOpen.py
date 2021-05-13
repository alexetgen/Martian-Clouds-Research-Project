# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:22:57 2020

@author: Alex Etgen
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2



def find_lines(fname):
    file = open(fname, 'rb')
    lines = file.readlines()[:5000]
    file.close()
    
    for line in lines:
      line = line.decode("ascii")
      if "LINES" in line:
          line = str(line)
          line = line.split( )
          return int(line[2])


def find_line_samples(fname):
    file = open(fname, 'rb')
    lines = file.readlines()[:5000]
    file.close() 
    
    for line in lines:
      line = line.decode("ascii")
      if "LINE_SAMPLES" in line:
          line = str(line)
          line = line.split( )
          return int(line[2])


def find_line_prefix(fname):
    file = open(fname, 'rb')
    lines = file.readlines()[:5000]
    file.close() 
    
    for line in lines:
      line = line.decode("ascii")
      if "LINE_PREFIX_BYTES" in line:
          line = str(line)
          line = line.split( )
          return float(line[2])


def find_vmax(fname):
    file = open(fname, 'rb')
    lines = file.readlines()[:5000]
    file.close() 
    
    for line in lines:
      line = line.decode("ascii")
      if "MAXIMUM " in line:
          line = str(line)
          line = line.split( )
          return float(line[2])


def find_vmin(fname):
    file = open(fname, 'rb')
    lines = file.readlines()[:5000]
    file.close() 
    
    for line in lines:
      line = line.decode("ascii")
      if "MINIMUM" in line:
          line = str(line)
          line = line.split( )
          return float(line[2])
      
def find_bytes(fname):
    file = open(fname, 'rb')
    lines = file.readlines()[:5000]
    file.close() 
    
    for line in lines:
      line = line.decode("ascii")
      if "BYTES " in line:
          line = str(line)
          line = line.split( )
          return float(line[2])
      
def radscaling(fname):
    file = open(fname, 'rb')
    lines = file.readlines()[:5000]
    file.close() 
    
    for line in lines:
      line = line.decode("ascii")
      if "RADIANCE_SCALING_FACTOR" in line:
          line = str(line)
          line = line.split( )
          return float(line[2])
      

def radoffset(fname):
    file = open(fname, 'rb')
    lines = file.readlines()[:5000]
    file.close() 
    
    for line in lines:
      line = line.decode("ascii")
      if "RADIANCE_OFFSET" in line:
          line = str(line)
          line = line.split( )
          return float(line[2])

def reflscaling(fname):
    file = open(fname, 'rb')
    lines = file.readlines()[:5000]
    file.close() 
    
    for line in lines:
      line = line.decode("ascii")
      if "REFLECTANCE_SCALING_FACTOR " in line:
          line = str(line)
          line = line.split( )
          return float(line[2])
      
def refloffset(fname):
    file = open(fname, 'rb')
    lines = file.readlines()[:5000]
    file.close() 
    
    for line in lines:
      line = line.decode("ascii")
      if "REFLECTANCE_OFFSET " in line:
          line = str(line)
          line = line.split( )
          return float(line[2])


# read in file into a numpy array and put in right dimensions based on the lines and line samples given by the image header
def read_file(fname):
  dim1=find_lines(fname)
  dim2=find_line_samples(fname)#+int(.5*find_line_prefix(fname))
  infile=open(fname, 'r')
  data=np.fromfile(infile, dtype=np.dtype('>u1'))
  infile.close()
  print(len(data))
  print(dim1*dim2)
  headerend = (len(data)-(dim1*dim2))
  print(headerend)
  data=data[headerend:headerend + (dim1*dim2)].reshape(dim1, dim2)
  return data


#open individual color channels with their corresponding color map
def mainR(fname):
  plt.imshow(read_file(fname), cmap= "Reds", vmax=int(find_vmax(fname)), vmin=int(find_vmin(fname))) 
  #plt.colorbar()
  #plt.show()
  
def mainB(fname):
  plt.imshow(read_file(fname), cmap= "Blues", vmax=int(find_vmax(fname)), vmin=int(find_vmin(fname))) 
  
def mainG(fname):
  plt.imshow(read_file(fname), cmap= "Greens", vmax=int(find_vmax(fname)), vmin=int(find_vmin(fname)))

#transpose 3 color channel images into a color image
def color(fnameR, fnameG, fnameB):
    dataR = read_file(fnameR)
    print(dataR.shape)
    
    dataG = read_file(fnameG)
    print(dataG.shape)
    
    dataB = read_file(fnameB)
    print(dataB.shape)
    
    overallmaxR = find_vmax(fnameR)
    #print(len(np.where(dataR>overallmaxR))[0])
    #print(np.where(dataR>overallmaxR), dataR, 0)
    overallmaxG = find_vmax(fnameG)
    overallmaxB = find_vmax(fnameB)
    print(np.array([dataR/overallmaxR,dataG/overallmaxG, dataB/overallmaxB]).shape)
    print((np.transpose(np.array([dataR/overallmaxR,dataG/overallmaxG, dataB/overallmaxB]))).shape)
    
    fig = plt.figure(1, figsize=(5, 50))
    ax = fig.add_axes([0,0,1,1])
    ax.axis('off')
   # composite = np.transpose(np.array([((dataR/overallmaxR)),((dataG/overallmaxG)), ((dataB/overallmaxB))]), axes=(1,2,0))
    composite = np.transpose(np.array([((dataR)),((dataG)), ((dataB))]), axes=(1,2,0)) #Data_noAlt
   # composite = np.transpose(np.array([((dataR*radscaling(fnameR))-radoffset(fnameR)),((dataG*radscaling(fnameG))-radoffset(fnameG)), ((dataB*radscaling(fnameB))-radoffset(fnameB))]), axes=(1,2,0))
    plt.imshow(composite)
    plt.savefig("ColorImages\\5562.png", bbox_inches = 'tight', dpi = None)
    
fnameR = "Clouds\\h5562_0000_re3.img"
fnameG = "Clouds\\h5562_0000_gr3.img"
fnameB = "Clouds\\h5562_0000_bl3.img"

 #   plt.figure(2, figsize=(5, 50))
   # ax = fig.add_axes([0,0,1,1])
 #   ax.axis('off')
 #   #plt.figure(figsize=(6, 19))
 #   main(fnameB)
 #   plt.savefig("BlueChannel.png", bbox_inches = 'tight')
    


color(fnameR, fnameG, fnameB)


def subtractions(fnameR, fnameB):
    
    fig = plt.figure(1, figsize=(5, 50))
    ax = fig.add_axes([0,0,1,1])
    ax.axis('off')
    mainR(fnameR)
    plt.savefig("WorkingFiles/RedChannel.png", bbox_inches = 'tight')
    
    fig = plt.figure(1, figsize=(5, 50))
    ax = fig.add_axes([0,0,1,1])
    ax.axis('off')
    mainB(fnameB)
    plt.savefig("WorkingFiles/BlueChannel.png", bbox_inches = 'tight')
    
    img_R = cv2.imread('WorkingFiles/RedChannel.png',0)
    img_B = cv2.imread('WorkingFiles/BlueChannel.png',0)
    
    Subtracted = img_B-img_R
    
    cv2.imshow('Subtracted',Subtracted)
    cv2.imwrite("DifferenceImages/1076B_R.jpg", Subtracted)
    
    Subtracted2 = img_R-img_B
    
    cv2.imshow('Subtracted',Subtracted2)
    cv2.imwrite("DifferenceImages/1076R_B.jpg", Subtracted2)

#subtractions(fnameR, fnameB)