#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Factorial Function

def fun_factorial():
    num = int(input("please enter a positive number whose factorial you want"))
    import math
    y = math.factorial(num)
    strn = str(num)
    print("factorial of ",num ,"=",y)
fun_factorial()


# In[3]:


#Calculate Upper Case and Lower Case String
def case_counter():
    upper = 0
    lower= 0
    stn = input("enter string")
    new_stn = stn.replace(" ","")
    for a in new_stn:
        check_case = a.isupper()
        if check_case == True:
            upper += 1
        elif check_case == False :
            lower += 1

    print("Number of upper case letters in your entered string = ",upper)
    print("Number of lower case letters in your entered string = ",lower)
case_counter()


# In[5]:


# Palindrome Test


def palindrome_check():
    string = input("enter a string")
    string_length = len(string)
    ss = string[:: -1]
    if string == ss:
        print("passed string is palindrome")
    else:
        print("passed string is not a palindrome")
palindrome_check()


# In[6]:


#Prime Number Function

def check_primeNumber():
    number = int(input("enter number to check if it is prime"))
    for i in range (2 , number):
        if number % i == 0 :
            print ("entered integer is not a prime number")
        else :
            print("entered integer is a prime number")
        break
check_primeNumber()


# In[7]:


#Receipt Details

def recipt():
    status = ""
    list_items = []
    print("when you have entered all items type done")
    while status != "done":
        status = input("enter item")
        list_items.append(status)
    list_items.remove("done")
    return print ("items you purchased are : ",list_items)
recipt()


# In[ ]:




