import math
from numpy import *
import numpy

array1 = full((5,5),2)
array2 = full((5,5),3)

array1 = array2.copy()
array2[2,2]= 66
array1[3,3] = 44
print(array1)
print(array2)