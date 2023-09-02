import numpy as np
from fastapi import FastAPI


app = FastAPI()

def calculate_fibonacci_num(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return calculate_fibonacci_num(n-1) + calculate_fibonacci_num(n-2)


def closed_form_fib(n):
    """
    closed form expression to find nth element of fib sequence
    https://en.wikipedia.org/wiki/Fibonacci_sequence
    """

    return 1/np.sqrt(5) * (np.power(((1+np.sqrt(5))/2), n) - np.power(((1-np.sqrt(5))/2), n))


@app.get("/")
def index(n):
    val = calculate_fibonacci_num(int(n))
    return val


@app.get("/closed-form")
def index(n):
    val = closed_form_fib(int(n))
    return val
