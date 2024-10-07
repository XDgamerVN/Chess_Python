from images import images
from sounds import sounds
import base64
import io
import pygame

def decode_and_load_image(piece, size):
    """Giải mã và tải ảnh của quân cờ, điều chỉnh kích thước"""
    if isinstance(images[piece], str):  # Nếu ảnh là chuỗi base64
        image_data = base64.b64decode(images[piece])
        image_file = io.BytesIO(image_data)
        image = pygame.image.load(image_file)
    else:
        image = images[piece]

    # Thay đổi kích thước ảnh theo kích thước mong muốn (size)
    return pygame.transform.smoothscale(image, size)

# Giải mã âm thanh và phát âm
def play_sound(sound_name):
    """Hàm phát âm thanh từ dữ liệu đã mã hóa"""
    pygame.mixer.init()

    # Giải mã âm thanh
    sound_data = base64.b64decode(sounds[sound_name])
    sound_file = io.BytesIO(sound_data)  # Tạo stream từ dữ liệu đã giải mã
    sound = pygame.mixer.Sound(sound_file)  # Tải âm thanh từ stream
    sound.play()