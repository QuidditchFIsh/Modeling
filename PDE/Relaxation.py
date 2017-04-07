import numpy as np

nMax = 50
maxIter = 100
file_accuracy = open('relaxation_accuracy', 'w')
phi = np.full((nMax, nMax, nMax), 0)
rho = np.full((nMax, nMax, nMax), 0)
temp = 0
for i in range(-1, 1):
    for j in range(-1, 1):
        for k in range(-1, 1):
            rho[(nMax / 2) + i, (nMax / 2) + j, (nMax / 2) + k] = -1

for w in range(1200, 1400,5):
    w=w/1000
    accuracy =1
    iter=0
    phi = np.full((nMax, nMax, nMax), 0)
    print(w)
    while accuracy > 0.01:
        accuracy = 0
        iter +=1
        for i in range(1, nMax - 1):
            for j in range(1, nMax - 1):
                for k in range(1, nMax - 1):
                    temp = phi[i, j, k]
                    phi[i, j, k] = (1 - w) * phi[i, j, k] - + (w / 6) * (
                    phi[i + 1, j, k] + phi[i - 1, j, k] + phi[i, j + 1, k] + phi[i, j - 1, k] + phi[i, j, k + 1] + phi[
                        i, j, k - 1] + rho[i, j, k])
                    accuracy += abs(temp - phi[i, j, k])

    file_accuracy.write(str(w) + " " + str(iter) + "\n")
