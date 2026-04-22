#!/usr/bin/env python
# coding: utf-8

# In[4]:


marks=95
if marks>=90:
    print("Grade is A")
elif marks>=80:
    print("Grade is B")
elif marks>=70:
    print("Grade is C")
else:
    print("Grade is D")


# In[5]:


#Grade using user values

marks=input("Enter your marks: ")
if marks>='90':
    print("Grade is A")
elif marks>='80':
    print("Grade is B")
elif marks>='70':
    print("Grade is C")
else:
    print("Grade is D")

