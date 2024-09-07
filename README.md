# Bank Management System

A web-based banking system using Flask and MySQL for user account management.

## Features

- **User Registration**: Create accounts with unique usernames and passwords.
- **User Login**: Access your account with credentials.
- **Account Management**:
  - Deposit funds
  - Withdraw funds
  - Check balance
- **Database**: User details and balances are stored in MySQL.

## Requirements

- Python 3.x
- Flask
- MySQL

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/CG11CG/Bank-Management-System.git
    cd Bank-Management-System
    ```

2. **Create and Activate a Virtual Environment**:
    - **Create**:
      ```bash
      python -m venv venv
      ```
    - **Activate**:
      - **Windows**:
        ```bash
        venv\Scripts\activate
        ```
      - **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up MySQL Database**:
    - Create a database named `bank_management`.
    - Set up the `users` table with the following SQL command:
      ```sql
      CREATE TABLE users (
          id INT AUTO_INCREMENT PRIMARY KEY,
          username VARCHAR(100) NOT NULL,
          password VARCHAR(100) NOT NULL,
          balance DECIMAL(10, 2) DEFAULT 0.00,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
      ```

5. **Update Database Configuration**:
    - Edit `main.py` to include your MySQL credentials:
      ```python
      db_config = {
          'user': 'your_mysql_username',
          'password': 'your_mysql_password',
          'host': 'localhost',
          'database': 'bank_management'
      }
      ```

6. **Run the Flask Application**:
    ```bash
    flask run
    ```

7. **Access the Application**:
    Open your browser and navigate to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

    


