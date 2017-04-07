import numpy as np
import math

nMax = 26
maxIter = 500
print('Running GSPoisson')
phiOld = np.full((nMax, nMax, nMax), 0)
rho = np.full((nMax, nMax, nMax), 0)
accuracy =1
temp =0
iter =0
file = open("GS1",'w')
file1 = open('GSAccuracy','w')
file2 = open("eField_GS",'w')

for i in range(-1, 1):
    for j in range(-1, 1):
        for k in range(-1, 1):
            rho[(nMax / 2) + i, (nMax / 2) + j, (nMax / 2) + k] = 1
            print(str((nMax / 2) + i)+" " + str((nMax / 2) + j) + " "+str((nMax / 2) + k) +"\n")

while accuracy > 0.01:
    iter += 1
    accuracy = 0
    for i in range(1, nMax - 1):
        for j in range(1, nMax - 1):
            for k in range(1, nMax - 1):
                temp =phiOld[i,j,k]
                phiOld[i, j, k] = (1 / 6) * (phiOld[i + 1, j, k] + phiOld[i - 1, j, k] + phiOld[i, j + 1, k] + phiOld[i, j - 1, k] + phiOld[i, j, k + 1] + phiOld[i, j, k - 1] + rho[i, j, k])
                accuracy += abs(phiOld[i, j, k] - temp)
    file1.write(str(iter) + " " + str(accuracy) + "\n")
    if iter % 10 == 0:
        print(str(iter/10) + " " + str(accuracy))

for i in range(1, nMax - 1):
    for j in range(1, nMax - 1):
        for k in range(1, nMax - 1):
            file.write(str(i) + " " + str(j) + " " + str(k) + " " + str(phiOld[i, j, k]) + "\n")
    file.write("\n")

#now tunrn into the electric field and its vecotrs

eFieldx,eFieldy,eFieldz = np.gradient(phiOld)

for i in range(1, nMax - 1):
    for j in range(1, nMax - 1):
        for k in range(1, nMax - 1):
            len = math.sqrt((i-eFieldx[i,j,k])**2+(j-eFieldy[i,j,k])**2+(k-eFieldz[i,j,k])**"")
            file2.write(str(i) + " " + str(j) + " " + str(k) + " " + str(eFieldx[i,j,k]/len) + " "+ str(eFieldy[i,j,k]/len) + " "+ str(eFieldz[i,j,k]/len) + "\n ")
    file2.write("\n")
