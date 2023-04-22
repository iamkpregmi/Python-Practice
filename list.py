# mylist = ["krishna","kushal","sapan","Brijesh"]
# print(mylist)

# #print list item using for loop
# mylist = ["krishna","kushal","sapan","Brijesh"]
# for i in mylist:
#     print(i)

# mylist = ["krishna","kushal","sapan","Brijesh"]
# for i in range(len(mylist)):
#     print(mylist[i])


# #print list item using while loop
# mylist = ["krishna","kushal","sapan","Brijesh"]
# i = 0
# while i < len(mylist):
#     print(mylist[i])
#     i += 1

#Show Specific items form list
# mylist = ["krishna","kushal","sapan","Brijesh"]
# print(mylist[1]) #print kushal

#find specific value present or not in the list
# mylist = ["krishna","kushal","sapan","Brijesh"]
# search = input("Enter a value you want to search: ")
# if search in mylist:
#     print("Result found in list")
# else:
#     print("Result not found in list")

#Update list value
# mylist = ["krishna","kushal","sapan","Brijesh"]
# print(mylist)
# mylist[2] = "Sapan 1"
# print(mylist)

#Change a range of item values
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

#insert item in a list at the specific position
# mylist = ["krishna","kushal","sapan","Brijesh"]
# mylist.insert(2,"Komal Sharma")
# print(mylist)

#insert item in a list
# mylist = ["krishna","kushal","sapan","Brijesh"]
# mylist.append("Komal Sharma")
# print(mylist)

#Marge two list using extend() method
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# #Remove item from list
# mylist = ["krishna","kushal","sapan","Brijesh"]
# # mylist.remove("krishna")
# # mylist.pop() #Remove last item from the list
# # mylist.pop(2) #Remove 2nd index value from the list
# del mylist[2] #Remove 2nd index value from the list
# print(mylist)

# mylist = ["krishna","kushal","sapan","Brijesh"]
# mylist.clear() #clear list items
# print(mylist)

#Single item list
# mylist = ["krishna"] #or mylist = ["krishna",] both are same
# print(mylist)

# Looping Using List Comprehension
# List Comprehension is the shortest syntax for looping through lists
# mylist = ["krishna","kushal","sapan","Brijesh"]
# [print(i) for i in mylist] 

##########################################################################################################
# thislist = ["Sapan", "Alex", "Sapan", "Brijesh", "Radha", "Krishna", "Kushal"]
# # print(len(thislist)) #Print length of the string
# newlist = []
# for i in thislist:
#     if "K" in i:
#         newlist.append(i)

# print(newlist)

#Write above program using list Comprehension
# thislist = ["Sapan", "Alex", "Sapan", "Brijesh", "Radha", "Krishna", "Kushal"]
# newlist = [i for i in thislist if "K" in i]
# print(newlist)
##########################################################################################################

#Sort list alphabetically
# thislist = ["krishna","Sapan", "Alex", "Sapan", "Brijesh", "Radha", "Krishna", "Kushal"]
# thislist.sort()
# print(thislist) #first capital latter after that print small latter

#Sort Descending
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse=True)
# print(thislist)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
# Sort the list based on how close the number is to 50:
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

#copy list items
# mylist = ["krishna","kushal","sapan","Brijesh"]
# # mylist1 = mylist.copy()
# mylist1 = list(mylist)
# print(mylist)
# print(mylist1)
#-------------------------------------------------------------------------------------------------------
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

