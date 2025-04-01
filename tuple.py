#Write a program to perform the following operations:
#  1. Create a tuple with different datatypes 
# 2. Create another tuple of integers 
# 3. Create a new tuple by adding 9 to the previous tuple 
# 4. Count the occurrences of an element in the tuple 
# 5. Perform slicing on the tuple
tuple1=(25, 5.5, "helo")
print(tuple1)
tuple2=(2, 5, 6, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
print(tuple2)
tuple3=tuple2+(9,)
print(tuple3)
print(tuple3.count(9))
slice=tuple3[1:10]
print(slice)