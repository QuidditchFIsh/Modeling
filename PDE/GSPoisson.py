import matplotlib.pyplot as plt
import numpy as np

nMax = 50
maxIter = 1000

phiOld = np.full((nMax, nMax, nMax), 0)
phiNew = np.full((nMax, nMax, nMax), 0)
rho = np.full((nMax, nMax, nMax), 0)
accuracy =0
file = open("GS1",'w')

for i in range(-1, 1):
    for j in range(-1, 1):
        for k in range(-1, 1):
            rho[(nMax / 2) + i, (nMax / 2) + j, (nMax / 2) + k] = 1
            print(str((nMax / 2) + i)+" " + str((nMax / 2) + j) + " "+str((nMax / 2) + k) +"\n")

