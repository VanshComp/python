#WAF to print the length of a list. ( list is the parameter)

# def my_list(list):
#     print(len(list))
#     return len(list)
# input_list=input("Enter your list with spaces: ")
# list=input_list.split()
# my_list(list)

#WAF to print the elements of a list in a single line. ( list is the parameter)

# def my_list(list):
#     print(list)
#     return list
# input_list=input("Enter your list with spaces: ")
# list=input_list.split()
# my_list(list)

#WAF to find the factorial of n. (n is the parameter)

# def fact(n):
#     result = 1
#     for i in range(1,n+1):
#         result *=i
#     print(result)
#     return result

# n = int(input("Enter number for which factorial is to be found: "))
# factorial_result = fact(n)
# print(f"The factorial of {n} is {factorial_result}")

#WAF to convert USD to INR.

# def converter(usd):
#     inr=usd*80
#     print("%d usd is converted into %d inr" % (usd,inr))
# usd=int(input("Enter usd from user: "))
# converter(usd)

# Write a recursive function to calculate the sum of first n natural numbers.

# def recursive_sum(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n + recursive_sum(n - 1)

# n = int(input("Enter number: "))
# result = recursive_sum(n)
# print("The sum is:", result)

# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

# def func(list,idx):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     func(list,idx+1)
# My_list=input("Enter list having spaces: ")
# list=My_list.split()
# func(list,0)    