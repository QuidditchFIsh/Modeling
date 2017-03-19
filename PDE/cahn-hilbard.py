import matplotlib.pylab as p
from numpy import *;
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

print('initalising')
nMax = 100;maxIter = 100;xStep = 0.1;tStep = 0.1;a=0.1;M=0.1;k=0.01
phiOld = full((nMax, nMax), 50 + np.rand.randint(0, 5))
mu, phiNew = full((nMax, nMax), 0)


for iter in range(maxIter):
    # first evolve the mu
    # a=M=0.1
    # k=0.01
    #in python the % sign works as math.floormod in java
    for i in range(0, nMax - 2):
        for j in range(0, nMax - 2):
            mu[i, j] = -a*phiOld[i, j] + a*(phiOld[i, j]**3) - (k/(xStep**2))*(phiOld[(i+1)% nMax,j] + phiOld[(i-1)% nMax,j] + phiOld[i,(j+1)% nMax] + phiOld[i,(j-1)% nMax] - 4*phiOld[i,j])

    for i in range(0, nMax - 2):
        for j in range(0, nMax - 2):
#now evolve the phi
            phiNew[i,j] = phiOld[i,j] + (M*tStep / xStep**2)*(mu[(i+1)% nMax,j] + mu[(i-1)% nMax,j] + mu[i,(j+1)% nMax] + mu[i,(j-1)% nMax] - 4*mu[i,j])


    phiOld = phiNew.copy()

#probably going to want a heat map here!!!






