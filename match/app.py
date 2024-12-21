from flask import Flask, render_template, request, url_for
import sqlite3
import os

app = Flask(__name__)

# Xác định đường dẫn tới cơ sở dữ liệu
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'match_data', 'matches.db')
print(f"Database path: {db_path}")

def get_db_connection():
    try:
        print("Attempting to connect to database...")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        print("Connection successful!")
        return conn
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None

@app.route('/')
def home():
    return "Welcome to the Match Info App!"

@app.route('/match/<int:match_id>')
def match_detail(match_id):
    print(f"Function match_detail is called with match_id: {match_id}")
    conn = get_db_connection()
    if not conn:
        return "Error: Unable to connect to database", 500

    try:
        match = conn.execute("SELECT * FROM matches WHERE match_id = ?", (match_id,)).fetchone()
        print(f"Match data retrieved: {match}")
        if not match:
            return f"Error: No match found with id {match_id}", 404
        return render_template('template_page.html', match=match)
    except sqlite3.Error as e:
        print(f"Error during query execution: {e}")
        return "Error: Query execution failed", 500
    finally:
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    app.run(debug=True)
