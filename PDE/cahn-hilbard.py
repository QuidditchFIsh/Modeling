import matplotlib.pyplot as plt
from numpy import *;
import numpy as np

nMax = 50;maxIter = 10000;xStep = 0.4;tStep = 0.2;a=0.1;M=0.1;k=0.02
phiOld = np.random.random((nMax,nMax))
#print(phiOld)
phiOld = (phiOld * 0.001)
phiOld = (phiOld + 0.5)
phiNew = np.full((nMax, nMax), 0)
mu = np.full((nMax, nMax), 0)
fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.imshow(phiOld, cmap='hot', interpolation='nearest')
plt.show(block=False)

file = open('cahn_hillard_free_energy','w')
freeEnergyDensity=0
time =0

for iter in range(maxIter):
    # first evolve the mu
    # a=M=0.1
    # k=0.01
    #in python the % sign works as math.floormod in java
    for i in range(0, nMax) :
        for j in range(0, nMax):
            mu[i, j] = -a*phiOld[i, j] + a*(phiOld[i, j]**3) - (k/(xStep**2))*(phiOld[(i+1)% nMax,j] + phiOld[(i-1)% nMax,j] + phiOld[i,(j+1)% nMax] + phiOld[i,(j-1)% nMax] - 4*phiOld[i,j])

    for i in range(0, nMax):
        for j in range(0, nMax):
#now evolve the phi
            phiNew[i,j] = phiOld[i,j] + (M*tStep / xStep**2)*(mu[(i+1)% nMax,j] + mu[(i-1)% nMax,j] + mu[i,(j+1)% nMax] + mu[i,(j-1)% nMax] - 4*mu[i,j])
    time += tStep

    for i in range(0,nMax):
        for j in range(0,nMax):
            freeEnergyDensity += (-a/2)*(phiNew[i,j]**2)+ (a/4)*(phiNew[i,j]**4) + (k/8*(xStep**2))*((phiNew[(i+1)% nMax,j]+phiNew[(i-1)% nMax,j])**2+(phiNew[i,(j+1)% nMax]+phiNew[i,(j-1)% nMax])**2)
    freeEnergyDensity /= (nMax * nMax)
    file.write(str(time) + " " + str(freeEnergyDensity) + "\n")

    phiOld = phiNew.copy()
    if iter % 100 == 0:
        im.set_array(phiOld)
        fig.canvas.draw()
        print(iter/10)
