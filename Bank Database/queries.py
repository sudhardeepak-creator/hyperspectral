"""
queries.py

Runs the three required retrieval queries against bank.db:
    1. List details of all customers
    2. Find all customers and their account details (JOIN)
    3. List all transactions
"""

import sqlite3

def run_queries():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    # ---------- QUERY 1: List all customers ----------
    print("\n--- 1. All Customers ---")
    cursor.execute("SELECT * FROM customers;")
    for row in cursor.fetchall():
        print(row)

    # ---------- QUERY 2: Customers + their account details (JOIN) ----------
    print("\n--- 2. Customers with Account Details ---")
    cursor.execute("""
        SELECT customers.customer_id, customers.name, customers.address, customers.email,
               accounts.account_id, accounts.account_type, accounts.balance
        FROM customers
        JOIN accounts ON customers.customer_id = accounts.customer_id;
    """)
    for row in cursor.fetchall():
        print(row)

    # ---------- QUERY 3: List all transactions ----------
    print("\n--- 3. All Transactions ---")
    cursor.execute("SELECT * FROM transactions;")
    for row in cursor.fetchall():
        print(row)

    conn.close()


if __name__ == "__main__":
    run_queries()
