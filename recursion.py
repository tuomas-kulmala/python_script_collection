#!/usr/bin/env python

__author__ = Tuomas Kulmala"
__copyright__ = "Tuomas Kulmala"
__credits__ = "Tuomas Kulmala"
__license__ = "Public Domain"
__version__ = "0.0.1"
__maintainer__ = "Tuomas Kulmala"
__email__ = "sufa@qscrum.com"
__status__ = "Test"

# init_list = empty list to be passed to recursive loop
# n = number of columns (basically size of init_list)
# x = lowest number to be put to list
# y = highest number to be put to the list


# Print all possible combinations for given numbers
def recursive(init_list,n,x,y):
    for i in range(x,y):
        if n == 0:
            init_list[n]=str(i)
            print(init_list)
        else:
            init_list[n] = str(i)
            recursive(init_list,n-1,x,y)


# Example
recursive(['',''],1,0,10)