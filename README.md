
Fibonacci API
========

Fibonacci API will implement and deploy an API that calculates the n-th Fibonacci number
for a given input number n.

📖 Documentation is available at [Docs](https://fatemetardasti96.github.io/fibonacci-api/)


Start the server on your localhost by building a docker image and run it on port 81:

    cd fibonacci_api_peoject
    docker build -t fibonacci_api .
    docker run -p 81:8081 fibonacci_api

You can now find the n-th fibonacci number by sending a request to the server:

    curl http://0.0.0.0:81/?n=7

OR

    curl http://0.0.0.0:81/iterative/?n=7


Installation
------------

Install project from source by running:

    cd fibonacci_api_peoject
    pip install -r requirements.txt
    uvicorn src.fibonacci_api.main:app --host 0.0.0.0 --port 81 --reload

API Endpoints
-------------
[`GET /`] This endpoint uses the recursive algorithm to find the n-th number of the series.

[`GET /iterative`] This endpoint uses the iterative algorithm to find the n-th number of the series.


Contribute
----------
To set up your local development environment, please use a fresh virtual environment,
then run

    pip install -r requirements-dev.txt

We use pytest as test framework. To execute the tests, please run

    pytest

Access API docs from

    0.0.0.0:81/docs

Before contributing code, please set up the pre-commit hooks to reduce errors
and ensure consistency

    pre-commit run -a

- Issue Tracker: github.com/fatemetardasti96/fibonacci-api/issues
- Source Code: github.com/fatemetardasti96/fibonacci-api

Support
-------

If you are having issues, please let us know.
We have a mailing list located at: ftardasti96@gmail.com

License
-------

The project is licensed under the BSD license.
