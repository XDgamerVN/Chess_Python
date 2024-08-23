# Dự án Chess Game bằng Python (chưa hoàn thiện)

## 1. Giới thiệu

Dự án này là một trò chơi cờ vua (Chess) được phát triển bằng Python, với giao diện đồ họa và các tính năng cơ bản của một ván cờ vua tiêu chuẩn.

## 2. Cấu trúc dự án

- `images/`: Thư mục chứa các tài nguyên hình ảnh quân cờ dạng PNG và ICO.

### Các file Python (chưa được tối ưu)

- `Main.py`: Chứa giao diện trò chơi
- `Game.py`: Chứa các chức năng chính của trò chơi.
- `Engine.py`: Chứa các thư viên trò chơi.
- `Constants.py`: Chứa các tỉ lệ hiển thị.
- `ChessAI.py`: máy chơi cờ (thử nghiệm sử dụng thuật Negamax với cắt tỉ alpha beta, đây là loại AI flash)

## 3. Hướng dẫn cài đặt và sử dụng

### Windows
`Chess_Python.exe`

### Linux 
Mở terminal
`./Chess_Python`

### Yêu cầu hệ thống đối với dev (Khuyên dùng với Pycharm)

- Python 3.1x
- pygame 2.6.0
