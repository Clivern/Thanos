"""
Time and Space Complexity
"""

"""
Time Complexity
===============

Use of time complexity makes it easy to estimate the running time of a program but not the exact time or even an acccurate value
(it depends on the compiler and the type of computer or speed of the processor).

We concentrate on operations that performed the largest number of times. Such operations are referred to as dominant.

=> Which is the dominant operation here?
    def dominant(n):
        result = 0
        for i in xrange(n):
            result += 1
        return result

The operation in line 4 is dominant and will be executed n times. The complexity is described in Big-O notation:
in this case O(n) — linear complexity

Please Note: The program may perform c · n operations, where c is a constant; however, it may not perform n^2 operations, since this involves
a different order of magnitude of data. In other words, when calculating the complexity we omit constants:

i.e. regardless of whether the loop is executed 20 · n times or n/5 times, we still have a complexity of O(n),
even though the running time of the program may vary. When analyzing the complexity we must look for specific,
worst-case examples of data that the program will take a long time to process.


Let’s compare some basic time complexities

* Constant time — O(1) "There is always a fixed number of operations."
    def constant(n):
        result = n * n
        return result


* Logarithmic time — O(log n) "The value of n is halved on each iteration of the loop"
    def logarithmic(n):
        result = 0
        while n > 1:
            n //= 2
            result += 1
        return result


* Linear time — O(n)
    def linear(n, A):
        for i in xrange(n):
            if A[i] == 0:
                return 0
        return 1


* Quadratic time — O(n^2).
    def quadratic(n):
        result = 0
        for i in xrange(n):
            for j in xrange(i, n):
                result += 1
        return result

* Linear time — O(n + m) "Sometimes the complexity depends on more variables (see example below)."
    def linear2(n, m):
        result = 0
        for i in xrange(n):
            result += i
        for j in xrange(m):
            result += j
        return result
"""


"""
Space complexity
================

Space complexity is the amount of memory needed to perform the computation. It includes all the variables, both global and local,
dynamic pointer data-structures and, in the case of recursion, the contents of the stack.

In short, if you have constant numbers of variables, you also have constant space complexity: in Big-O notation this is O(1). If you need to declare
an array with n elements, you have linear space complexity — O(n)
"""


"""
From Brute Force to Fast Solution
=================================

You are given an integer n. Count the total of 1+2+ ... + n.

O(n^2) Time Complexity
    def solution1(n):
        result = 0
        for i in range(1, n+1, 1):
            for k in range(1, i+1, 1):
                result += 1
        return result

O(n) Time Complexity
    def solution2(n):
        result = 0
        for i in range(1, n+1, 1):
            result += i
        return result

O(1) Time Complexity
    def solution3(n):
        result = n * (n + 1) // 2
        return result

O(1) Time Complexity
    def solution4(n):
        return n * (n + 1) // 2


print(solution1(5)) # 15
print(solution2(5)) # 15
print(solution3(5)) # 15
print(solution4(5)) # 15
"""
