#!/usr/bin/env python
# coding: utf-8

# # [Classes](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes)
class MyFirstClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello {}!'.format(self.name))

my_instance = MyFirstClass('John Doe')
my_instance.greet()

print('my_instance: {}'.format(my_instance))
print('type: {}'.format(type(my_instance)))
print('my_instance.name: {}'.format(my_instance.name))


# ## Methods
# The functions inside classes are called methods. They are used similarly as functions. 
alice = MyFirstClass(name='Alice')
alice.greet()


# ### `__init__()`
# `__init__()` is a special method that is used for initialising instances of the class. It's called when you create an instance of the class. 

class Example:
    def __init__(self):
        print('Now we are inside __init__')
        
print('creating instance of Example')
example = Example()
print('instance created')


# `__init__()` is typically used for initialising instance variables of your class. These can be listed as arguments after `self`. To be able to access these instance variables later during your instance's lifetime, you have to save them into `self`. `self` is the first argument of the methods of your class and it's your access to the instance variables and other methods. 

class Example:
    def __init__(self, var1, var2):
        self.first_var = var1
        self.second_var = var2
        
    def print_variables(self):
        print('{} {}'.format(self.first_var, self.second_var))
        
e = Example('abc', 123)
e.print_variables()
    


# ### `__str__()`
# `__str__()` is a special method which is called when an instance of the class is converted to string (e.g. when you want to print the instance). In other words, by defining `__str__` method for your class, you can decide what's the printable version of the instances of your class. The method should return a string.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return 'Person: {}'.format(self.name)
    
jack = Person('Jack', 82)
print('This is the string presentation of jack: {}'.format(jack))


# ## Class variables vs instance variables
# Class variables are shared between all the instances of that class whereas instance variables can hold different values between different instances of that class.

class Example:
    # These are class variables
    name = 'Example class'
    description = 'Just an example of a simple class'

    def __init__(self, var1):
        # This is an instance variable
        self.instance_variable = var1

    def show_info(self):
        info = 'instance_variable: {}, name: {}, description: {}'.format(
            self.instance_variable, Example.name, Example.description)
        print(info)


inst1 = Example('foo')
inst2 = Example('bar')

# name and description have identical values between instances
assert inst1.name == inst2.name == Example.name
assert inst1.description == inst2.description == Example.description

# If you change the value of a class variable, it's changed across all instances
Example.name = 'Modified name'
inst1.show_info()
inst2.show_info()

# ## Public vs private
# In python there's now strict separation for private/public methods or instance variables. The convention is to start the name of the method or instance variable with underscore if it should be treated as private. Private means that it should not be accessed from outside of the class.
# 
# For example, let's consider that we have a `Person` class which has `age` as an instance variable. We want that `age` is not directly accessed (e.g. changed) after the instance is created. In Python, this would be:

# In[8]:


class Person:
    def __init__(self, age):
        self._age = age
        
example_person = Person(age=15)
# You can't do this:
# print(example_person.age)
# Nor this:
# example_person.age = 16


# If you want the `age` to be readable but not writable, you can use `property`:

class Person:
    def __init__(self, age):
        self._age = age
        
    @property
    def age(self):
        return self._age
        
example_person = Person(age=15)
# Now you can do this:
print(example_person.age)
# But not this:
#example_person.age = 16


# This way you can have a controlled access to the instance variables of your class: 

class Person:
    def __init__(self, age):
        self._age = age
        
    @property
    def age(self):
        return self._age
    
    def celebrate_birthday(self):
        self._age += 1
        print('Happy bday for {} years old!'.format(self._age))
        
example_person = Person(age=15)
example_person.celebrate_birthday()


# ## Introduction to inheritance


class Animal:
    def greet(self):
        print('Hello, I am an animal')

    @property
    def favorite_food(self):
        return 'chicken'


class Dog(Animal):
    def greet(self):
        print('wof wof')


class Cat(Animal):
    @property
    def favorite_food(self):
        return 'fish'



dog = Dog()
dog.greet()
print("Dog's favorite food is {}".format(dog.favorite_food))
cat = Cat()
cat.greet()
print("Cat's favorite food is {}".format(cat.favorite_food))

