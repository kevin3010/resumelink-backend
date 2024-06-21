# Project Setup

Follow these steps to set up your environment:

1. **Create a virtual environment:**

    ```bash
    python -m venv .venv
    ```

2. **Activate the virtual environment:**

    On Windows:

    ```bash
    .venv\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source .venv/bin/activate
    ```

3. **Install the requirements:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the server:**

    ```bash
    uvicorn main:app --reload
    ```

5. **Run the tests:**

    Open a new terminal and activate the virtual environment as described in step 2. Then run the tests with your preferred test runner. For example, if you're using pytest:

    ```bash
    pytest -s test.py
    ```

Remember to replace `pytest` with your actual test command if it's different.

