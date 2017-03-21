import matplotlib.pyplot as plt
from numpy import *;
import numpy as np

nMax = 50;maxIter = 20000;xStep = 0.4;tStep = 0.1;a=0.1;M=0.1;k=0.01
phiOld = np.random.random((nMax,nMax))
#phiOld = phiOld + 0.5
phiNew = np.full((nMax, nMax), 0)
mu = np.full((nMax, nMax), 0)
fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.imshow(phiOld, cmap='hot', interpolation='nearest')
plt.show(block=False)

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

    phiOld = phiNew.copy()
    if iter % 100 == 0:
        im.set_array(phiOld)
        fig.canvas.draw()
