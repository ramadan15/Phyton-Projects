#!/usr/bin/env python
# coding: utf-8

# In[2]:


# we must first give input to define the shape of arrays
a= input()
b= a.split()
c=[]
# each iteration, numbers are first converted into the integer and the list has appended in each iteration
for itervar in b:
    itervar= int(itervar)
    c.append(itervar)
print(c)
# we will create our arrays 
import numpy as np
f= np.full((c[0],c[2]),1)
s= np.full((c[1],c[2]),2)
cn= np.concatenate([f,s])
cn

