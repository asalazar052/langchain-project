# test_chintook_queries.py

from langchain.sql_database import SQLDatabase

# Load the SQLite DB (adjust path if needed)
db = SQLDatabase.from_uri("sqlite:///chinook.db")

def run_and_print(title, query):
    print(f"\n🔹 {title}")
    print("SQL:")
    print(query.strip())
    try:
        result = db.run(query)
        print("Result:")
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("✅ Connected to Chinook DB.")

    # Print tables just for sanity
    tables = db.get_usable_table_names()
    print("\n📋 Tables in DB:")
    for table in tables:
        print(f" - {table}")

    # Test 1: Count of customers
    run_and_print("Test 1: Total number of customers", """
        SELECT COUNT(*) FROM Customer;
    """)

    # Test 2: Top 5 most expensive tracks
    run_and_print("Test 2: Top 5 tracks by unit price", """
        SELECT Name, UnitPrice FROM Track ORDER BY UnitPrice DESC LIMIT 5;
    """)

    # Test 3: Customers from Brazil
    run_and_print("Test 3: Customers from Brazil", """
        SELECT FirstName, LastName, Country FROM Customer WHERE Country = 'Brazil';
    """)

    # Test 4: Total revenue
    run_and_print("Test 4: Total revenue from all invoices", """
        SELECT SUM(Total) FROM Invoice;
    """)

    # Test 5: Country with the most invoices
    run_and_print("Test 5: Most frequent billing country", """
        SELECT BillingCountry, COUNT(*) as Count 
        FROM Invoice 
        GROUP BY BillingCountry 
        ORDER BY Count DESC 
        LIMIT 1;
    """)

if __name__ == "__main__":
    main()