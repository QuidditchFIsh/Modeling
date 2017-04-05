import numpy as np
w = 1.4
nMax = 50
maxIter = 100
file_potential = open('relaxation_potential_'+str(w), 'w')
file_accuracy = open('relaxation_accuracy_'+str(w), 'w')
phi = np.full((nMax, nMax, nMax), 0)
rho = np.full((nMax, nMax, nMax), 0)
accuracy = 0

temp = 0
for i in range(-1, 1):
    for j in range(-1, 1):
        for k in range(-1, 1):
            rho[(nMax / 2) + i, (nMax / 2) + j, (nMax / 2) + k] = -10
            print(str((nMax / 2) + i) + " " + str((nMax / 2) + j) + " " + str((nMax / 2) + k) + "\n")

for iter in range(0, maxIter):
    accuracy = 0
    for i in range(1, nMax - 1):
        for j in range(1, nMax - 1):
            for k in range(1, nMax - 1):
                temp = phi[i, j, k]
                phi[i, j, k] = (1 - w) * phi[i, j, k]- + (w / 6) * (phi[i + 1, j, k] + phi[i - 1, j, k] + phi[i, j + 1, k] + phi[i, j - 1, k] + phi[i, j, k + 1] + phi[i, j, k - 1] + rho[i, j, k])
                accuracy += abs(temp - phi[i, j, k])
    file_accuracy.write(str(iter) + " " + str(accuracy) + "\n")
