from functools import lru_cache
from fastapi import FastAPI, HTTPException, status


app = FastAPI()


@lru_cache
def calculate_fibonacci_num(n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError
    if n == 1:
        return 1
    if n == 2:
        return 1
    return calculate_fibonacci_num(n-1) + calculate_fibonacci_num(n-2)


@lru_cache
def calculate_fibonacci_num_iterative(n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError
    if n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


@app.get("/")
def get_nth_num_recursive(n):
    if not n.isdigit():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enter Integer!")
    val = calculate_fibonacci_num(int(n))
    return val


@app.get("/iterative")
def get_nth_num_iterative(n):
    if not n.isdigit():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enter Integer!")
    val = calculate_fibonacci_num_iterative(int(n))
    return val
