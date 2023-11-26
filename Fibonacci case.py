#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: User Input
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Step 2: Initialize Variables
a, b = 0, 1

# Step 3: Loop
for i in range(1, n + 1):
    # Step 4: Fibonacci Calculation
    fibonacci = a
    a, b = b, a + b

    # Step 5: Output
    print(fibonacci)

