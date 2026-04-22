#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("Enter the number:"))
print(f"Multiplication table for {num}:")
for i in range(1,11):
    print(f"{num}x{i}={num*i}")

