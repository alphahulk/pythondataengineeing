# Python Interview Questions. (Asked in Volkswagen Group from hashtag#AWS data engineer role)

# 1. You are given a list of stock prices, where the stock's price on the i-th day is stored as the i-th element of the prices list.
# You want to maximize your profit trading the stock, but are only allowed to buy the stock once and sell it once on a future day.
# Write a function called max_profit which takes in this list of stock prices and computes the maximum profit possible. Return 0 if you can't make any profit.
# Input: prices = [9, 1, 3, 6, 4, 8, 3, 5, 5] Output: 7 Explanation: Buy on day 2 (price = 1) and sell on day 6 (price = 8), profit = 8 - 1 = 7.

# prices = [9, 1, 3, 6, 4, 8, 3, 5, 5]
# def max_price(prices):
#     max_price=0
#     for i in range(len(prices)-1):
#         for j in range(i+1,len(prices)):
#             current_prof=prices[j]-prices[i]
#             print(current_prof)
#     if current_prof > max_profit:
#         max_profit = current_prof
#         return max_profit
#     print(max_profit)


# Python interview questions: (Was asked by hashtag#PWC for Snowflake Data Engineer Role)

# 1. Given an list of integers called input, and an integer target, return the index of the two numbers which sum up to the target. Do not use the same list element twice.
# Clarifications:
# Assume there aren't multiple valid solutions.
# In case there is no valid solution, return [-1, -1].
# Return the indexes in increasing order (i.e. [1,3], NOT [3,1]).

# input= [1, 4, 6, 10]
# target=10
# Expected Output =[1 2]

# input_list= [1, 4, 6, 10]
# target=10

# def two_sum(input_list: list[int], target: int) -> list[int]:
#     for i in range(len(input_list)):
#         for j in range(i + 1, len(input_list)):
#             if input_list[i] + input_list[j] == target:
#                 # If the condition is met, return the indices of the two elements
#                 return [i, j]
#     # If no such pair is found, return [-1, -1]
#     return [-1, -1]

# result=two_sum([1,4,6,20],10)
# print(result)

# ---**-----

# 1. Write a function to get the intersection of two lists.
# For example, if A = [1, 2, 3, 4, 5], and B = [0, 1, 3, 7] then you should return [1, 3].

# def setof(a,b):
#     intersection=[]
#     for value in a:
#         if value in b:
#             intersection.append(value)
#     return intersection

# a=[1,2,3,4]
# b=[0,1,3,7]
# result=setof(a,b)
# print(result)



# ----***-----
# 1. Python program to interchange first and last elements in a list.

# hashtag#Find the lenght of the list and simply
# hashtag#swap the first element with (n-1)th element.

# def swaplist(newlist):
#  lenght = len(newlist)

#  temp = newlist[0]
#  newlist[0] = newlist[lenght-1]
#  newlist[lenght-1] = temp

#  return newlist

# hashtag#Give a list
# newlist=[12,34,34,4,5]

# print(swaplist(newlist))




# # 2. Check if element exists in list in Python.

# # Check if 3 exist or not.

# My_list = [1,4,5,6,7,8]

# i = 3


# if i in My_list:
#  print(f"{i} exits in the list")
# else:
#  print(f"{i} not exits in the list")

# OR

# Check if 4 exist or not.
# Initializing list
# test_list = [1,4,5,6,7,8]

# # Checking if 4 exists in list
# for i in test_list:
#  if(i == 4):
#  print(f"{i} exits in the list")



# ----***------

# Swap elements in String list "e" with "G" & "G" with "e" from the given list .

# list = ['eGt', 'bGst', 'MGntorship', 'for', 'DataGnginGGring', ':']

# We will be using replace() + list comprehension

# # Initializing List
# test_list = ['eGt', 'bGst', 'MGntorship', 'for', 'DataGnginGGring', ':']

# print("Original Input:" + str(test_list))

# res1 = [sub.replace('G','-').replace('e','G').replace('-','e') for sub in test_list]
# print("Output:" +str(res1))


# ---**----
# 1 Remove Duplicates from the list.

# # Python program to print duplicates from a list of integers
# lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

# uniqueList = []
# duplicateList = []

# for i in lis:
#  if i not in uniqueList:
#  uniqueList.append(i)
#  elif i not in duplicateList:
#  duplicateList.append(i)

# print(duplicateList)
# print(uniqueList)

# 2 Find if there are duplicates or not.

# def has_duplicate_or_not(values):
#  if len(values) != len(set(values)):
#  return True
#  else:
#  return False

# plants = ['One','Two','Three','One']
# has_duplicate_or_not(plants)