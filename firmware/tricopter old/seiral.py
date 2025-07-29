# import serial
import csv
import os
from posix import chdir, mkdir, write
import time
import matplotlib.pyplot as plt
import numpy as np
from numpy._core.numeric import array
from numpy.random import get_state, rand, random
import serial
import random
import threading

ser = serial.Serial("/dev/ttyACM0", 115200)

while ser.inWaiting() == 0:
    pass
while True:
    data = ser.readline().decode("UTF-8", errors="ignore").strip()
    print(data)



