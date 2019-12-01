#!/usr/bin/env python
# coding: utf-8

# In[10]:


# dictionary to store information about a person first name, last name, age, and the city in which they live

person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# . Add a new key value pair about qualification then update the qualification value to high academic level 

person['Qualification'] = ('Highest Acadmic Qualification')
print (person ['Qualification'])

del person['Qualification']
print (person)


# In[3]:


# Make a dictionary called cities
cities = {
    "karachi":{
        "country" : "Pakistan",
        "population":"20 million",
        "fact":"karachi is the City",
    },
    "lahore" : {
        "country" : "Pakistan",
        "population":"15 million",
        "fact" : "Lahore is the city of Food",
    },
    "peshawar" : {
        "country": "Paksitan",
        "population": "5 million",
        "fact" :"Peshawar is the city of Flowers",
    },
}
print(cities)


# In[5]:


# A movie theater charges different ticket prices depending on a person’s age
age = int(input("enter your age"))
if age < 3 and age > 0  :
    print("free ticket")
elif age >= 3 and age < 12 :
    print("your movie ticket cost's $10")
elif age >= 12 :
    print("your movie ticket cost's $15")
else:
    print("You are not eligible for movie tickets")


# In[15]:


# Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland

def favorite_book (title):
    title = input("enter your favorite book name")
    print("one of my favorite book is :", title)
    
favorite_book("Title")


# In[17]:


# Write a program which randomly generate a number between 1 to 30 and ask the user in input field to guess the correct number

import random
value = random.randint(1 ,32)
guess = int(input("enter a number in range 1 to 30 as a guess number "))
if value == guess :
    print("bingo")
elif value > guess :
    print("wrong guess" + "\n" + "Hint : number is greater than the number you entered")
else :
    print("wrong guess" + "\n" + "Hint : number is less than number you entered")
guess_2 = int(input("enter another guess number"+ "\n" + "secound last chance"))
if guess_2 == value:
    print("bingo")
elif guess_2 > value :
    print("wrong guess" + "\n" + "Hint : number is less than number you entered")
else :
    print("wrong guess" + "\n" + "Hint : number is greater than number you entered")
guess_3 = int(input("enter another guess number" + "\n" + "last chance"))
if guess_3 == value :
    print("bingo")
else :
    print("better luck next time")
print("the actual number was : ", value)


# In[ ]:




