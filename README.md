# **Dự án Cờ Vua bằng Python (Chưa Hoàn Thiện)**

## 1. Giới thiệu

Dự án này là một trò chơi cờ vua được phát triển bằng Python, với giao diện đồ họa và các tính năng cơ bản của một ván cờ vua tiêu chuẩn.

![Ảnh bìa dự án](images/gameplay.gif)  <!-- Thay thế bằng đường dẫn tới ảnh bìa dự án -->

## 2. Cấu trúc dự án

- **`images/`**: Thư mục chứa các tài nguyên hình ảnh quân cờ dạng PNG và ICO.
- **`sounds/`**: Thư mục chứa các tài nguyên âm thanh dạng MP3.

### Các file Python (Chưa được tối ưu)

- **`negamaxAI.py`**: Máy chơi cờ (thử nghiệm sử dụng thuật Negamax).
- **`constants.py`**: Chứa các hằng số.
- **`engine.py`**: Chứa các thư viện trò chơi.
- **`system.py`**: Chứa các chức năng chính của trò chơi.
- **`interface.py`**: Chứa giao diện trò chơi.
- **`additions.py`**: Bổ sung cho giao diện trò chơi.
- **`main.py`**: Phần khởi chạy file trò chơi.

## 3. Yêu cầu hệ thống đối với lập trình viên

**Khuyên dùng với PyCharm**

- **Python**: 3.1.x hoặc cao hơn
- **Pygame**: 2.6.x

## 4. Cách bắt đầu

1. Clone dự án về máy tính của bạn.
2. Cài đặt các thư viện cần thiết bằng lệnh:
   ```bash
   pip install pygame
