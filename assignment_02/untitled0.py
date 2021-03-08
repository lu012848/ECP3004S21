# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Luis Perez
#
# Date:3/8/2021
# 
##################################################
#
# Sample Script for Midterm Exam: 
# Module with Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for a script that you might call
# my_midterm_tests.py (but is not graded).
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

import doctest


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def in_budget(x: int, y: int, p_x: int, p_y: int, w: int) -> bool:
    """
    Preconditions: x, y, w >= 0 and p_x, p_y > 0
    
    Calculates returns a boolean indicator 
    of whether the consumer's expenditure 
    is less than or equal to wealth.
    
    >>> in_budget(3, 1, 10, 25, 100)
    True
    >>> in_budget(1, 5, 9, 15, 500)
    True
    >>> in_budget(10, 6, 9, 31, 100)
    False
    
    """
    if ((x * p_x + y * p_y) < w):
      return True
    else:
      return False

# Exercise 2

def calc_bundle(p_x: int, p_y: int, w: int, alpha: float) -> (float, float):
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    
    >>> calc_bundle(10, 20, 120, 1.0/3.0)
    [4.0, 4.0]
    >>> calc_bundle(5, 15, 32, 1.0/4.0)
    [1.6, 1.6]
    >>> calc_bundle(9, 18, 200, 2.0/5.0)
    [8.9, 8.9]
    
    """
    list = []
    x = alpha / p_x * w
    y = (1 - alpha) / p_y * w
    list.append(round(x, 1))
    list.append(round(x, 1))

    return list



# Exercise 3


def y_solve(x_star: int, p_x: int, p_y: int, w: int) -> float:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= x_star <= w/p_x
    
    Calculates the remaining expenditure on good y, 
    given an expenditure x_star in good x.
    
    >>> y_solve(5, 5, 10, 100)
    7.5
    >>> y_solve(4, 3, 7, 80)
    9.714285714285714
    >>> y_solve(8, 10, 6, 120)
    6.666666666666667
    
    """
    
    return (w - x_star * p_x) / p_y


# Exercise 4


def one_loop_bundle(p_x: int, p_y: int, w: int, alpha: float, step: float) -> (float, float):
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    It searches over a loop on x_star and assigns the remaining
    wealth to y using y_solve.
    
    >>> one_loop_bundle(5, 10, 100, 0.25, 0.01)
    [5.0, 7.5]
    >>> function_name(arguments)
    answer_you_expect
    >>> function_name(arguments)
    answer_you_expect
    
    """
    
    return None



# Exercise 5


def util_in_budget(x: type) -> type:
    """Calculates the value of the Cobb-Douglass utility
    function for consumption goods x and y with exponent alpha.
    It restricts x and y to non-negative values and 
    alpha to the unit interval.
    It also restricts the calculation to bundles [x, y] within budget w, 
    otherwise it assigns zero.
    
    >>> util_in_budget(4, 4, 10, 20, 120, 1.0/3.0)
    4.0
    >>> function_name(arguments)
    answer_you_expect
    >>> function_name(arguments)
    answer_you_expect
    
    """
    
    return None





# Exercise 6


def two_loop_bundle(x: type) -> type:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    It searches over two loops on x_star and y_star.
    
    Note that there is no error handling
    because that is taken care of in util_in_budget() and np.arange(). 
    
    >>> two_loop_bundle(10, 25, 100, 0.5, 0.01)
    [5.0, 2.0]
    >>> function_name(arguments)
    answer_you_expect
    >>> function_name(arguments)
    answer_you_expect
    
    """
    
    return None



# Only function definitions above this point. 



doctest.testmod()


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings above
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# Add code so that the tests are implemented below 
# -- but only when the script is run,
# not when it is imported. 












##################################################
# End
##################################################