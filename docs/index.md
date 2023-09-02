
Fibonacci API
========

The Fibonacci sequence is the series of numbers:

    1, 1, 2, 3, 5, 8, 13, ...

The next number is found by summing of the two previous numbers.

The Fibonacci API will implement and deploy an API that calculates the n-th Fibonacci number
for a given input number n.

There are multiple approaches to compute the n-th number of the sequence.
Here two algorithms are implemented: recursive and iterative.

API Endpoints
-------------
[`GET /`] This endpoint uses the iterative algorithm to find the n-th number of the series.

[`GET /recursive`] This endpoint uses the recursive algorithm to find the n-th number of the series.


Access API docs from

    0.0.0.0:81/docs
