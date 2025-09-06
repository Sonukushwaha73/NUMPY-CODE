
# Short me yaad rakho:

# + , -, *, /, ** → arithmetic

# ==, >, < → comparison

# np.logical_and/or/not → logical

# @ → matrix multiplication karta hai jaise(row x column)






# Arthmathmatics
import numpy as np


a = np.array([12,34,56])
b = np.array([67,78,98])
print("addtion:",a+b)#[ 79 112 154]
print("subtraction:",a-b)#[-55 -44 -42]
print("division:",a/b)#[0.17910448 0.43589744 0.57142857]
print("Multiplication:", a * b)#[ 804 2652 5488]
print("power:",a**2)#[ 144 1156 3136]



#Comparison Operators--- ==, >, <

print("equal:",a==b)
print("greater than:",a>b)
print("less than:",a<b)


#Logical Operators--->and or not
#Logic = decision making


#AND--- dono true hona chahiye
#OR-----ek true bhi clega
#NOT------ true ko false   false ko true

print(np.logical_and(a,b))
print(np.logical_or(a,b))
print(np.logical_not(a,b))
