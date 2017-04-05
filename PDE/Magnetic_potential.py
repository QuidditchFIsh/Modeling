import numpy as np

nMax = 50
maxIter = 1000
magPotential = np.full((nMax, nMax, nMax), 0)
wire = np.full((nMax, nMax, nMax), 0)
file = open('magnetic_result','w')
file1 = open('magnetic_Accuracy','w')


for i in range(-2, 2):
    for j in range(-2, 2):
        for k in range(0, nMax):
            wire[(nMax / 2) + i, (nMax / 2) + j, k] = 10

for iter in range(0, maxIter):
    accuracy = 0
    for i in range(1, nMax - 1):
        for j in range(1, nMax - 1):
            for k in range(1, nMax - 1):
                temp =magPotential[i,j,k]
                magPotential[i, j, k] = (1 / 6) * (magPotential[i + 1, j, k] + magPotential[i - 1, j, k] + magPotential[i, j + 1, k] + magPotential[i, j - 1, k] + magPotential[i, j, k + 1] + magPotential[i, j, k - 1] + wire[i, j, k])
                accuracy += abs(magPotential[i, j, k] - temp)
    file1.write(str(iter) + " " + str(accuracy) + "\n")
    accuracy = 0
    if iter % 10 == 0:
        print(iter/10)

for i in range(1, nMax - 1):
    for j in range(1, nMax - 1):
        for k in range(1, nMax - 1):
            file.write(str(i) + " " + str(j) + " " + str(k) + " " + str(magPotential[i, j, k]) + "\n")
    file.write("\n")


