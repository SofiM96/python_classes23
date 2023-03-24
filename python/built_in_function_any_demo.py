"""
This script demonstrates the functionalities of python built-in function any()
Author: Sofija Markovic
Date: 23.03.2023.
"""
# %% Basic functionality
print("Built-in function any() takes an iterable and returns True if any element of the iterable is true. If none of "
      "the elements are true, or the iterable is empty, any() returns False:")

print('Strings are iterables:', any('Hello'))
print('Empty string is evaluated False:', any(''))
print('Same goes for 0 and False: ', any([0, False]))
print('If only one element is True, any will return True: ', any([0, False, 3, 0, '']))
print("However, strings '0' and 'False' are both True:", any('0'), any('False'))

# %% Use with different iterables

# Lists:
print('Lists')
my_list = [0, 0, '', False]
print(any(my_list))

my_list = [0, 0, '', False, []]
print(any(my_list))

my_list = [0, 0, '', False, [5, 2, 3]]
print(any(my_list))
print()
# Tuples:
print('Tuples')
my_tuple = ('', 0, 0, 0, False, False)
print(any(my_tuple))

my_tuple = ('', 0, 0, 0, False, False, '0')
print(any(my_tuple))
print()
# Sets:
print('Sets')
my_set = {0, 2, 5, 3}
print(any(my_set))
print()

# Dictionaries:
print('Dictionaries')
my_dict = {1: 0, 2: '', 3: False}
print(any(my_dict))  # iterates through keys
print(any(my_dict.values()))  # this way any iterates through values
print()
print('What happens to integers?')
any(5)


# %% Equivalent function

def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False


print(my_any(''))
print(my_any(my_dict))
print(my_any([0, 0, 0, 'False']))
print(my_any(my_dict.values()))
