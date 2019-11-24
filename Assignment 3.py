#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python Program - Make Simple Calculator

print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");
print("5. Exit");
choice = int(input("Enter your choice: "));
if (choice>=1 and choice<=4):
    print("Enter two numbers: ");
    num1 = int(input());
    num2 = int(input());
    if choice == 1:
    	res = num1 + num2;
    	print("Result = ", res);
    elif choice == 2:
    	res = num1 - num2;
    	print("Result = ", res);
    elif choice == 3:
    	res = num1 * num2;
    	print("Result = ", res);
    else:
    	res = num1 / num2;
    	print("Result = ", res);
elif choice == 5:
    exit()
else:
    print("Wrong input..!!")


# In[3]:


# Python program to print positive Numbers in a List 

# list of numbers 
list1 = [-10, 21, -4, -45, -66, 93] 
num = 0

# using while loop	 
while(num < len(list1)): 
	
	# checking condition 
	if list1[num] >= 0: 
		print(list1[num], end = " ") 
	
	# increment num 
	num += 1


# In[20]:


#To add key to Dictinary
dic = {0:10,1:20}
print('Original dictionary',dic)
dic.update({2:30})
print('Updated dictionary',dic)


# In[19]:


#To sum all Numeric items
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))


# In[17]:


# Python program to print 
# duplicates from a list 
# of integers 
def Repeat(x): 
	_size = len(x) 
	repeated = [] 
	for i in range(_size): 
		k = i + 1
		for j in range(k, _size): 
			if x[i] == x[j] and x[i] not in repeated: 
				repeated.append(x[i]) 
	return repeated 

# Driver Code 
list1 = [10, 20, 30, 20, 20, 30, 40, 
		50, -20, 60, 60, -20, -20] 
print (Repeat(list1)) 


# In[18]:


# Python3 Program to check whether a 
# given key already exists in a dictionary. 

# Function to print sum 
def checkKey(dict, key): 
	
	if key in dict.keys(): 
		print("Present, ", end =" ") 
		print("value =", dict[key]) 
	else: 
		print("Not present") 

# Driver Code 
dict = {'a': 100, 'b':200, 'c':300} 

key = 'b'
checkKey(dict, key) 

key = 'w'
checkKey(dict, key) 


# In[ ]:




