import sqlite3

# Kết nối với cơ sở dữ liệu
conn = sqlite3.connect('matches.db')
cursor = conn.cursor()

# Cập nhật tỉ số của trận đấu (ví dụ cập nhật trận đấu có id = 2)
match_id_to_update = 2
new_score = '2:3'  # Tỉ số mới
cursor.execute('''
UPDATE matches
SET score = ?
WHERE match_id = ?
''', (new_score, match_id_to_update))

# Lưu thay đổi
conn.commit()
print(f"Tỉ số trận đấu với ID {match_id_to_update} đã được cập nhật thành {new_score}.")

# Đóng kết nối
conn.close()
