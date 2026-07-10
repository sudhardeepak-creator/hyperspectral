"""
create_db.py

Creates (or connects to) bank.db and defines the three tables required
for the Bank Database project:
    1. customers
    2. accounts   (foreign key -> customers)
    3. transactions (foreign key -> accounts)
"""

import sqlite3

def create_database():
    # If bank.db doesn't exist, this creates it. If it exists, it just connects.
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    # Enforce foreign key constraints (SQLite has this off by default)
    cursor.execute("PRAGMA foreign_keys = ON;")

    # ---------- 1. CUSTOMERS TABLE ----------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name        TEXT NOT NULL,
            address     TEXT,
            email       TEXT
        );
    """)

    # ---------- 2. ACCOUNTS TABLE ----------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_id   INTEGER PRIMARY KEY,
            customer_id  INTEGER NOT NULL,
            account_type TEXT CHECK (account_type IN ('savings', 'current')),
            balance      REAL NOT NULL DEFAULT 0,
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
        );
    """)

    # ---------- 3. TRANSACTIONS TABLE ----------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id   INTEGER PRIMARY KEY,
            account_id       INTEGER NOT NULL,
            transaction_type TEXT CHECK (transaction_type IN ('deposit', 'withdraw')),
            amount           REAL NOT NULL,
            transaction_date TEXT NOT NULL,
            FOREIGN KEY (account_id) REFERENCES accounts (account_id)
        );
    """)

    conn.commit()
    conn.close()
    print("Database 'bank.db' created successfully with tables: customers, accounts, transactions.")


if __name__ == "__main__":
    create_database()
