this_tuple = ("first", "Second", "Third", "Forth", "Fifth")

# this_tuple1 = ("krishna",)

# this_tuple2 = tuple(("krishna", "Regmi"))

# print(type(this_tuple))
# print(type(this_tuple1))
# print(type(this_tuple2))

# print(sorted(this_tuple)) #Print all value of tuple after sort
# print(this_tuple[1]) #Print value of first index

# if "Third" in this_tuple:
#     print("Yes found.")

#Update Tuple
'''Tuple can't be possible to edit*
    We can edit tuple after it's convert into list
'''
# temp = list(this_tuple)
# temp.append("Krishna")
# this_tuple = tuple(temp)
# print(this_tuple)

# this_tuple1 = ("Apple", "Banana", "Cherry")
# y = ("Orange",)

# this_tuple1 = this_tuple1 + y

# print(this_tuple1)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)
# del thistuple #Delete thistuple

# print(thistuple)

#Unpack Tuple
# fruits = ("Apple", "Banana", "Cherry")
# (first, second, third) = fruits
# print(first)
# print(second)
# print(third)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

#loop using tuple
# for i in this_tuple:
#     print(i)

# for i in range(len(this_tuple)):
#     print(this_tuple[i])

# Join Two Tuples
# t1 = ("a", "b", "c", "d")
# t2 = (1, 2, 3)

# t3 = t1 + t2

# print(t3)

#Multiply values
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)