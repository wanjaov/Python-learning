"""
Datatypes in python
1. int - Integers, handles whole numbers
2. float- Handles decimals
3. string- Handles a a collection of characters
4. Bool- Boolean, handles logical statements has two values i.e: True, False
5. List- Takes in a collection of data items , they can be different types, they remove redundant values from the set unlike lists.
i.e: {1, 1,1, 2, 3} is transformed to {1, 2, 3}
6. Tuple - Takes in a collection of items and can allow redundancies, however tuples are immutable, they cannot be edited once created
i.e: (1, 2, 3, 4)
7. Dictionaries: They work with key value pairs for their items. That is each item, must have a key and value.All keys in a dictionary should have a specific type, values, however can have different types.
8. User_details = {
             "email": "john@gmail.com".
             "phone_number": 0716189133,
             "is_married": True
}

TODO
1. Difference btwn a list, a set, a tuple and a dictionary
2.What is a dictionary
3.Difference btwn an array and a list in python, also how to create an array in python
"""
# integer
# x = 10
# print(type(x))



#Boolean
z = False
print(type(z))

tuple_x = (1, 1, 1, 2,3)
list_y = [1, 1, 1, 2, 3]
set_z = {1, 1, 1, 2, 3}

print(tuple_x, type(tuple_x))
print(list_y, type(list_y))
print(set_z, type(set_z))

dict_user = {
    "name": "Micheal",
    "age": 19,
    "phone_number": 2547113344,
    "is_student": True
}
print(dict_user, type(dict_user))

#List operations
#Adding an item to a list
list_y.append(4)
print(list_y)

list_y.pop()
print(list_y)

list_y.pop()
print(list_y)

# TODO 
#   How to implement a queue and a stack in python

list_fruits = ["orange", "banana", "apple", "pineapple", "mango"]
tuple_fruits =("orange", "banana", "apple", "pineapple", "mango")
set_fruits ={"orange", "banana", "apple", "pineapple", "mango"}

print(list_fruits[3], type(list_fruits[3]))

#Editing value of a list item
list_fruits[3] = "avocado"

print(list_fruits)

print(set_fruits)
set_fruits.add("guavas")
print(set_fruits)
# set_fruits.update({"strawberries", "macadamia"})



print(tuple_fruits)
print(tuple_fruits[3])
list_fruits[3] ="Grapes"

#TODO adding removing nd reading dictionary items
#Tommorrow functions loops conditional in py w3schools and geeksforgeeks



