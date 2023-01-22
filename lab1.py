#Synt_1
print("Hello World")

#Synt_2
if 5 > 2:
  print("Five is greater than two!")

  
#Com_1
#This is a comment

#Com_2
"""
This is a comment
written in 
more that just one line
"""


#Variables_1
carname = "Volvo"

#V_2
x = 50

#V_3
x = 5
y = 10
print(x + y)

#V_4
x = 5
y = 10
z = x + y
print(z)

#V_5
myfirst_name = "John"

#V_6
x = y = z = "Orange"

#V_7
def myfunc():
  global x
  x = "fantastic"

  
#DT_1
x = 5
print(type(x))

int

#DT_2
x = "Hello World"
print(type(x))

str

#DT_3
x = 20.5
print(type(x))

float

#DT_4
x = ["apple", "banana", "cherry"]
print(type(x))

list

#DT_5
x = ("apple", "banana", "cherry")
print(type(x))

tuple

#DT_6
x = {"name" : "John", "age" : 36}
print(type(x))

dict

#DT_7
x = True
print(type(x))

bool


#Num_1
x = 5
x = float(x)

#Num_2
x = 5.5
x = int(x)

#Num_3
x = 5
x = complex(x)


#Str_1
x = "Hello World"
print(len(x))

#Str_2
txt = "Hello World"
x = txt[0]

#Str_3
txt = "Hello World"
x = txt[2:5]

#Str_4
txt = " Hello World "
x = txt.strip()

#Str_5
txt = "Hello World"
txt = txt.upper()

#Str_6
txt = "Hello World"
txt = txt.lower()

#Str_7
txt = "Hello World"
txt = txt.replace("H", "J")

#Str_8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#Bool_1
print(10 > 9)

True

#Bool_2
print(10 == 9)

False

#Bool_3
print(10 < 9)

False

#Bool_4
print(bool("abc"))

True

#Bool_5
print(bool(0))

False


#Oper_1
print(10 * 5)

#Oper_2
print(10 / 2)

#Oper_3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Oper_4
if 5 != 10:
  print("5 and 10 is not equal")

#Oper_5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")


#List_1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#L_2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#L_3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#L_4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#L_5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#L_6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#L_7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#L_8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


#Tuples_1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#T_2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#T_3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#T_4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


#Sets_1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#S_2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#S_3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#S_4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#S_5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#Dictionaries_1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#D_2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#D_3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#D_4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#D_5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()


#If/Else_1
a = 50
b = 10
if a > b:
  print("Hello World")

#IE_2
a = 50
b = 10
if a != b:
  print("Hello World")

#IE_3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#IE_4
a = 50
b = 10
if a = b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

#IE_5
if a == b and c == d:
   print("Hello")

#IE_6
if a == b or c == d:
  print("Hello")

#IE_7
if 5 > 2:
  print("Five is greater than two!")

#IE_8
if 5 > 2: print("Five is greater than two!")

#IE_9
print("Yes") if 5 > 2 else print("No")
