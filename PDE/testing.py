import matplotlib.pyplot as plt
import numpy as np

test = np.full((5,5,5),9)
test3,test2,test1 = np.gradient(test)
print(test1)
print(test1.shape)
print('-----------')
print(test2)
file = open('test','w')
file.write(str(test2[1,1,1]))