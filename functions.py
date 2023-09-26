"""
Function is a collection of code that achieves a particular onjective.
Characteristics
1. Has a name 
2. Has parameters
3. it has a body
4. It has a return type

We define a function in python using the key word def

def add(x, y):
    sum = x+y
    return x+y

print(add(10,30))
"""

def add(x: int, y: int):
    if not type(x) == int or not type(y) == int:
        return "X and Y should be numbers"
    sum = x+y
    return sum
    
print(add(10, True))

def multiplication(x: int, y: int):
    """
    Multiplys two numbers
    """
    multiplication = x*y
    return multiplication

print(multiplication(9, 100))

def division(x: int, y:int):
    if y == 0:
        return "Math error"
    divide = x/y
    return divide

print(division(4, 0))

# TODO Write a function that checks the age of a person and classifies them into :Minor, adult, Elderly

"""
SOLUTION BREAKDOWN
->Check the age groups for minor adults and elderly
1.Minor: 0-17
2.Youth: 18-35
3.Mature Adults: 36-60
4.Elderly:61-120
4.Any other age will be classified as invalid
"""
def check_age(age:int) ->str:
    """
    Takes in an age, and specifies the age group i.e
    minor, adult, elderly
    """
    if not type(age) == int:
        return "Please input a valid number"
    if age >= 0 and age <= 17:
        return "This is minor"
    elif age >=18 and age <= 35:
        return "This is an youth"
    elif age >=36 and age<= 60:
        return "This is a mature adult"
    elif age >=61 and age <= 120:
        return "This is an elder"
    else:
        return "Invalid age"
    
print(check_age(40))

List_fruits = ["banana", "apples","managoes", "pineapples", "macadamia"]
#The for in loop: It is used to iterate through collections

for fruit in List_fruits:
    print(fruit)

   # TODO Go look at while loops , range ()function in python and how to use and iterate over it
   # Nested if conditions
   # Nested loops

   #THE WHILE LOOP
i=0
while i < 6:
    print(i)

    i +=1 # i = i+1
 

