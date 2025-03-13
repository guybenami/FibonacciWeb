from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import numpy as np

app = Flask(__name__)
CORS(app)

class Fibo:
    @staticmethod
    def recursive(n):
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
        return (F ** (n - 1))[0, 0]


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    n = int(data.get('number', 0))

    start1 = time.time()
    # Recursive method is not used for large numbers to avoid long execution time
    fib_recursive = Fibo.recursive(n) if n < 20 else "Too slow for large numbers"
    end1 = time.time()

    start2 = time.time()
    fib_memo = Fibo.memoization(n)
    end2 = time.time()

    start3 = time.time()
    fib_iterative = Fibo.fibonacci_iterative(n)
    end3 = time.time()

    start4 = time.time()
    fib_matrix = Fibo.fibonacci_matrix(n)
    end4 = time.time()

    return jsonify({
        "recursive": {"value": fib_recursive, "time": end1 - start1},
        "memoization": {"value": fib_memo, "time": end2 - start2},
        "iterative": {"value": fib_iterative, "time": end3 - start3},
        "matrix": {"value": fib_matrix, "time": end4 - start4}
    })


if __name__ == '__main__':
    app.run(debug=True)
