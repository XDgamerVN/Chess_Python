from interface import main_menu
import os
import sys
import pygame

pygame.init()

# Hàm để lấy đường dẫn tài nguyên khi đóng gói bằng PyInstaller
def resource_path(relative_path):
    """ Lấy đường dẫn tới file tài nguyên khi chạy từ file .exe """
    try:
        base_path = sys._MEIPASS  # PyInstaller trích xuất tài nguyên tạm thời
    except AttributeError:
        base_path = os.path.abspath(".")  # Khi chạy trực tiếp từ mã nguồn

    return os.path.join(base_path, relative_path)

# Lấy đường dẫn tới file icon
icon = pygame.image.load(resource_path(os.path.join('images', 'logo.png')))

# Thiết lập icon cho cửa sổ
pygame.display.set_icon(icon)

# Thiết lập tiêu đề cửa sổ
pygame.display.set_caption('Chess_Python by Nguyen Le Van Dung')

if __name__ == '__main__':
    main_menu()
