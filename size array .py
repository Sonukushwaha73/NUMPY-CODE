#size------>Array ke andar total kitne elements hain ye shape se alg hai
#size == total element

#1D array

import numpy as np
arr = np.array([1,3,4,6,3,9])
print("size:",arr.size)
print("shape:",arr.shape)


#2D array

import numpy as np
arr = np.array([[1,3,4,6,3,9],[1,4,7,9,0,4]])
print("size:",arr.size)
print("shape:",arr.shape) #output  shape: (6,) kitna row colmn hai
# size: 12 
# shape: (2, 6) row*size



#3D array



import numpy as np
arr3 = np.array([[1,2,3],[4,5,6],[9,8,7]])
print("arr3.shape")#9
print(arr3.size)#block 3 row 3 column 3