import sqlite3
import os

# Xác định thư mục chứa file hiện tại
base_dir = os.path.dirname(os.path.abspath(__file__))

# Đảm bảo đường dẫn đúng tới cơ sở dữ liệu trong thư mục match_data
db_path = os.path.join(base_dir, 'matches.db')

# In ra đường dẫn để kiểm tra
print(f"Đường dẫn tới cơ sở dữ liệu: {db_path}")

# Kết nối với cơ sở dữ liệu
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Xóa trận đấu theo match_id (ví dụ xóa trận đấu có id = 1)
match_id_to_delete = 2
cursor.execute("DELETE FROM matches WHERE match_id = ?", (match_id_to_delete,))

# Lưu thay đổi
conn.commit()
print(f"Trận đấu với ID {match_id_to_delete} đã bị xóa.")

# Đóng kết nối
conn.close()
