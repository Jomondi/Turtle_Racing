# Numbers divisible by 5
# def is_divisible(numList):
#   for num in numList:
#        if (num % 5) == 0:
#            print(num)

# is_divisible(numList = [10, 20, 33, 46, 55])

# *********************************************************************************

# Check how many times sub-string appears in a string

# text = "Emma is good developer. Emma is a writer"

# count = text.count("Emma")
# print(count)

# *********************************************************************************

# Accept list of 5 float numbers as a input from user
# count = 0


# def numbers_entered():
#   if count.numbers_entered < 5:
#        print(input("Enter a float number: "))
#        (numbers_entered())

# *********************************************************************************
# Using the round() function
# amount = float(input("Enter the amount: "))
# print("\n")
# print("The amount of the product is $" + str(round(amount, 2)))

# *********************************************************************************
# name = input("Enter your name: ")
# for i in range(5):
#   print("I love you " + name)

# *********************************************************************************
# using the math import
# import math
#
# a = 52
#
# print(math.log10(a).__round__(2))
# print(math.sqrt(a).__round__(2))

# *********************************************************************************
# Using while and for loops
# for i in range(10):
#     print(i + 1)

# i = 0
# while i <= 10:
#     print(i)
#     i = i + 1
# *********************************************************************************
# Random generator
# import random
#
#
# def premier(team):
#     if team == 1:
#         return "Manchester"
#     elif team == 2:
#         return 'Merseyside'
#     elif team == 3:
#         return "Stratford"
#     elif team == 4:
#         return "London"
#
#
# r = random.randint(1, 4)
# position = premier(r)
# print(position)
# *********************************************************************************
# Need to work on making this work
# names = 'Those ppl are not allowed to come down here.'# ['Bones', 'Flacco', 'Isles', 'Bruno', 'Tiger', 'Izom', 'Becks', 'Bucky', 'Dino', 'Den', 'Lion', 'Bear']
# if names.startswith('Those'):
#     print(names)
# else:
#     print("Does not start with that!")
# *******************************************************************************************
# Random generator
# import random

# towns = ['Manchester', 'Merseyside', 'Stratford', 'Hawthorn', 'London', 'Berkshire']

# print("The current town is: " + random.choice(towns))

# print("The current town is: " + towns[random.randint(0, len(towns) - 1)])

# *******************************************************************************************
# Error Handling
# try:
#     number = int(input("Enter the digits: "))
#     print("The number entered is: " + number)
#
# except TypeError:
#     print("\nCannot add numbers(concatenate) with strings")
# *******************************************************************************************
# The methods keys(), values(), and items() are used to get values from a dictionary
# students = {'Alice': 'CompSci', 'Wanda': 'History', 'Mark': 'Math', 'John': 'Psychology'}
# for i in students.items():
#     print(i)
# *******************************************************************************************
# Using get() and setdefault() method in a dictionary
# students = {'Alice': 1, 'Wanda': 2, 'Mark': 3, 'John': 4}
#
# students.setdefault('Tony', 5)
# print("The team will be bringing " + str(students.get('Wanda', 0)) + " cups")
# print(students)
# *******************************************************************************************
# Program to show how many times each character appears in a string
# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# pprint.pprint(count)
# *******************************************************************************************
# Concatenating a dictionary
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {}
# for d in (dic1, dic2): dic3.update(d)
# print(dic3)

# *******************************************************************************************
# Checking if a value exists in a dictionary
# dic1 = {1: 10, 2: 20, 3: 30, 4: 40}
#
# def is_key_present(x):
#     if x in dic1:
#         print('Values is present in the dictionary')
#     else:
#         print('Value is not present in the dictionary')
#
# is_key_present(6)
# *******************************************************************************************
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are square of keys
# dic1 = {}
#
# for values in range(1, 12):
#     dic1[values] = values**2
# print(dic1)
# *******************************************************************************************
# Deleting values from a dictionary
# values = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81,
# 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# if 15 in values:
#      del values[15]
#
# print(values)
# *******************************************************************************************
# Write a Python program to get the maximum and minimum value in a dictionary
# values = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
# 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
#
# for i in range(values):
#     print(values.max())
# *******************************************************************************************
# Printing multi line string using '''
# print('''Dear Alice,
# Eve's cat has been arrested for catnapping, cat burglary, and extortion.
# Sincerely, Bob''')
# *******************************************************************************************
# String interpolation
# name = 'Al'
# age = 4000
# print('My name is %s. I am %s years old.' % (name, age))
# or
# print(f'My name is {name}. Next year I will be {age + 1}.')
# *******************************************************************************************
# String manipulation using join and split
# string = 'My name is Papa Jones'
# print(string.split())
# print(''.join(string))
# *******************************************************************************************
# Removing spaces from string
# hi = 'Hello'.rstrip()
# print(hi)
# *******************************************************************************************
# Regular expressions
# import re

# phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phone_number_regex.search('My number is 415-555-4242.')
# print('Phone number found is: ' + mo.group())

# str='The advancements in biomarine studies franky@google.com, with the investments ' \
#    'necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'
# regex = r'\S+@\S+'
# emails=re.findall(regex, str)
# print(emails)
# *******************************************************************************************
# '''Create a function showEmployee() in such a way that it should accept employee name, and
# it’s salary and display both, and if the salary is missing in function call it should show
# it as 9000'''
#
# def showEmployee(name, salary = 9000):
#     print("Name is ", name, "Salary is ", salary)
#
# showEmployee('Ben', 1200)
# *******************************************************************************************
# helloFile = open('/Users/jomondi/Desktop/HalloWorld.rtf', 'a')
# helloFile.write('\nToday is Monday')
# helloFile.read()
# print(helloFile)

# import requests
#
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.status_code
#
# import bs4
# *******************************************************************************************
# Reversing a string
# def reverse_words_order_and_swap_cases(sentence):
#     # Write your code here
#     word = sentence.split()
#     word = word[-1::-1]
#     return ' '.join(word)
#
# print(reverse_words_order_and_swap_cases('awesome is coding'))
# *******************************************************************************************
# Calculating total price
# def solve(meal_cost, tip_percent, tax_percent):
#     tip_percent = meal_cost/100 * tip_percent
#     tax_percent = meal_cost/100 * tax_percent
#     meal_cost = meal_cost + tip_percent + tax_percent
#     print(round(meal_cost))
#
# if __name__ == '__main__':
#     meal_cost = float(input('Meal cost: '))
#
#     tip_percent = int(input('Tip %: '))
#
#     tax_percent = int(input('Tax %: '))
#
#     solve(meal_cost, tip_percent, tax_percent)
# *******************************************************************************************
# Web scrapping cyclegear
# import bs4 as BeautifulSoup, requests
#
# res = requests.get('https://www.cyclegear.com/gear/bilt-interstate-gloves')
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# elems = soup.select_one('#main-content > div.product-hero.js-SkuSelector-341247 > '
#                         'div.product-hero__sku-selector.sku-selector > div.sku-selector'
#                         '__pricing > div > div.sku-selector__price-retail.product-details'
#                         '__price-retail.js-SkuSelector-priceRetail > span')
# print(elems)
# *******************************************************************************************
# import random
#
# count = 0
# while count <= 10-1:
#     dates = random.randint(1, 6)
#     count += 1
# print(f'Dice number is: {dates}')
# print('Count is ' +str(count))
# *******************************************************************************************
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_names = ['Name', 'Sex', 'Age']
# table.add_row(['Noha', 'Male', 22])
# print(table)
# *******************************************************************************************
