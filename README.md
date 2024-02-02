# SQL Injection and Secure SQL Example

This repository contains two Python scripts, one demonstrating SQL Injection vulnerability and the other fixing the issue to ensure secure SQL queries.

## SQL Injection (insecure_sql.py)

The `insecure_sql.py` script illustrates a scenario where SQL Injection is possible. Here's how it works:

1. Establish a connection to the MySQL database using the `mysql.connector` library.
2. Simulate SQL Injection by setting the `nome_produto` variable to `"chocolate' OR '1'='1"`.
3. Create an SQL query with the vulnerable string concatenation method.
4. Execute the SQL query with the vulnerable input.

This script shows how an attacker can exploit the vulnerability to manipulate the SQL query and potentially gain unauthorized access or manipulate data in the database.

## Secure SQL (secure_sql.py)

The `secure_sql.py` script demonstrates the secure way to interact with a database, preventing SQL Injection. Here's how it works:

1. Establish a connection to the MySQL database using the `mysql.connector` library.
2. Define safe input values for `nome_produto` and `valor`.
3. Create an SQL query with parameterized placeholders.
4. Execute the SQL query with the safe input using parameter binding.

This script showcases the recommended approach to protect against SQL Injection attacks by using parameterized queries.

## Usage

To run the scripts:

1. Make sure you have Python installed.
2. Install the `mysql-connector-python` library if not already installed: `pip install mysql-connector-python`.
3. Modify the database connection details in each script (e.g., host, user, password, database).
4. Execute `insecure_sql.py` and `secure_sql.py` separately to observe the differences.

Please ensure that you have the appropriate MySQL database and table structure in place for these scripts to work correctly.

## Security Note

Always use the secure SQL approach (parameterized queries) to prevent SQL Injection vulnerabilities in your applications. The `secure_sql.py` script demonstrates best practices for handling database queries securely.

---

Feel free to explore the scripts and learn about SQL Injection vulnerabilities and how to protect your applications from such security risks.
