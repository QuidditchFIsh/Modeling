import matplotlib.pyplot as plt
import numpy as np

test = np.full((5,5),9)
test3,test2 = np.gradient(test)
print(test2)
