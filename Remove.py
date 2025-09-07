
#Remove   np.delete(array,index,axis = none)
#flettern array 



import numpy as np
arr = np.array([10,20,30,40,50,60])
new_array = np.delete(arr, 2)
print(new_array)




#2D remove array



import numpy as np
arr_2D = np.array([[12,34,56],[78,89,90]])
#arr_2D = np.array([[12,34,56],[78,89,90]])
new_arr_2D = np.delete(arr_2D, 0 ,axis=0)
print(new_arr_2D)# yaha bs first row delte hoga
