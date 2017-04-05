import numpy as np
import math

nMax = 30
maxIter = 500
magPotential = np.full((nMax, nMax, nMax), 0)
b_field = np.full((nMax, nMax, nMax), 0)
wire = np.full((nMax, nMax, nMax), 0)
file_vector_field = open('magnetic_result', 'w')
file_accuracy = open('magnetic_Accuracy', 'w')
file_field = open('magnetic_field', 'w')

for i in range(-2, 2):
    for j in range(-2, 2):
        for k in range(0, nMax):
            wire[(nMax / 2) + i, (nMax / 2) + j, k] = 10

for iter in range(0, maxIter):
    accuracy = 0
    for i in range(1, nMax - 1):
        for j in range(1, nMax - 1):
            for k in range(1, nMax - 1):
                temp = magPotential[i, j, k]
                magPotential[i, j, k] = (1 / 6) * (
                magPotential[i + 1, j, k] + magPotential[i - 1, j, k] + magPotential[i, j + 1, k] + magPotential[
                    i, j - 1, k] + magPotential[i, j, k + 1] + magPotential[i, j, k - 1] + wire[i, j, k])
                accuracy += abs(magPotential[i, j, k] - temp)
        file_accuracy.write(str(iter) + " " + str(accuracy) + "\n")
    accuracy = 0
    if iter % 10 == 0:
        print(iter / 10)

for i in range(1, nMax - 1):
    for j in range(1, nMax - 1):
        for k in range(1, nMax - 1):
            file_vector_field.write(str(i) + " " + str(j) + " " + str(k) + " " + str(magPotential[i, j, k]) + "\n")
        file_vector_field.write("\n")

# too calcuate the magnetic field differentiate the vector potential in the folowing way B=(d_y A_z,d_x A_z,0)

d_x, d_y, d_z = np.gradient(magPotential)

for i in range(1, nMax - 1):
    for j in range(1, nMax - 1):
        for k in range(1, nMax - 1):
            len = math.sqrt((i - d_x[i, j, k])**2 + (j - d_y[i, j, k])**2 + (k) ** 2)
            file_field.write(str(i) + " " + str(j) + " " + str(k) + " " + str(d_x[i, j, k] / len) + " " + str(d_y[i, j, k] / len) + " " + str(0) + "\n ")
        file_field.write("\n")
