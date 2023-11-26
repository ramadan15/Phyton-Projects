#!/usr/bin/env python
# coding: utf-8

# - Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . 
# 
# - Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to 
# 
# - Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

# In[1]:


x = int(input())
y = int(input())
z = int(input())
n = int(input())
print(list([a,b,c] for a in range (x+1) for b in range (y+1) for c in range (z+1) if a+b+c!=n))

