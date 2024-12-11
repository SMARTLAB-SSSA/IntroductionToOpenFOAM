import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv)<1:
    raise ValueError("Give the path to the file to be opened")
else:
    data=np.loadtxt(sys.argv[1])


    plt.plot(data[:,0],data[:,1]-273.15)

    plt.hlines(30.15,data[0,0],data[-1,0],colors="r")
    plt.xlabel("Iteration")
    plt.ylabel("Temperature (°C)")
    # plt.yscale("log")
    plt.grid(which="both")
    plt.tight_layout()
    plt.savefig("PlotT.png")
    
