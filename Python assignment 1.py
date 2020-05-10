#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#comma-separated sequence on a single line.
            


# In[11]:


l=[]
for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))


# In[ ]:


#Write a Python program to accept the user's first and last name and then getting them printed in
#the the reverse order with a space between first name and last name.


# In[2]:


Type_name1=(input("Enter a first name: "))
Type_name2=(input("Enter a second name: "))
print("Reverse name is: ", Type_name2+ ' '+Type_name1)


# In[ ]:


#Write a Python program to find the volume of a sphere with diameter 12 cm.
#Formula: V=4/3 * π * r


# In[3]:


d=12
pi=3.14
Area_of_sphere= 4/3*3.14*(d/2)**3
print(round(Area_of_sphere,2))
    


# In[ ]:


#Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list.


# In[4]:


values = input("Please add some numbers in a row: ")
l = values.split(",")
print(l)


# In[ ]:


#Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*


# In[25]:


for i in range(0,9):
    if(i <= 4):
        for j in range(0,i+1):
            print("*", end=" ")
        print("\n")
    else:
        for j in range(i,9):
            print("*", end=" ")
        print("\n")



# In[ ]:





# In[13]:


#Write a Python program to reverse a word after accepting the input from the user
#Sample Output:
#Input word: AcadGild
#Output: dilGdacA


# In[15]:


words= input("Enter a word: ")
print(words[::-1])
    


# In[ ]:





# In[16]:


#Write a Python Program to print the given string in the format specified in the sample output.
#WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
#SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
#its citizens
#Sample Output:
#WE, THE PEOPLE OF INDIA,
      #having solemnly resolved to constitute India into a SOVEREIGN, !
                  #SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
                      #and to secure to all its citizens

print("WE, THE PEOPLE OF INDIA,\n\thaving solemly resolved  to constitute India into a SOVERIGN, !\n\t\t\tSOCAILIST,SECULAR,DEMOCRATIC REPUBLIC\n\t\t\t\tand to secure all its citizens")


        


# In[ ]:





# In[ ]:





# In[ ]:




