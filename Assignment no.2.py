#!/usr/bin/env python
# coding: utf-8

# In[3]:


sub1=int(input("Enter marks of the Physics subject: "))
sub2=int(input("Enter marks of the Chemistry subject: "))
sub3=int(input("Enter marks of the Maths subject: "))
sub4=int(input("Enter marks of the Biology subject: "))
sub5=int(input("Enter marks of the English subject: "))
f= (sub1+sub2+sub3+sub4+sub5)*100/500
print("Your Marks In Percentage Is",f,"%")
if f >=90:
    print("Grade: A")
elif f >= 80 or f < 90:
    print("Grade: B")
elif f >= 70 or f < 80:
    print("Grade: C")
elif f >= 60 or f < 70:
    print("Grade: D")
else:
    print("Grade: F")


# In[4]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[13]:


# Python code to demonstrate 
# length of list 
# using native method
# Initializing list 
test_list = [ 1, 4, 5, 7, 8 ] 

# Printing test_list 
print ("The list is : " + str(test_list)) 

# Finding length of list 
# using loop 
# Initializing counter 
counter = 0
for i in test_list: 
    
# incrementing counter 
	counter = counter + 1

# Printing length of list 
print ("Length of list using native method is : " + str(counter)) 


# In[1]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


# In[2]:


# Python program to find largest 
# number in a list 

# list of numbers 
list1 = [10, 20, 4, 45, 99] 

# sorting the list 
list1.sort() 

# printing the last number
print("Largest number is:", list1[-1]) 


# In[2]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []

for item in a:
    new_list.append(item)
if item < 5:
    print(new_list)


# In[ ]:




