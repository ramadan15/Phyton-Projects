#!/usr/bin/env python
# coding: utf-8

# - Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# 
# - Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# In[4]:


def is_leap(year):
    if year%4!=0:
        return False
    elif year%4==0 and year%100==0 and year%400!=0:
        return False
    elif year%4==0 or (year%4==0 and year%100==0 and year%400==0): 
        return True
    
year= int(input())

is_leap(year)

