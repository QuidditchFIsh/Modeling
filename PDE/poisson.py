import matplotlib.pyplot as plt
import numpy as np
import math

iter =0
nMax = 26;
maxIter = 1000
phiOld = np.full((nMax, nMax, nMax), 0)
phiNew = np.full((nMax, nMax, nMax), 0)
rho = np.full((nMax, nMax, nMax), 0)
accuracy =10
file = open("Jacobi1",'w')
file1 = open("AccuracyJacobi",'w')
file2 = open("eField_Jacobi",'w')
# create the charge distribution in the middle of the box
# always iterate from 1 to nMAx -1 to keep the boundarys of the box 0
for i in range(-1, 1):
    for j in range(-1, 1):
        for k in range(-1, 1):
            rho[(nMax / 2) + i, (nMax / 2) + j, (nMax / 2) + k] = 1

while accuracy > 0.01:
    iter +=1
    accuracy =0
    for i in range(1, nMax - 1):
        for j in range(1, nMax - 1):
            for k in range(1, nMax - 1):
                phiNew[i, j, k] = (1 / 6) * (phiOld[i + 1, j, k] + phiOld[i - 1, j, k] + phiOld[i, j + 1, k] + phiOld[i, j - 1, k] + phiOld[i, j, k + 1] + phiOld[i, j, k - 1] + rho[i, j, k])
                accuracy += abs(phiOld[i,j,k] - phiNew[i,j,k])
    file1.write(str(iter) + " " + str(accuracy) + "\n")
    phiOld = phiNew.copy()
    if iter % 10 == 0:
        print(str(iter/10) + " " + str(accuracy))

for i in range(1, nMax - 1):
    for j in range(1, nMax - 1):
        for k in range(1, nMax - 1):
            file.write(str(i) + " " + str(j) + " " + str(k) + " " + str(phiNew[i, j, k]) + "\n")
    file.write("\n")

eFieldx,eFieldy,eFieldz = np.gradient(phiOld)

for i in range(1, nMax - 1):
    for j in range(1, nMax - 1):
        for k in range(1, nMax - 1):
            len = math.sqrt((i-eFieldx[i,j,k])**2+(j-eFieldy[i,j,k])**2+(k-eFieldz[i,j,k])**"")
            file2.write(str(i) + " " + str(j) + " " + str(k) + " " + str(eFieldx[i,j,k]/len) + " "+ str(eFieldy[i,j,k]/len) + " "+ str(eFieldz[i,j,k]/len) + "\n ")
    file2.write("\n")
