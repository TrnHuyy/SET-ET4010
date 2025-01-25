import cantools
from datetime import datetime

# Tải tệp DBC
dbc_file = 'dbc/FORD_CADS.dbc' 
db = cantools.database.load_file(dbc_file)

# Dữ liệu CAN mẫu
raw_message = "d7 a7 7f 8c 11 2f 00 10"

# Tách dữ liệu
raw_message = raw_message.strip("()")  # Loại bỏ dấu ngoặc tròn ở hai đầu
parts = raw_message.split()  # Tách chuỗi dựa trên khoảng trắng

timestamp = parts[0]  # Lấy phần timestamp
raw_id_data = parts[2] 

# Chuyển đổi timestamp
timestamp = float(timestamp)  # Chuyển sang số thực

# Xử lý CAN ID và dữ liệu
can_id, data = raw_id_data.split("#")  # Tách CAN ID và dữ liệu
can_id = int(can_id, 16)  # Chuyển CAN ID từ hex sang số nguyên
data_bytes = bytes.fromhex(data)  # Chuyển dữ liệu hex sang byte

# Giải mã thông điệp
decoded_message = db.decode_message(can_id, data_bytes)

# Hiển thị kết quả
readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
print(f"Timestamp: {readable_time}")
print(f"Decoded Message: {decoded_message}")
