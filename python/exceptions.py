#!/usr/bin/env python
# coding: utf-8

# # [Exceptions](https://docs.python.org/3/library/exceptions.html#concrete-exceptions)
# When something goes wrong an exception is raised. For example, if you try to divide by zero, `ZeroDivisionError` is raised or if you try to access a nonexistent key in a dictionary, `KeyError` is raised.
# 
# 
empty_dict = {}


# ## `try-except` structure 
# If you know that a block of code can fail in some manner, you can use `try-except` structure to handle potential exceptions in a desired way.


# Let's try to open a file that does not exist
file_name = 'not_existing.txt'

try:
    with open(file_name, 'r') as my_file:
        print('File is successfully open')
        
except FileNotFoundError as e:
    print('Uups, file: {} not found'.format(file_name))
    print('Exception: {} was raised'.format(e))


# If you don't know the type of exceptions that a code block can possibly raise, you can use `Exception` which catches all exceptions. In addition, you can have multiple `except` statements.

def calculate_division(var1, var2):
    result = 0
    
    try:
        result = var1 / var2
    except ZeroDivisionError as ex1:
        print("Can't divide by zero")
    except Exception as ex2:
        print('Exception: {}'.format(ex2))

    return result

result1 = calculate_division(3, 3)
print('result1: {}'.format(result1))

result2 = calculate_division(3, '3')
print('result2: {}'.format(result2))

result3 = calculate_division(3, 0)
print('result3: {}'.format(result3))


# `try-except` can be also in outer scope:

def calculate_division(var1, var2):
    return var1 / var2

try:
    result = calculate_division(3, '3')
except Exception as e:
    print(e)


# ## Creating your custom exceptions
# In your own applications, you can use custom exceptions for signaling users about errors which occur during your application run time.  

import math

# Define your own exception
class NegativeNumbersNotSupported(Exception):
    pass

# Dummy example how to use your custom exception
def secret_calculation(number1, number2):
    if number1 < 0 or number2 < 0:
        msg = 'Negative number in at least one of the parameters: {}, {}'.format(
            number1, number2)
        raise NegativeNumbersNotSupported(msg)

    return math.sqrt(number1) + math.sqrt(number2)

# Uncomment to see the traceback
# result = secret_calculation(-1, 1)

