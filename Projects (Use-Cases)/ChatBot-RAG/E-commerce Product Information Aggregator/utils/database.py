import sqlite3
import json

def loadMy_data_into_db(json_file, db_path):
    """Load books data from JSON into SQLite database."""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,  -- Changed to numeric for price comparisons
            rating TEXT,
            availability TEXT,
            category TEXT
        )
    ''')
    
    for book in data:
        c.execute('''
            INSERT INTO books (title, price, rating, availability, category)
            VALUES (?, ?, ?, ?, ?)
        ''', (book['title'], float(book['price']), book.get('rating', 'N/A'), book.get('availability', 'N/A'), book.get('category', 'General')))
    
    conn.commit()
    conn.close()

def query_books(query, db_path):
    """Generalized function to query books based on the user's prompt."""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    query = query.lower()
    
    # cheapest books
    if "cheapest" in query:
        c.execute("SELECT title, price, rating, availability FROM books ORDER BY price ASC LIMIT 10")
    # expensive books
    elif "expensive" in query:
        c.execute("SELECT title, price, rating, availability FROM books ORDER BY price DESC LIMIT 10")
    # for category
    elif "category" in query:
        category = query.split("category")[-1].strip()  # Extract category after "category"
        c.execute("SELECT title, price, rating, availability FROM books WHERE category LIKE ?", (f"%{category}%",))
    else:
        # search by title
        c.execute("SELECT title, price, rating, availability FROM books WHERE title LIKE ?", (f"%{query}%",))
    
    results = c.fetchall()
    conn.close()
    return results
