# Overview
Đây là project Đồ Án 2 với nội dung tìm hiểu và mô phỏng/triển khai mạng CAN.

Những nội dung chi tiết vui lòng đọc file báo cáo: Đồ_án_2.pdf

# Những thay đổi trong source code
Để sử dụng phần mềm đọc gói tin CANToolz và phần mềm giải mã CAN_decoder, nhóm đã lấy các code về dưới dạng thư viện sau đó thay đổi chúng.

Để thuận tiện cho việc đọc và sử dụng, các thay đổi được copy lại trong 2 folder CANToolz và CAN_decoder của chúng tôi. Tuy nhiên, các thay đổi thực tế mà bạn cần đổi nằm trong môi trường ảo venv của project.

# Hướng dẫn cài đặt

## Chuẩn bị môi trường
Clone repo này về máy.

Xóa folder CAN-venv của chúng tôi.

Tạo môi trường ảo trong python (Window)
<pre>
python -m venv CAN-venv
CAN-venv\Scripts\activate
</pre>

Tạo và kích hoạt môi trường ảo trong python (Linux/macOS)
<pre>
python -m venv CAN-venv
source CAN-venv/bin/activate
</pre>

Cài các thư viện cần thiết
<pre>
pip install -r requirements.txt
</pre>

## Chạy CANToolz
Để chạy CANToolz, vào thư mục CAN-venv và tìm folder CANToolz chứa source code của thư viện CANToolz, sau đó thay thế folder CANToolz/cantoolz bằng folder tương ứng của nhóm ở repo

Kết nối máy tính với hệ thống CAN, sau đó chạy lệnh
<pre>
cantoolz -g w -c examples/can_sniff.py
</pre>

Nếu không có kết nối và chỉ muốn xem UI để sửa đổi, chạy lệnh
<pre>
cantoolz
</pre>

Để tìm các option của CANToolz, gõ lệnh
<pre>
cantoolz -h
</pre>

## Chạy CAN_decoder
Để chạy thử ví dụ của CAN_decoder, vào folder can_decoder/examples. Sau đó tiến hành chạy file decode
<pre>
python decode_dataframe.py
</pre>

File này sẽ dùng file log và dbc mẫu của CSS để giải mã, sau đó hiển thị ra đồ thị dưới dạng .png

**Lưu ý**: Các câu lệnh phải chạy khi kích hoạt CAN-venv

# Tài liệu tham khảo
Tham khảo mã nguồn của dự án tại [CANToolz](https://github.com/CANToolz/CANToolz) và [CAN_decoder](https://github.com/CSS-Electronics/can_decoder)
