import board 
import busio 
import adafruit_mpu6050 
import numpy as np
import csv
import time


from time import sleep, perf_counter 
 
i2c = busio.I2C(board.SCL, board.SDA) 
mpu = adafruit_mpu6050.MPU6050(i2c) 

#Step has occured (awaiting drop in acceleration)
primed = False

#Counts Steps
numSteps = 0

#Keeps track of steps
averageMag = []
firstStep = True
restingAc = 0

#current average from the rolling average
curAvg = 0

while True:
    #raw data collection
    rawData = mpu.gyro
    rawDataX = rawData[0]
    rawDataY = rawData[1]
    rawDataZ = rawData[2]

    #insert into list for rolling average (pushes back the rest of points)
    averageMag.insert(0,curAc)
    
    #reocrd the resting acceleration
    if firstStep:
      restingAc = curAc
      firstStep = False
      continue
    
    #50 points per average
    if len(averageMag) == 50:
      curAvg = np.average(averageMag)
    
      #Step was taken awaiting next step (Falling acceleration)
      if primed and curAvg - restingAc <= 1 :
        primed = False
    
      #Step taken (Rising acceleration)
      if not primed and curAvg - restingAc >= 3 :
        numSteps += 1
        print('Steps Taken: ' + str(numSteps) + '\n')
        primed = True
    
      #pop off last to create room for rolling average
      averageMag.pop()
    #wait of .1 ms
    sleep(1e-4)
