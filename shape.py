#shape ek property hoti hai NumPy array ki jo batati hai array ka dimension aur size (rows × columns).
#Simple shabdon me bole to shape batata hai ki array kis size ka hai.


# 1D array
import numpy as np


arr = np.array([1,2,4,5])
print(arr.shape) #shape ka mtlb hota hai size kitna hai 


#2D array
 

import numpy as np
arr2 = np.array([[1,4,3,2,5,],# two arary row---- column five
                [8,6,0,3,5]])
print(arr2.shape)



#3D array

import numpy as np
arr3 = np.array([[1,3,2,4,6],[8,9,5,3,1],[7,9,3,0,1]])
print(arr3.shape)#block 3  row 3 column 5