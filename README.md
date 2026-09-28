# Secure Calculator

A simple Python calculator used as a playground for learning CI/CD and DevSecOps.

## Run it

    python calculator.py

## Run the tests

    pip install -r requirements.txt
    pytest -v

## Pipeline

Every push and pull request runs a GitHub Actions workflow that lints the code
with Ruff and runs the test suite with pytest.
