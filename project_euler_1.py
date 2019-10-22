# -*- coding: utf-8 -*-

def problem_statement():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all
    the multiples of 3 or 5 below 1000
    """
    pass    

def triangular_number_solution():
    """
    Intuition here is that we can restate problem as the following
    sum1000 = 5(1+...+199) + 3(1+...+333) - 15(1+...+66)
    """
    return 5 * partial_sum(199) + 3 * partial_sum(333) - 15 * partial_sum(66)

def partial_sum(n):
    return n*(n+1)/2

def brute_force_solution():
    total = 0
    for i in range(0, 1000):
        if (i%3 == 0 and i%5 == 0):
            total+=i
            continue
        if (i%3 == 0 or i%5 == 0):
            total+=i
    return total

if __name__=="__main__":
    print(triangular_number_solution())