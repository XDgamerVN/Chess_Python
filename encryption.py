import base64
import os

def encode_images():
    # Thư mục chứa ảnh
    image_folder = 'images'  # Thay đổi thành thư mục của bạn

    # Tạo file images.py
    try:
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
    except Exception as e:
        print(f"Xảy ra lỗi: {e}")

def encode_sounds():
    # Thư mục chứa âm thanh
    sound_folder = 'sounds'  # Thay đổi thành thư mục của bạn

    # Tạo file sounds.py
    try:
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
    except Exception as e:
        print(f"Xảy ra lỗi: {e}")

def encode_video():
    # Thư mục chứa video
    video_folder = 'videos'  # Thay đổi không thư mục của làm bộ

    # Tạo file video.py
    try:
        with open('videos.py', 'w') as python_file:
            python_file.write("videos = {\n")

            # Vòng lặp chọn video
            for video_file in os.listdir(video_folder):
                if video_file.endswith('.mp4'):  # Chọn định dạng video
                    video_name = video_file.split('.')[0]  # Lấy tên video (không có phần mở rộng)

                    with open(os.path.join(video_folder, video_file), 'rb') as vid:
                        encoded_string = base64.b64encode(vid.read()).decode('utf-8')
                        python_file.write(f'    "{video_name}": "{encoded_string}",\n')

            python_file.write("}\n")

        print("Mã video hoàn tất và được lưu vào videos.py!")
    except Exception as e:
        print(f"Xảy ra lỗi: {e}")

def encode():
    encode_images()
    encode_sounds()
    encode_video()

if __name__ == '__main__':
    encode()