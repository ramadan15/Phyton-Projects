#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=input()

def fonksiyon(yazı):
    yazı= yazı.title()
    yazı= "".join(char for char in yazı if char!= " ")
    yazı= "".join(char for char in yazı if char.isalpha())
    return yazı

fonksiyon(a)

