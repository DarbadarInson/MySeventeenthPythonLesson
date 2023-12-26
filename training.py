import random

mylist = ["apple", "banana", "cherry", "apelsin"]

print(random.choice(mylist)) 

print("-----------------------------")

x = "WELCOME"

print(random.choice(x))

print("-----------------------------")

print(random.randint(3, 9)) 

print("-----------------------------")

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist) 

print("-----------------------------")

from random import random

  
lst = []
 
for i in range(10):
  lst.append(random())
   
# Prints random items
print(lst)