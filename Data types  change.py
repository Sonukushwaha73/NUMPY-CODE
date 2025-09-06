
# dtype=float → banate waqt type fix karo

# astype() → baad me convert karo

#int me change
import numpy as np
arr = np.array([1.4,3.5,6.7])
int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)

#float change 
import numpy as np
arr = np.array([1,3,6])
int_arr = arr.astype(float)
print(int_arr)
print(int_arr.dtype)


#string change
import numpy as np
arr = np.array([1,3,6])
int_arr = arr.astype(str)
print(int_arr)
print(int_arr.dtype)




#boolean
import numpy as np
arr = np.array([1,3,6])
int_arr = arr.astype(bool)
print(int_arr)
print(int_arr.dtype)