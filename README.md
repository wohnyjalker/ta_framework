# Test Automation Framework

This repository contains a test automation framework written in Python. It includes the necessary setup steps and instructions to run the tests using different configurations.

## TODO
* add Allure Reporting
* add screenshots on fail
* add video recording on rerun

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/wohnyjalker/ta_framework.git test-automation-framework
   cd test-automation-framework


2. Copy the .env.example file as .env:
    ```bash
    cp .env.example .env
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```


## Running Tests Locally

To run the tests locally, use the following command:
```bash
pytest -n 4
```
The -n 4 flag specifies the number of parallel workers to use. Adjust the value as per your machine's capabilities.

## Using Docker and Selenium Grid

1. Make sure you have Docker installed and running on your machine.

2. Run the tests using the provided run_tests.sh script:

    ```bash
    ./run_tests.sh
    ```
