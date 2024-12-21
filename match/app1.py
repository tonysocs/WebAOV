from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/match/<int:match_id>')
def match_detail(match_id):
    print(f"match_id: {match_id}")  # In ra giá trị match_id để kiểm tra
    conn = get_db_connection()
    match = conn.execute('SELECT * FROM matches WHERE match_id = ?', (match_id,)).fetchone()
    conn.close()
    if match is None:
        return "<h1>Trận đấu không tồn tại!</h1>", 404
    return render_template('template_page.html', match=match)
