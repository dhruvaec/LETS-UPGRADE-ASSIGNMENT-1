#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Questions 1:
# Given the following jumbled word, OBANWRI guess the correct English word.
#
# A. RANIBOW
# B. RAINBOW
# C. BOWRANI
# D. ROBWANI
#
# ANS  : RAINBOW


# In[1]:


# Questions 2:
# Write a program which prints “LETS UPGRADE”. (Please note that you have to print in ALL CAPS as given)

print("LETS UPGRADE")

# or

string = "lets UPGRADE"
print(string.upper())

# Output:
# LETS UPGRADE
# LETS UPGRADE


# In[3]:


# Assignment :1(Que3)

# Questions 3:
# Write a program that takes cost price and selling price as input and displays whether the transaction is a
# Profit or a Loss or Neither.
# INPUT FORMAT
# the cost price.
#  selling price.
# OUTPUT
# Print "Profit" if the transaction is a profit or "Loss" if it is a loss. If it is neither
# profit nor loss, print "Neither".(You must not have quotes in your output)

cost_price = int(input())
selling_price = int(input())
if (selling_price - cost_price) > 0:
    print("Profit")
elif (selling_price - cost_price) < 0:
    print("Loss")
else:
    print("Neither")

# Output:
# Test case 1:
# 20
# 30
# Profit
#
# Test case 2:
# 20
# 10
# Loss

# Test case 3:
# 20
# 20
# Neither

# Test case 4:
# 19
# 19
# Neither

# Test case 5:
# 23
# 7
# Loss

# Test case 5:
# 19
# 95
# Profit


# In[4]:



# Questions 4:
# Write a program that takes an amount in Euros as input. You need to find its equivalent in
# Rupees and display it. Assume 1 Euro equals Rs. 80.
# Please note that you are expected to stick to the given input and output
# format as in sample test cases. Please don't add any extra lines such as
# 'Enter a number', etc.
# Your program should take only one number as input and display the output.


# euro = int(input())
# rupees = euro*80
# print(rupees)

# or
print(int(input())*80)


# Output:

# Test Case 1:
# 20
# 1600

# Test Case 2:
# 50
# 4000

# Test Case 3:
# 72
# 5760

# Test Case 4:
# 7
# 560

# Test Case 5:
# 7
# 560

# Test Case 6:
# 23
# 1840

# Test Case 7:
# 95
# 7600

# Test Case 8:
# 18
# 1440


# In[ ]:




