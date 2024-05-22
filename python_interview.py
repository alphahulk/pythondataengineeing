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

def swap(input):
    # Ensure the list has at least two elements before swapping
    if len(input) >= 2:
        # Store the first element in a temporary variable
        first = input[0]
        # Assign the last element to the first position
        input[0] = input[-1]
        # Assign the temporary variable value to the last position
        input[-1] = first




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




prime number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


#pallindrome 
Here's a breakdown of the code:

Prompt the user to input a number.
Initialize variables:
temp: Store a temporary copy of the input number.
reverse: Initialize a variable to store the reversed number.
Use a while loop to reverse the digits of the number:
Inside the loop:
Get the last digit of the temp variable using the modulo operator % and store it in the remainder variable.
Update the reverse variable by multiplying it by 10 and adding the remainder.
Remove the last digit from temp by integer division // with 10.
Repeat this process until temp becomes 0.
After reversing the digits, compare the original number (num) with the reversed number (reverse).
If they are equal, print "Palindrome"; otherwise, print "Not Palindrome".
def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10  # Get the last digit
        reversed_number = reversed_number * 10 + digit  # Append digit to reversed_number
        number = number // 10  # Remove the last digit from number

    return original_number == reversed_number

# Example usage:
number = 12321
if is_palindrome(number):
    print("Yes")
else:
    print("No")



#factorial
num = int(input("Enter a number: "))
# 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)




#fibonacci
def fibonacci(n):
    if n <= 0:
        return "Invalid input: Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
num = int(input("Enter a number: "))
print("Fibonacci of", num, "is:", fibonacci(num))
In this recursive approach:

The fibonacci function takes an integer n as input and returns the Fibonacci number at position n.
If n is 1, it returns 0; if n is 2, it returns 1.
For n > 2, it recursively calculates the Fibonacci number by adding the previous two Fibonacci numbers (fibonacci(n - 1) and fibonacci(n - 2)).



bubble sort
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(my_list)

print("Sorted array:", my_list)


# binary search->
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10




# -------------------------
def add_without_plus(a, b):
    while b != 0:
        # Carry now contains common set bits of a and b
        carry = a & b
        
        # Sum of bits of a and b where at least one of the bits is not set
        a = a ^ b
        
        # Carry is shifted by one so that adding it to a gives the required sum
        b = carry << 1
    
    return a

# Test the function
num1 = 5
num2 = 7
print("Sum of", num1, "and", num2, "is:", add_without_plus(num1, num2))



# ----------
from datetime import datetime

def convert_date_format(date_str):
    # Parse the input date string into a datetime object
    original_date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Format the datetime object into the desired format
    converted_date = original_date.strftime('%d-%m-%Y')
    
    return converted_date

# Test the function
date_str = "2024-04-28"
converted_date_str = convert_date_format(date_str)
print("Original date:", date_str)
print("Converted date:", converted_date_str)


# ----------
9. Write a Program to combine two different dictionaries. While combining, if you find the same keys, you can add the values of these same keys. Output the new dictionary
We can use the Counter method from the collections module

from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)





# Reversing a list using two-pointer approach
def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
 
    return arr
 
arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))



def count_trailing_zeros(n):
    count = 0
    i = 5
    while n >= i:
        count += n // i
        i *= 5
    return count

# Example usage:
n = int(input("Enter a number: "))
print(f"The number of trailing zeros in {n}! is {count_trailing_zeros(n)}")
Explanation:
Initialize the count: Start with a count of 0.
Iterate through multiples of 5: For each multiple of 5 (i.e., 5, 25, 125, ...), count how many times 
𝑛
n can be divided by that multiple.
Update the count: For each iteration, add the result of 
𝑛
n divided by the current multiple of 5 to the count.
Stop when the multiple exceeds 
𝑛
n: When the multiple of 5 exceeds 
𝑛
n, stop the loop.
Example:
For 
𝑛
=
100
n=100:

⌊
100
/
5
⌋
=
20
⌊100/5⌋=20 (counts multiples of 5)
⌊
100
/
25
⌋
=
4
⌊100/25⌋=4 (counts multiples of 25)
⌊
100
/
125
⌋
=
0
⌊100/125⌋=0 (no multiples of 125 within 100)
So, the number of trailing zeros in 
100
!
100! is 
20
+
4
=
24
20+4=24.




How to Remove Letters From a String in Python
input_string = 'Geeks123For123Geeks'
output_string = ''.join([char for char in input_string if not char.isdigit()])

print(output_string)
