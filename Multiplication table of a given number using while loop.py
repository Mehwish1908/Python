#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("Enter the number:"))
i=1
print(f"Multiplication table for {num}:")
while i<=10:
    print(f"{num}x{i}={num*i}")
    i+=1

