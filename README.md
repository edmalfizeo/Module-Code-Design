# **Calculators API**

The **Calculators API** is a Python Flask-based application providing multiple endpoints for performing various calculations. Each calculator is designed with modular architecture, ensuring scalability, maintainability, and adherence to software development best practices.

---

## **Requirements**

blinker==1.9.0
click==8.1.7
colorama==0.4.6
Flask==3.1.0
iniconfig==2.0.0
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==3.0.2
numpy==2.1.3
packaging==24.2
pluggy==1.5.0
pytest==8.3.3
Werkzeug==3.1.3

---

## **Setup Instructions**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/edmalfizeo/Module-Code-Design.git
   cd Module-Code-Design
   ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python ./run.py
    ```

## **About**

The **Calculators API** is a comprehensive application designed to handle various types of calculations through dedicated endpoints. It demonstrates:

- **Clean Architecture Principles**: Separation of concerns and modular design.
- **Robust Error Handling**: Graceful management of invalid inputs and descriptive error messages.
- **Test-Driven Development (TDD)**: Ensuring reliability and maintainability through extensive unit testing.
- **Scalability**: A factory pattern and driver handler interface allow for the easy addition of new calculators or functionalities.
