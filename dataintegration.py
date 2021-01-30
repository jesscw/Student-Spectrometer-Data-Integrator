
"""
tag(filepath): given a file, will add "Scan No. X" to each instance of a MCS scan
integrate(scannumbers, filepath): given a list of scan numbers and a file path, combines the data from each specified scan into one array
plot(data): given an array of data, will plot as a bar plot
"""


import fileinput
import numpy as np
import matplotlib.pyplot as plt

def tag(filepath):
    i = 1
    for line in fileinput.FileInput(filepath,inplace=1):
            if "Started a MCS scan" in line:
                line=line.replace(line,line+"Scan No. " + str(i))
                i+=1
                print(line)
            else:
                print(line, end = '')
                
def integrate(scannumbers, filepath):
    f = open(filepath, 'r')
    data = [0]*1000
    
    while True:
        line = f.readline()
        if not line: break
        if "Scan No." in line:
            line = line.rstrip().strip("Scan No. ")
            if int(line) in scannumbers:
                for i in range(11):
                    f.readline()
                for i in range(1000):
                    line = f.readline()
                    line = line.rstrip()
                    data[i] += int(line)
    return data

def plot(data):
    y = np.array(data)
    x = range(0,1000)
    plt.bar(x, y, edgecolor='k')
    

    
            
    
    
    
    