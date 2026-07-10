# Bank Database Management System

A Python + SQLite project that models core banking operations through a normalized relational database. Built to practice database design, SQL querying, and Python-database integration — skills directly applicable to QA and test automation roles.

## Overview

The system manages three interrelated entities:

- **Customers** — personal and contact details
- **Accounts** — linked to customers, holding balance and account type
- **Transactions** — deposits and withdrawals linked to accounts

Referential integrity is enforced through primary and foreign key constraints across all three tables.

## Schema

**customers**
| Column | Type | Constraint |
|---|---|---|
| customer_id | INTEGER | PRIMARY KEY |
| name | TEXT | NOT NULL |
| address | TEXT | |
| email | TEXT | |

**accounts**
| Column | Type | Constraint |
|---|---|---|
| account_id | INTEGER | PRIMARY KEY |
| customer_id | INTEGER | FOREIGN KEY → customers |
| account_type | TEXT | CHECK: 'savings' or 'current' |
| balance | REAL | NOT NULL |

**transactions**
| Column | Type | Constraint |
|---|---|---|
| transaction_id | INTEGER | PRIMARY KEY |
| account_id | INTEGER | FOREIGN KEY → accounts |
| transaction_type | TEXT | CHECK: 'deposit' or 'withdraw' |
| amount | REAL | NOT NULL |
| transaction_date | TEXT | NOT NULL |

## Project Structure

```
bank-database-project/
├── create_db.py     # Creates bank.db and defines all three tables (DDL)
├── insert_data.py   # Seeds sample data into all three tables (DML)
├── queries.py        # Runs retrieval queries, including a multi-table JOIN
└── README.md
```

## Setup & Usage

Requires only Python 3 — `sqlite3` is part of the standard library, no external packages needed.

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/bank-database-project.git
cd bank-database-project

# 2. Create the database and tables
python create_db.py

# 3. Insert sample data
python insert_data.py

# 4. Run the queries
python queries.py
```

Running the steps above generates a local `bank.db` SQLite file and prints the results of three queries to the console.

## Sample Queries Included

1. **List all customers** — full customer table dump
2. **Customers with account details** — INNER JOIN across `customers` and `accounts`
3. **List all transactions** — full transaction history

## Key Concepts Demonstrated

- Relational schema design with primary/foreign key constraints
- DDL and DML scripting in Python via `sqlite3`
- Parameterized inserts using `executemany()`
- Multi-table JOIN queries for relational data retrieval
- Modular script structure separating schema, seeding, and querying concerns

## Possible Extensions

- Add update/delete operations for accounts and transactions
- Add input validation and error handling for invalid transaction types
- Write `pytest` unit tests to validate query outputs against expected data
- Migrate from SQLite to MySQL/PostgreSQL for a production-style setup

## Author

**Sudharshan M**
[LinkedIn](#) | [GitHub](#)
