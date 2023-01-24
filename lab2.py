#List_1Print the second item in the fruits list
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#L_2Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#L_3Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#L_4Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#L_5Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#L_6Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#L_7Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#L_8Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


#Tuples_1Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#T_2Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#T_3Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#T_4Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


#Sets_1Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#S_2Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#S_3Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#S_4Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#S_5Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#Dictionaries_1Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#D_2Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#D_3Add the key/value pair "color" : "red" to the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#D_4Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#D_5Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#While_1Print i as long as i is less than 6
i = 1
while i < 6:
  print(i)
  i += 1

#While_2Stop the loop if i is 3
i = 1
while i < 6:
  if i == 3:
    break
  i += 1

#while_3In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#While_4Print a message once the condition is false.
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#For_1Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#3Use the range function to loop through a code set 6 times.
for x in range(6):
  print(x)

#4Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
