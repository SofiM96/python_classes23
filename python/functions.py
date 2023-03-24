"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


#%%
# Setup / Data
song = 'Here Comes the Sun'
year = 1969

john = 'John Lennon'
paul = 'Paul McCartney'
george = 'George Harrison'
ringo = 'Ringo Starr'
the_beatles = [john, paul, george, ringo]
#john, *the_beatles = [john, paul, george, ringo]


#%%
def demonstrate_annotations(title: str, year_of_release: int) -> str:
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """
    print(title + ', ' + str(year_of_release))
    print(demonstrate_annotations.__annotations__)
    print(demonstrate_annotations.__doc__)
    return f'{demonstrate_annotations.__name__}(\'{title}\', {year})'


#%%
# Test demonstrate_annotations(title, year)
print(demonstrate_annotations(song, year))

#%%
# def show_song(title, author='George Harrison', year: int = 1969):
def show_song(title, author='George Harrison', year=1969):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """
    print(locals())
    print('\n'+ title + ', ' + author + ', ' + str(year))

#%%
# Test show_song(title, author='George Harrison', year=1969)
show_song('Something')
show_song('Something',year = 1970,author='GH') # order is not important as long as we don't confuse it with positional arguement
show_song(year=1970,title='Something',author='GH')


#%%
def use_flexible_arg_list(band: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the type of the 'members' argument
    - print the band name and the list of band members in one line
    """
    # star arguments must come after the positional arguments

    # print(type(members))
    b = band + ':' if members else band
    print(f'{b} {", ".join([member for member in members])}')
#%%
# Test use_flexible_arg_list(band: str, *members)
use_flexible_arg_list('The Beatles', *the_beatles)
print()
use_flexible_arg_list('The Beatles')


#%%
def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print the type of the 'details' argument
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """
    #print(type(details))
    b = band + ':' if members else band
    m = ", ".join([member for member in members])
    a = '(active)' if is_active == True else '(not active)'
    d = ', '.join([str(k) + ':' + str(v) for k, v in details.items()])
    return f'{b}{m} {a}; {d}'

#%%
# Test use_all_categories_of_args(band, *members, is_active=True, **details)
# print(use_all_categories_of_args('The Beatles', is_active=False, start=1962, end=1970))
print(use_all_categories_of_args('The Beatles', *the_beatles, is_active=False, start=1962, end=1970))


