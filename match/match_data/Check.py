import sqlite3

# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('matches.db')
cursor = conn.cursor()

# Tạo bảng matches nếu chưa có
cursor.execute('''
CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teamA_logo TEXT NOT NULL,
    teamA_name TEXT NOT NULL,
    teamB_logo TEXT NOT NULL,
    teamB_name TEXT NOT NULL,
    score TEXT,
    match_time TEXT NOT NULL,
    location TEXT NOT NULL,
    video_link TEXT,
    description TEXT,
    comments TEXT
)
''')

# Lưu thay đổi
conn.commit()

conn.close()
