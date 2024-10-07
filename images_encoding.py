import base64
import os

# Thư mục chứa ảnh
image_folder = 'images'  # Thay đổi thành thư mục của bạn

# Tạo file images.py
with open('images.py', 'w') as python_file:
    python_file.write("images = {\n")

    # Vòng lặp để mã hóa từng ảnh
    for image_file in os.listdir(image_folder):
        if image_file.endswith(('.png', '.jpg', '.jpeg')):  # Chọn định dạng ảnh
            piece_name = image_file.split('.')[0]  # Lấy tên quân cờ (không có phần mở rộng)

            with open(os.path.join(image_folder, image_file), 'rb') as img:
                encoded_string = base64.b64encode(img.read()).decode('utf-8')
                python_file.write(f'    "{piece_name}": "{encoded_string}",\n')

    python_file.write("}\n")

print("Mã hóa ảnh hoàn tất và đã lưu vào images.py!")
