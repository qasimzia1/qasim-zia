#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("piaic firstr assignment using 5 built in funtions")


# In[2]:


help(print)


# In[3]:


get_ipython().run_line_magic('pinfo', 'print')


# In[4]:


print("pakistan",1947, 65)


# In[5]:


print("pakistan",1947, 65,sep="#")


# In[7]:


a=12.6
#to find its type we will use command  type
type(a)


# In[8]:


country="pakistan"
type(country)


# In[12]:


#adding two string variables
name="qasim"
second_name="zia"
print(name+second_name)


# In[13]:


val1=100
val2=10.6
diff=val2-val1
print(diff)


# In[14]:


val1=100
val2=10.6
diff=val1-val2
print(diff)


# In[15]:


type(diff)


# In[17]:


val1=100
val2=10.6
div=val2/val1 #use by default float div 
print(diff)


# In[18]:


name = input("Enter Your Name")
father_name = input("Enter your Father's name")
uni = input("University")


message = """
PIAIC ISLAMABAD BATCH3
Name : {}
Father_Name: {} 
University: {}
"""

message1 = message.format(name, father_name, uni)

print(message1)


# In[ ]:




