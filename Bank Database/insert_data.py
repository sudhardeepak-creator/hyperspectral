"""
insert_data.py

Inserts sample data into the customers, accounts, and transactions tables.
Run create_db.py first so the tables exist.
"""

import sqlite3

def insert_sample_data():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # ---------- CUSTOMERS ----------
    customers = [
        (1, "Rohan Mehta",   "Chennai, India",   "rohan.mehta@example.com"),
        (2, "Priya Nair",    "Bengaluru, India", "priya.nair@example.com"),
        (3, "Arjun Sharma",  "Mumbai, India",    "arjun.sharma@example.com"),
        (4, "Sneha Iyer",    "Hyderabad, India", "sneha.iyer@example.com"),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO customers (customer_id, name, address, email) VALUES (?, ?, ?, ?);",
        customers
    )

    # ---------- ACCOUNTS ----------
    # (account_id, customer_id, account_type, balance)
    accounts = [
        (101, 1, "savings", 25000.00),
        (102, 2, "current", 50000.00),
        (103, 3, "savings", 12000.00),
        (104, 4, "current", 8000.00),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO accounts (account_id, customer_id, account_type, balance) VALUES (?, ?, ?, ?);",
        accounts
    )

    # ---------- TRANSACTIONS ----------
    # (transaction_id, account_id, transaction_type, amount, transaction_date)
    transactions = [
        (1001, 101, "deposit",  5000.00, "2026-01-05"),
        (1002, 101, "withdraw", 2000.00, "2026-01-10"),
        (1003, 102, "deposit", 10000.00, "2026-02-01"),
        (1004, 102, "withdraw", 3000.00, "2026-02-15"),
        (1005, 103, "deposit",  1500.00, "2026-03-03"),
        (1006, 103, "withdraw",  500.00, "2026-03-20"),
        (1007, 104, "deposit",  2000.00, "2026-04-11"),
        (1008, 104, "withdraw", 1000.00, "2026-04-25"),
    ]
    cursor.executemany(
        """INSERT OR IGNORE INTO transactions
           (transaction_id, account_id, transaction_type, amount, transaction_date)
           VALUES (?, ?, ?, ?, ?);""",
        transactions
    )

    conn.commit()
    conn.close()
    print("Sample data inserted successfully into customers, accounts, and transactions.")


if __name__ == "__main__":
    insert_sample_data()
