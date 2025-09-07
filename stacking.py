
"""
vertically
horizontally


vsstack()row wise
hstack ()column wise
"""


import numpy as np
arr1 = np.array([10,20,30,45])
arr2 = np.array([89,70,65,78])
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))
