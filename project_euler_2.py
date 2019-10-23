# -*- coding: utf-8 -*-
"""
@author: lask01
"""
def problem_statement():
    """
    By considering the terms in the Fibonacci sequence whose values do not
    exceed 4 million, find the sum of the even-valued terms.
    """
    pass

def dynamic_programming_solution(max_value):
    """
    Space efficient dynamic programming solution
    """
    
    # For simplification
    assert(max_value > 2)

    sum_fib = 0    
    n_minus_two = 0
    n_minus_one = 1
    n = n_minus_two + n_minus_one
    
    while n < max_value:
         n = n_minus_two + n_minus_one
         n_minus_two = n_minus_one
         n_minus_one = n
         if n%2 == 0:
             sum_fib += n
    return sum_fib

if __name__=="__main__":
    print(dynamic_programming_solution(4*(10**6)))
    
