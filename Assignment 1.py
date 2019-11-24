#!/usr/bin/env python
# coding: utf-8

# In[10]:


a =" Twinkle, Twinkle , little star"
b = "How I wonder what you are"
c = " Up above the world so high"
d =" Like a diamond in the sky"

print (a,"\n\t",b,"\n\t\t", c, "\n\t\t",d,"\n", a, "\n\t", b)


# In[11]:


import sys
print(sys.version)


# In[16]:


import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)


# In[17]:


PI = 3.14
r = float(input('Enter the radius of the circle :'))
area = PI * r **2
print("Area of the circle is : %.2f" %area)


# In[18]:


firstname = input("Input your First Name : ")
lastname = input("Input your Last Name : ")
print ( lastname + " " + firstname)


# In[ ]:


# taking two inputs at a time 
x, y = input("Enter a two value: ").split() 
print("Number of boys: ", x) 
print("Number of girls: ", y) 
print() 


# In[ ]:




