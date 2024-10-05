import pygame.mixer
from interface import *
from constants import *
import qrcode
import io
from PIL import Image

def quit_game(SQ_SIZE):
    """Kiểm tra xem người chơi có muốn thoát game hay không"""
    in_quit = True
    while in_quit:
        # Vẽ nút và các thông báo thoát game
        draw_button("", 0,SQ_SIZE * 4, SQ_SIZE * 3,
                    SQ_SIZE * 6, SQ_SIZE * 2, SQ_SIZE // 7, SQ_SIZE // 15,
                    'white', 'black', COLOR_SCREEN, COLOR_SCREEN, 'aquamarine')

        draw_button('Are you sure you want to quit the game?', SQ_SIZE // 3, SQ_SIZE * 7 - SQ_SIZE // 4,
                    SQ_SIZE * 3 + SQ_SIZE // 2, SQ_SIZE // 2, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                    'white', 'white', COLOR_SCREEN, COLOR_SCREEN, COLOR_SCREEN)

        yes_button = draw_button("Yes", SQ_SIZE // 3, SQ_SIZE * 5 + SQ_SIZE // 8, SQ_SIZE * 4 + SQ_SIZE // 4,
                                 SQ_SIZE * 2 - SQ_SIZE // 4, SQ_SIZE // 2, SQ_SIZE // 7, SQ_SIZE // 22,
                                 'white', 'black', COLOR_SCREEN, 'tomato', 'tomato')

        no_button = draw_button("No", SQ_SIZE // 3, SQ_SIZE * 7 + SQ_SIZE // 8, SQ_SIZE * 4 + SQ_SIZE // 4,
                                SQ_SIZE * 2 - SQ_SIZE // 4, SQ_SIZE // 2, SQ_SIZE // 7, SQ_SIZE // 22,
                                'white', 'black', COLOR_SCREEN, 'light green', 'light green')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if no_button.collidepoint(event.pos):
                    return
                elif yes_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()

        clock.tick(60)
        pygame.display.flip()

def draw_button(text, text_size,  x, y, width, height, border_radius, border_width,
                not_text_hover_color, text_hover_color, not_hover_color, hover_color, border_color):
    """Vẽ nút bo góc với màu sắc, viền và vị trí đã chỉ định"""
    font_button = pygame.font.SysFont('Arial', text_size, True)
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)
    if button_rect.collidepoint(mouse_pos):
        button_color = hover_color
        text_color = text_hover_color
    else:
        button_color = not_hover_color
        text_color = not_text_hover_color
    draw_rounded_rect(screen, button_rect, border_radius, border_color, border_width)
    rounded_rect(screen, button_rect, border_radius, button_color)
    text_surface = font_button.render(text, True, text_color)
    screen.blit(text_surface, text_surface.get_rect(center=button_rect.center))
    return button_rect

def rounded_rect(surface, rect, radius, color):
    """Vẽ hình chữ nhật bo góc"""
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def draw_rounded_rect(surface, rect, radius, color, border_width):
    """Vẽ hình chữ nhật bo góc với viền"""
    border_rect = rect.inflate(border_width, border_width)
    pygame.draw.rect(surface, color, border_rect, border_radius=radius)

def play_sound(sound_file):
    """Hàm phát âm thanh từ file"""
    pygame.mixer.init()
    sound = pygame.mixer.Sound(f"sounds/{sound_file}")   # Trỏ đến thư mục sounds
    sound.play()

def qr_code(data, SQ_SIZE):
    """Hàm tạo mã QR từ dữ liệu đầu vào"""
    # Tạo mã QR bằng qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size= SQ_SIZE // 12,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Tạo ảnh mã QR bằng PIL và chuyển sang RGBA
    img = qr.make_image(fill='black', back_color='white').convert('RGBA')

    # Chuyển đổi ảnh QR từ PIL sang đối tượng Pygame Surface
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    qr_image = Image.open(img_bytes)

    # Chuyển đổi từ PIL sang Pygame
    size = qr_image.size
    data = qr_image.tobytes()

    qr_surface = pygame.image.fromstring(data, size, 'RGBA')
    return qr_surface  # Trả về đối tượng Surface để vẽ lên màn hình

