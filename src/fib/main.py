import numpy as np
from fastapi import FastAPI, HTTPException, status


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
    val = 1/np.sqrt(5) * (np.power(((1+np.sqrt(5))/2), n) - np.power(((1-np.sqrt(5))/2), n))
    return int(val)


@app.get("/")
def index(n):
    if not n.isdigit():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enter Integer!")
    val = calculate_fibonacci_num(int(n))
    return val


@app.get("/closed-form")
def index(n):
    if not n.isdigit():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enter Integer!")
    val = closed_form_fib(int(n))
    return val
