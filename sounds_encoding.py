import base64
import os

# Thư mục chứa âm thanh
sound_folder = 'sounds'  # Thay đổi thành thư mục của bạn

# Tạo file sounds.py
with open('sounds.py', 'w') as python_file:
    python_file.write("sounds = {\n")

    # Vòng lặp để mã hóa từng âm thanh
    for sound_file in os.listdir(sound_folder):
        if sound_file.endswith(('.wav', '.ogg', '.mp3')):  # Chọn định dạng âm thanh
            sound_name = sound_file.split('.')[0]  # Lấy tên âm thanh (không có phần mở rộng)

            with open(os.path.join(sound_folder, sound_file), 'rb') as snd:
                encoded_string = base64.b64encode(snd.read()).decode('utf-8')
                python_file.write(f'    "{sound_name}": "{encoded_string}",\n')

    python_file.write("}\n")

print("Mã hóa âm thanh hoàn tất và đã lưu vào sounds.py!")
