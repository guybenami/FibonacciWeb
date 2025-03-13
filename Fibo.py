import random
import sys
import numpy as np #Need to download numpy if you don't have it. :)
import time

class Fibo:

    @staticmethod
    def recursive(n):
        # Base case: if n is 0 or 1, return n
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return Fibo.recursive(n - 1) + Fibo.recursive(n - 2)
    
    @staticmethod
    def memoization(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        memo[n] = Fibo.memoization(n - 1, memo) + Fibo.memoization(n - 2, memo)
        return memo[n]

    @staticmethod
    def fibonacci_iterative(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def fibonacci_matrix(n):
        if n <= 0:
            return 0
        F = np.matrix([[1, 1], [1, 0]], dtype=object)
        return (F**(n-1))[0, 0]


    def main():
        y = int(input("Please enter the index of n'th number...\n"))
        start1 = time.time()
        Fibo.recursive(y)
        end1 = time.time()
        start2 = time.time()
        Fibo.memoization(y)
        end2 = time.time()
        start3 = time.time()
        Fibo.fibonacci_iterative(y)
        end3 = time.time()
        start4 = time.time()
        x = Fibo.fibonacci_matrix(y)
        end4 = time.time()

        print("The time that " + str(y) + "th number is calculated by recursive method: " + str(end1 - start1))
        print("The time that " + str(y) + "th number is calculated by memoization method: " + str(end2 - start2))
        print("The time that " + str(y) + "th number is calculated by iterative method: " + str(end3 - start3))
        print("The time that " + str(y) + "th number is calculated by matrix method: " + str(end4 - start4))
        print("The number is: " + str(x))
        sys.setrecursionlimit(2000)

if __name__ == "__main__":
    Fibo.main()