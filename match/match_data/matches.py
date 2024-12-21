import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))  

db_path = os.path.join(base_dir, 'matches.db')

# Kết nối hoặc tạo cơ sở dữ liệu
conn = sqlite3.connect(db_path)

# Tạo cursor để thực thi các lệnh SQL
cursor = conn.cursor()

# Tạo bảng matches với các trường như yêu cầu
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

# Thêm hai trận đấu mẫu vào cơ sở dữ liệu
cursor.execute('''
INSERT INTO matches (teamA_logo, teamA_name, teamB_logo, teamB_name, score, match_time, location, video_link, description, comments)
VALUES
    ('image/Rmit_logo.png', 'ĐH RMIT SGS', 'image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', '1-2', '2024-09-09', 'stadium A', 'https://www.youtube.com/embed/9CcSiqqRfj8?si=Ke2qCHJ9ogyqZxCG&amp;start=1118', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Nam_can_tho_logo.png', 'ĐH Nam Cần Thơ', 'image/ĐH_Can_tho_logo.png', 'ĐH Cần Thơ', '2-0', '2024-09-09', 'stadium A', 'https://www.youtube.com/embed/9CcSiqqRfj8?si=zAdYhAv3uuYWjJ-a&amp;start=9621', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Hutech_logo.png', 'Trường Đại học Công Nghệ TPHCM', 'image/NEU_logo.png', 'Trường Đại học Kinh Tế Quốc Dân', '1-1', '2024-12-11 20:00', 'Stadium B', 'https://www.youtube.com/embed/9CcSiqqRfj8?si=b4HVb7mUHN4oQzPP&amp;start=14293', 'A close game between Team A2 and Team B2', 'Intense match with a draw.'),
    ('image/Logo_ute-removebg-preview.png', 'Trường ĐH Sư Phạm Kĩ Thuật', 'image/UTH-logo.png', 'Trường ĐH Giao Thông Vận Tải TPHCM', '3-2', '2024-12-10 18:00', 'Stadium A', 'https://www.youtube.com/embed/9CcSiqqRfj8?si=gTbAcfAJC1rZHNyO&amp;start=19425', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Dong_thap_logo.png', 'Đồng Tháp', 'image/Ninh_thuan_logo.png', 'Ninh Thuận', '2-0', '10-09-2024', 'stadium A', 'https://www.youtube.com/embed/nu5Ngua9kHY?si=pKr1UjI_M53d9R82&amp;start=1104', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Dat_lak_logo.png', 'Đắk Lắk', 'image/Thai_nguyen_logo.png', 'Thái Nguyên', '2-0', '10-09-2024', 'stadium A', 'https://www.youtube.com/embed/nu5Ngua9kHY?si=wRebgf_x7_zR70nf&amp;start=5544', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Binh_duong_logo.png', 'Bình Dương', 'image/Phu_tho_logo.png', 'Phú Thọ', '2-1', '10-09-2024', 'stadium A', 'https://www.youtube.com/embed/nu5Ngua9kHY?si=p73_iSREOH_TY2o8&amp;start=9831', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),          
    ('image/Hai_phong_logo.png', 'Hải Phòng', 'image/Can_tho_logo.png', 'Cần Thơ', '0-2', '10-09-2024', 'stadium A', 'https://www.youtube.com/embed/nu5Ngua9kHY?si=M6ZfNMnjdZp3sNho&amp;start=17605', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Rmit_logo.png', 'ĐH RMIT SGS', 'image/ĐH_Can_tho_logo.png', 'ĐH Cần Thơ', '0-2', '11-09-2024', 'stadium A', 'https://www.youtube.com/embed/Hor71ZLvraQ?si=H1gqV9YIC2V4HmrR&amp;start=4', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/NEU_logo.png', 'ĐH Kinh Tế Quốc Dân', 'image/UTH-logo.png', 'ĐH Giao Thông Vận Tải TP.HCM', '1-2', '11-09-2024', 'stadium A', 'https://www.youtube.com/embed/Hor71ZLvraQ?si=EcpMTZcMEqpYvK7V&amp;start=5628', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', 'image/Nam_can_tho_logo.png', 'ĐH Nam Cần Thơ', '2-0', '11-09-2024', 'stadium A', 'https://www.youtube.com/embed/Hor71ZLvraQ?si=38qIMwmbyHtI6w4A&amp;start=13149', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/NEU_logo.png', 'ĐH Kinh Tế Quốc Dân', 'image/Logo_ute-removebg-preview.png', 'ĐH Sư Phạm Kỹ Thuật TP.HCM', '2-0', '11-09-2024', 'stadium A', 'https://www.youtube.com/embed/Hor71ZLvraQ?si=Xn5nvPTH9fmal7mE&amp;start=17802', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Phu_tho_logo.png', 'Phú Thọ', 'image/Hai_phong_logo.png', 'Hải Phòng', '2-1', '16-09-2024', 'stadium A', 'https://www.youtube.com/embed/nZtBxvotUrM?si=wsS_Do0mSqH3ruZR&amp;start=1071', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Ninh_thuan_logo.png', 'Ninh Thuận', 'image/Thai_nguyen_logo.png', 'Thái Nguyên', '2-0', '16-09-2024', 'stadium A', 'https://www.youtube.com/embed/nZtBxvotUrM?si=6lTi466IavmkCZOm&amp;start=8882', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Binh_duong_logo.png', 'Bình Dương', 'image/Can_tho_logo.png', 'Cần Thơ', '1-2', '16-09-2024', 'stadium A', 'https://www.youtube.com/embed/nZtBxvotUrM?si=21VMQ4t3EIfpLOCV&amp;start=14200', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Dong_thap_logo.png', 'Đồng Tháp', 'image/Dat_lak_logo.png', 'Đắk Lắk', '2-1', '16-09-2024', 'stadium A', 'https://www.youtube.com/embed/nZtBxvotUrM?si=Kx-Ck9j3k_fHO9Sr&amp;start=21355', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Nam_can_tho_logo.png', 'ĐH Nam Cần Thơ', 'image/ĐH_Can_tho_logo.png', 'ĐH Cần Thơ', '3-1', '17-09-2024', 'stadium A', 'https://www.youtube.com/embed/c-IOTjYrS7g?si=Mkr_WPal8FbM9byY&amp;start=560', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Logo_ute-removebg-preview.png', 'ĐH Sư Phạm Kỹ Thuật TP.HCM', 'image/UTH-logo.png', 'ĐH Giao Thông Vận Tải TP.HCM', '3-1', '17-09-2024', 'stadium A', 'https://www.youtube.com/embed/c-IOTjYrS7g?si=0sJZtojoujQOqbIV&amp;start=9293', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', 'image/Hutech_logo.png', 'ĐH Công nghệ TP.HCM', '1-3', '17-09-2024', 'stadium A', 'https://www.youtube.com/embed/c-IOTjYrS7g?si=HRF3Vl0jq2QX_CyD&amp;start=18956', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Can_tho_logo.png', 'Cần Thơ', 'image/Dong_thap_logo.png', 'Đồng Tháp', '3-1', '18-09-2024', 'stadium A', 'https://www.youtube.com/embed/b5ck9xqjWcA?si=twogyajABuDQzJX_&amp;start=587', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Binh_duong_logo.png', 'Bình Dương', 'image/Phu_tho_logo.png', 'Phú Thọ', '3-1', '18-09-2024', 'stadium A', 'https://www.youtube.com/embed/b5ck9xqjWcA?si=4RYr24kayfO1V-qi&amp;start=10607', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Dat_lak_logo.png', 'Đắk Lắk', 'image/Ninh_thuan_logo.png', 'Ninh Thuận', '3-1', '18-09-2024', 'stadium A', 'https://www.youtube.com/embed/b5ck9xqjWcA?si=KRJy0XCGdKVBfFS6&amp;start=21004', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Rmit_logo.png', 'ĐH RMIT SGS', 'image/NEU_logo.png', 'ĐH Kinh Tế Quốc Dân', '1-3', '24-09-2024', 'stadium A', 'https://www.youtube.com/embed/EsiZCxgXZac?si=MXEF5f4KTZdp1PzP&amp;start=1419', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Thai_nguyen_logo.png', 'Thái Nguyên', 'image/Hai_phong_logo.png', 'Hải Phòng', '1-3', '24-09-2024', 'stadium A', 'https://www.youtube.com/embed/EsiZCxgXZac?si=rJ3ZwZpFQbCmuJpE&amp;start=11056', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', 'image/Logo_ute-removebg-preview.png', 'ĐH Sư Phạm Kỹ Thuật TP.HCM', '2-1', '25-09-2024', 'stadium A', 'https://www.youtube.com/embed/YohA64YYlD8?si=1QuI58kBobAmu0kD&amp;start=1944', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Nam_can_tho_logo.png', 'ĐH Nam Cần Thơ', 'image/Logo_ute-removebg-preview.png', 'ĐH Sư Phạm Kỹ Thuật TP.HCM', '0-2', '25-09-2024', 'stadium A', 'https://www.youtube.com/embed/YohA64YYlD8?si=MNesertUtmO9hiSo&amp;start=8463', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', 'image/Nam_can_tho_logo.png', 'ĐH Nam Cần Thơ', '2-0', '25-09-2024', 'stadium A', 'https://www.youtube.com/embed/YohA64YYlD8?si=BGUyB3HdwtDf4oCI&amp;start=12658', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Dong_thap_logo.png', 'Đồng Tháp', 'image/Dat_lak_logo.png', 'Đắk Lắk', '0-2', '26-09-2024', 'stadium A', 'https://www.youtube.com/embed/bZMfkUwDJcI?si=zvr4t7Qno5b9K4jO&amp;start=812', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Dong_thap_logo.png', 'Đồng Tháp', 'image/Binh_duong_logo.png', 'Bình Dương', '0-2', '26-09-2024', 'stadium A', 'https://www.youtube.com/embed/bZMfkUwDJcI?si=j8MyLb9PgnoiUYB8&amp;start=5896', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Binh_duong_logo.png', 'Bình Dương', 'image/Dat_lak_logo.png', 'Đắk Lắk', '0-2', '26-09-2024', 'stadium A', 'https://www.youtube.com/embed/bZMfkUwDJcI?si=7mRxYm46h9IXDDDl&amp;start=11138', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/ĐH_Can_tho_logo.png', 'ĐH Cần Thơ', 'image/UTH-logo.png', 'ĐH Giao Thông Vận Tải TP.HCM', '1-2', '27-09-2024', 'stadium A', 'https://www.youtube.com/embed/UUBUGsA5Ubk?si=MlpsFvRPfXXwnyxB&amp;start=2226', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/ĐH_Can_tho_logo.png', 'ĐH Cần Thơ', 'image/NEU_logo.png', 'ĐH Kinh Tế Quốc Dân', '2-1', '27-09-2024', 'stadium A', 'https://www.youtube.com/embed/UUBUGsA5Ubk?si=xw23XqXpjDJsJsb-&amp;start=8716', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/NEU_logo.png', 'ĐH Kinh Tế Quốc Dân', 'image/UTH-logo.png', 'ĐH Giao Thông Vận Tải TP.HCM', '1-2', '27-09-2024', 'stadium A', 'https://www.youtube.com/embed/UUBUGsA5Ubk?si=TVKOQN57k4DP8PaG&amp;start=6420', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Phu_tho_logo.png', 'Phú Thọ', 'image/Ninh_thuan_logo.png', 'Ninh Thuận', '2-1', '28-09-2024', 'stadium A', 'https://www.youtube.com/embed/Kj2RMOGbdQ0?si=smkTPSGt1w27u0DP&amp;start=1854', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Hai_phong_logo.png', 'Hải Phòng', 'image/Ninh_thuan_logo.png', 'Ninh Thuận', '2-1', '28-09-2024', 'stadium A', 'https://www.youtube.com/embed/Kj2RMOGbdQ0?si=KhB-O84ZEEWNy_iy&amp;start=14932', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Hai_phong_logo.png', 'Hải Phòng', 'image/Phu_tho_logo.png', 'Phú Thọ', '1-2', '28-09-2024', 'stadium A', 'https://www.youtube.com/embed/nZtBxvotUrM?si=03dQO0ksyLYamjoy&amp;start=2109', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Nam_can_tho_logo.png', 'ĐH Nam Cần Thơ', 'image/UTH-logo.png', 'ĐH Giao Thông Vận Tải TP.HCM', '0-3', '29-09-2024', 'stadium A', 'https://www.youtube.com/embed/tft1KXjKcgw?si=A0aG33tKM3Yj_Eu3&amp;start=1072', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Logo_ute-removebg-preview.png', 'ĐH Sư Phạm Kỹ Thuật TP.HCM', 'image/ĐH_Can_tho_logo.png', 'ĐH Cần Thơ', '3-2', '29-09-2024', 'stadium A', 'https://www.youtube.com/embed/tft1KXjKcgw?si=LkCbyy9fpqwkb0mm&amp;start=8718', 'Exciting match between Team A1 and Team B1' , 'Great game! Team A1 performed excellently.'),
    ('image/Dong_thap_logo.png', 'Đồng Tháp', 'image/Phu_tho_logo.png', 'Phú Thọ', '0-3', '29-09-2024', 'stadium A', 'https://www.youtube.com/embed/tft1KXjKcgw?si=P51Ov5bj00SYpzvs&amp;start=20783', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),  
    ('image/Binh_duong_logo.png', 'Bình Dương', 'image/Hai_phong_logo.png', 'Hải Phòng', '3-0', '29-09-2024', 'stadium A', 'https://www.youtube.com/embed/tft1KXjKcgw?si=hy7prc3-vfboNjSv&amp;start=2944', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Hutech_logo.png', 'ĐH Công nghệ TP.HCM', 'image/UTH-logo.png', 'ĐH Giao Thông Vận Tải TP.HCM', '3-0', '07-10-2024', 'stadium A', 'https://www.youtube.com/embed/SxqIqYASSc4?si=WJwS9bGzaxWx9ntJ&amp;start=1620', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', 'image/Logo_ute-removebg-preview.png', 'ĐH Sư Phạm Kỹ Thuật TP.HCM', '3-1', '07-10-2024', 'stadium A', 'https://www.youtube.com/embed/SxqIqYASSc4?si=3l1rOIC6GWqWLRXa&amp;start=8659', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/UTH-logo.png', 'ĐH Giao Thông Vận Tải TP.HCM', 'image/Logo_ute-removebg-preview.png', 'ĐH Sư Phạm Kỹ Thuật TP.HCM', '2-3', '07-10-2024', 'stadium A', 'https://www.youtube.com/embed/SxqIqYASSc4?si=B-oGvUsuOCg9N-FP&amp;start=18615', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Can_tho_logo.png', 'Cần Thơ', 'image/Phu_tho_logo.png', 'Phú Thọ', '3-0', '08-10-2024', 'stadium A', 'https://www.youtube.com/embed/AOSGeIuMy8g?si=4dRxuQDiXa2ng0FE&amp;start=1705', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Dat_lak_logo.png', 'Đắk Lắk', 'image/Binh_duong_logo.png', 'Bình Dương', '2-3', '08-10-2024', 'stadium A', 'https://www.youtube.com/embed/AOSGeIuMy8g?si=TFehxcgKrTEY7mDb&amp;start=7786', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Phu_tho_logo.png', 'Phú Thọ', 'image/Dat_lak_logo.png', 'Đắk Lắk', '0-3', '08-10-2024', 'stadium A', 'https://www.youtube.com/embed/AOSGeIuMy8g?si=vYaxqkVgTKHh6l47&amp;start=18149', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Hutech_logo.png', 'ĐH Công nghệ TP.HCM', 'image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', '3-0', '09-10-2024', 'stadium A', 'https://www.youtube.com/embed/IvUBoKldvwA?si=eFgVvER3DQ4n_qV4&amp;start=1882', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Can_tho_logo.png', 'Cần Thơ', 'image/Binh_duong_logo.png', 'Bình Dương', '3-2', '09-10-2024', 'stadium A', 'https://www.youtube.com/embed/IvUBoKldvwA?si=B3WW5NwFpBaiUOQK&amp;start=9051', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', 'image/Logo_ute-removebg-preview.png', 'ĐH Sư Phạm Kỹ Thuật TP.HCM', '3-0', '10-10-2024', 'stadium A', 'https://www.youtube.com/embed/rXp2tjF9QNI?si=-z4Inm2yEItoTuQA&amp;start=621', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Binh_duong_logo.png', 'Bình Dương', 'image/Dat_lak_logo.png', 'Đắk Lắk', '2-3', '10-10-2024', 'stadium A', 'https://www.youtube.com/embed/rXp2tjF9QNI?si=QfSvqa7LHjzZHBKs&amp;start=8382', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Hutech_logo.png', 'ĐH Công nghệ TP.HCM', 'image/Dat_lak_logo.png', 'Đắk Lắk', '1-3', '11-10-2024', 'stadium A', 'https://www.youtube.com/embed/dHIWS2b7jO4?si=9ADt09nl9ohFmSip&amp;start=2367', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Can_tho_logo.png', 'Cần Thơ', 'image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', '1-3', '11-10-2024', 'stadium A', 'https://www.youtube.com/embed/dHIWS2b7jO4?si=uhAEGwcqp3H4S1bc&amp;start=11912', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Hutech_logo.png', 'ĐH Công nghệ TP.HCM', 'image/Can_tho_logo.png', 'Cần Thơ', '3-2', '12-10-2024', 'stadium A', 'https://www.youtube.com/embed/OsjOwuJ-XXw?si=sCUSsWOcbJ6E-FhQ&amp;start=2045', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Dat_lak_logo.png', 'Đắk Lắk', 'image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', '1-3', '12-10-2024', 'stadium A', 'https://www.youtube.com/embed/OsjOwuJ-XXw?si=xru9ELpbyt5W7nXq&amp;start=13185', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Hutech_logo.png', 'ĐH Công nghệ TP.HCM', 'image/Dat_lak_logo.png', 'Đắk Lắk', '0-3', '19-10-2024', 'stadium A', 'https://www.youtube.com/embed/PJJf8IeWcSc?si=y-8C8k1tvPNjzUQz&amp;start=1759', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.'),
    ('image/Fpt_logo.png', 'CĐ FPT POLYTECHNIC TP.HCM', 'image/Dat_lak_logo.png', 'Đắk Lắk', '3-4', '19-10-2024', 'stadium A', 'https://www.youtube.com/embed/PJJf8IeWcSc?si=hyGJo6gLrbpgXPMV&amp;start=16520', 'Exciting match between Team A1 and Team B1', 'Great game! Team A1 performed excellently.')                                                               
''')


# Lưu các thay đổi vào cơ sở dữ liệu
conn.commit()

# Kiểm tra dữ liệu đã thêm
cursor.execute('SELECT * FROM matches')
matches = cursor.fetchall()
for match in matches:
    print(match)

# Đóng kết nối
conn.close()
