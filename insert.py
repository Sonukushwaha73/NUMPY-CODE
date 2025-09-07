"""
insert - hamesha new elment banta hai hai element ko change karta hai
insert ( arary ,index ,value,asix= None)
array- originals array
index -
value -
axis -
axis-0 row-wise
axis-1 column-wise
"""



import numpy as np
arr = np.array([10,20,30,40,50,60])
new_array = np.insert(arr,1,100) 
print(new_array)
print(arr)