def code_version(SQ_SIZE):
    """🤑🤑🤑"""
    in_version = True
    input_text = ""
    cursor_pos = 0
    cursor_visible = True
    cursor_blink_time = 500
    last_blink_time = pygame.time.get_ticks()
    typing_active = False
    typing_timeout = 1000
    backspace_held = False
    backspace_hold_time = 150
    last_backspace_time = pygame.time.get_ticks()

    show_message = False
    message_text = ""
    message_start_time = 0
    message_duration = 5000

    while in_version:
        current_time = pygame.time.get_ticks()

        # Nếu không nhập ký tự trong thời gian typing_timeout, con trỏ nhấp nháy trở lại
        if not typing_active:
            if current_time - last_blink_time >= cursor_blink_time:
                cursor_visible = not cursor_visible  # Đảo trạng thái hiển thị của con trỏ
                last_blink_time = current_time  # Cập nhật thời điểm thay đổi trạng thái
        else:
            cursor_visible = True  # Khi đang nhập, con trỏ luôn hiện

        # Kiểm tra nếu giữ phím BACKSPACE
        if backspace_held and current_time - last_backspace_time >= backspace_hold_time:
            if cursor_pos > 0:
                input_text = input_text[:cursor_pos - 1] + input_text[cursor_pos:]  # Xóa ký tự trước con trỏ
                cursor_pos -= 1  # Di chuyển con trỏ về phía trước
            last_backspace_time = current_time  # Cập nhật thời gian backspace cuối cùng

        # Vẽ nút và các thông báo thoát game
        draw_button("", 0, SQ_SIZE * 4, SQ_SIZE * 2,
                    SQ_SIZE * 6, SQ_SIZE * 3, SQ_SIZE // 5, SQ_SIZE // 10,
                    'white', 'black', COLOR_SCREEN, COLOR_SCREEN, 'aquamarine')

        text_button = draw_button("", 0, SQ_SIZE * 5, SQ_SIZE * 2 + SQ_SIZE // 2,
                                  SQ_SIZE * 4, SQ_SIZE, SQ_SIZE // 5, SQ_SIZE // 10,
                                  'white', 'black', 'white', 'white', 'aquamarine')

        send_button = draw_button("Send", SQ_SIZE // 3, SQ_SIZE * 5 - SQ_SIZE // 4, SQ_SIZE * 4 + SQ_SIZE // 4,
                                  SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 5, SQ_SIZE // 15,
                                  'white', 'black', COLOR_SCREEN, 'aquamarine', 'aquamarine')

        quit_button = draw_button("Quit", SQ_SIZE // 3, SQ_SIZE * 7 + SQ_SIZE // 4, SQ_SIZE * 4 + SQ_SIZE // 4,
                                  SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 5, SQ_SIZE // 15,
                                  'white', 'black', COLOR_SCREEN, 'tomato', 'tomato')

        # Hiển thị văn bản nhập vào ở vị trí của text_button
        font = pygame.font.SysFont('Arial', SQ_SIZE // 3 + SQ_SIZE // 15, True)
        text_surface = font.render(input_text, True, 'black')
        text_rect = text_surface.get_rect(center=text_button.center)
        screen.blit(text_surface, text_rect.topleft)

        # Hiển thị con trỏ (dấu nháy) nếu đang ở trạng thái hiển thị
        if cursor_visible:
            cursor_x = text_rect.x + font.size(input_text[:cursor_pos])[0]  # Tính vị trí X của con trỏ
            cursor_y = text_rect.y
            pygame.draw.rect(screen, 'black', pygame.Rect(cursor_x, cursor_y, 2, text_rect.height))

        # Kiểm tra sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if send_button.collidepoint(event.pos):
                    # Kiểm tra văn bản nhập vào
                    if input_text == "WXVyaWtv":
                        message_text = "Pass"
                    else:
                        message_text = "Wrong code!"
                    show_message = True  # Bắt đầu hiển thị thông báo
                    message_start_time = current_time  # Lưu thời gian bắt đầu hiển thị
                    input_text = ""  # Xóa văn bản sau khi gửi
                    cursor_pos = 0  # Đặt lại vị trí con trỏ

                elif quit_button.collidepoint(event.pos):
                    in_version = False  # Thoát khởi vòng lặp

            elif event.type == pygame.KEYDOWN:  # Kiểm tra sự kiện bàn phím
                typing_active = True  # Đang nhập văn bản, con trỏ sẽ luôn hiển thị
                last_blink_time = current_time  # Đặt lại thời gian nhấp nháy để ngừng nhấp nháy

                if event.key == pygame.K_BACKSPACE:
                    if cursor_pos > 0:
                        input_text = input_text[:cursor_pos - 1] + input_text[cursor_pos:]  # Xóa ký tự trước con trỏ
                        cursor_pos -= 1  # Di chuyển con trỏ về phía trước
                    backspace_held = True  # Bắt đầu giữ phím BACKSPACE
                    last_backspace_time = pygame.time.get_ticks()  # Đặt lại thời gian bắt đầu giữ BACKSPACE
                elif event.key == pygame.K_RETURN:
                    if input_text == "WXVyaWtv":
                        message_text = "Pass"
                    else:
                        message_text = "Wrong code!"

                    show_message = True  # Bắt đầu hiển thị thông báo
                    message_start_time = current_time  # Lưu thời gian bắt đầu hiển thị
                    input_text = ""  # Xóa văn bản sau khi gửi
                    cursor_pos = 0  # Đặt lại vị trí con trỏ
                elif event.key == pygame.K_LEFT:  # Di chuyển con trỏ sang trái
                    if cursor_pos > 0:
                        cursor_pos -= 1
                elif event.key == pygame.K_RIGHT:  # Di chuyển con trỏ sang phải
                    if cursor_pos < len(input_text):
                        cursor_pos += 1
                else:
                    # Chỉ thêm ký tự nếu tổng độ dài không vượt quá 19
                    if len(input_text) < 19:
                        input_text = input_text[:cursor_pos] + event.unicode + input_text[cursor_pos:]
                        cursor_pos += 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    backspace_held = False  # Dừng giữ phím BACKSPACE

        # Kiểm tra xem người dùng đã ngừng nhập trong thời gian timeout hay chưa
        if typing_active and current_time - last_blink_time >= typing_timeout:
            typing_active = False  # Nếu hết thời gian nhập, trở về trạng thái nhấp nháy

        # Hiển thị thông báo nếu có và kiểm tra thời gian để ẩn
        if show_message and message_text != "":
            if current_time - message_start_time <= message_duration:
                # Vẽ thông báo lên màn hình
                draw_button(message_text, SQ_SIZE // 2, SQ_SIZE * 4, SQ_SIZE * 2,
                            SQ_SIZE * 6, SQ_SIZE * 3, SQ_SIZE // 5, SQ_SIZE // 10,
                            'white', 'white', COLOR_SCREEN, COLOR_SCREEN, 'aquamarine')
                if message_text == "Pass":
                    draw_button("DON'T SCAN ME!", SQ_SIZE // 3, SQ_SIZE * 7 - SQ_SIZE // 4, SQ_SIZE * 2,
                                SQ_SIZE * 3, SQ_SIZE * 3, SQ_SIZE // 5, 0,
                                'white', 'white', COLOR_SCREEN, COLOR_SCREEN, COLOR_SCREEN)
                    # Tạo mã QR
                    qr_surface = qr_code("https://s.pro.vn/ZQ36", SQ_SIZE)
                    qr_rect = qr_surface.get_rect(center=(SQ_SIZE * 6 - SQ_SIZE // 4, SQ_SIZE * 4 - SQ_SIZE // 2))
                    screen.blit(qr_surface, qr_rect.topleft)
            else:
                show_message = False  # Ẩn thông báo sau 5 giây

        pygame.display.flip()
