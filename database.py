import sqlite3

class DatabaseManager:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        category TEXT,
                        description TEXT,
                        amount REAL
                    )"""
        self.conn.execute(query)
        self.conn.commit()

    def insert_expense(self, date, category, description, amount):
        self.conn.execute(
            "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
            (date, category, description, amount),
        )
        self.conn.commit()

    def fetch_all_expenses(self):
        return self.conn.execute("SELECT * FROM expenses").fetchall()

    def delete_expense(self, expense_id):
        self.conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        self.conn.commit()

    def total_by_category(self):
        query = "SELECT category, SUM(amount) FROM expenses GROUP BY category"
        return self.conn.execute(query).fetchall()
