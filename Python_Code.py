import serial
import time
import matplotlib.pyplot as plt
import csv
import numpy as np
S=serial.Serial('com5',115200) #com7
#csvfile=open('EMG_sample_1.csv')
#plots=csv.reader(csvfile,delimiter=',')
t=[]
val=[]
tmp=[]
newy=[]
emg_rectified=[]
resolution = 12
vcc = 3300
gain = 1920
sr = 1000  # sampling rate(amount of sigals present in 1 sec)
i = 0
w=25
emg_final=[]
box=[]
threshold = 0.1
for n in range(3000):
    try:
        cmd=S.readline()
        box=(cmd.split(b','))
        t.append(int(box[0])/1000)
        val.append(int(box[1]))  # if you use x= then only one value be there in x.
        signal_mv = (((int(box[1]) / 2 ** resolution) - 0.5) * vcc) / gain  # formula to change 4025 to volts
        emg_rectified.append(abs(signal_mv))
        moving_average = sum(emg_rectified[i+1-w:])/w
        emg_final.append(moving_average)
        if moving_average> threshold  :
            newy.append(1)
        else:
            newy.append(0)
        S.write((str(newy[-1])+'\n').encode('UTF-8'))
        x1=t[-400:]
        y1=emg_final[-400:]
        y2=newy[-400:]
        if i % 20 == 0: # it makes it go 10 at a time or else itll increase by one v slow
             plt.plot(x1, y1)
             plt.plot(x1, y2)
             plt.pause(0.01)
             plt.cla()
        i = i + 1
    except:
        print('Hello')
S.close()