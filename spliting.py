
"""
1. 1D Array Splitting

Imagine 1D array jaise ek line of boxes:


 2 Rows: horizontal line (up-down)

Columns: vertical line (left-right)


 3 np.array_split()

Agar equal divide nahi ho sakta, use karo:



np.hssplit()
np.vsplit()
"""



import numpy as np
arr = np.array([10,20,30,40,50,60])
print(np.split(arr,2))#[10, 20, 30]), array([40, 50, 60])]
print(np.split(arr,3))#array([10, 20]), array([30, 40]), array([50, 60])]

print(np.split(arr,20))#ValueError