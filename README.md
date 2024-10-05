# Dự Án Cờ Vua Bằng Python

## 1. Giới Thiệu

Dự án này là một trò chơi cờ vua được phát triển bằng Python, với giao diện đồ họa thân thiện và đầy đủ các tính năng cơ bản của một ván cờ vua tiêu chuẩn. Trò chơi cho phép người dùng chơi với AI hoặc với bạn bè, mang lại trải nghiệm thú vị và thử thách.

<div align="center">
    <img src="images/gameplay.gif" alt="Ảnh gif gameplay" width="300" height="300">
</div>

---

## 2. Cấu Trúc Dự Án

Dự án được tổ chức theo cấu trúc sau:

- **`images/`**: Thư mục chứa các tài nguyên hình ảnh quân cờ dưới định dạng PNG và ICO.
- **`sounds/`**: Thư mục chứa các tài nguyên âm thanh dưới định dạng MP3.

### Các File Python

Dưới đây là danh sách các file Python trong dự án cùng với mô tả chức năng của chúng:

- **`negamaxAI.py`**: Chương trình điều khiển AI (thử nghiệm với thuật toán Negamax).
- **`constants.py`**: Chứa các hằng số sử dụng trong trò chơi.
- **`engine.py`**: Cung cấp các thư viện và chức năng cơ bản của trò chơi.
- **`system.py`**: Chứa các chức năng chính và logic của trò chơi.
- **`interface.py`**: Định nghĩa giao diện người dùng cho trò chơi.
- **`additions.py`**: Các bổ sung và tiện ích cho giao diện người dùng.
- **`main.py`**: File khởi chạy chính của trò chơi.

---

## 3. Yêu Cầu Hệ Thống

Để phát triển và chạy trò chơi, bạn cần:

- **Khuyên dùng**: IDE PyCharm
- `Python`: 3.10.x hoặc cao hơn
- `Pygame`: 2.6.0
- `Pillow`: 10.8.0
- `qrcode`: 8.0

## 4. Hướng Dẫn Bắt Đầu

### 4.1. Clone Dự Án

Đầu tiên, bạn cần clone dự án về máy tính của mình:

```bash
git clone https://github.com/XDgamerVN/Chess_Python.git
cd Chess_Python
```

### 4.2. Tạo Môi Trường Ảo (Tuỳ Chọn)

Môi trường ảo giúp bạn quản lý các phụ thuộc cho dự án mà không làm ảnh hưởng đến các dự án khác:

```bash 
python -m venv venv
source venv/bin/activate  # Trên Linux
venv\Scripts\activate   # Trên Windows
```

### 4.3. Cài Đặt Thư Viện

#### Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip
sudo apt install libsdl2-mixer-2.0-0 libjpeg-dev zlib1g-dev
```

#### Fedora:

```bash
sudo dnf install python3 python3-pip
sudo dnf install SDL2_mixer-devel libjpeg-devel zlib-devel
```

#### Arch Linux/Manjaro:

```bash
sudo pacman -S python python-pip
sudo pacman -S sdl2_mixer libjpeg-turbo zlib
```

#### Windows:

- Tải Python từ trang chính thức: [python.org](https://www.python.org/)
- Chạy trình cài đặt và đảm bảo chọn tùy chọn "Add Python to PATH"
- Mở Command Prompt và kiểm tra phiên bản Python bằng lệnh:

```bash
python --version
```

Dự án yêu cầu một số thư viện Python bổ sung như `pygame`, `qrcode`, và `Pillow`. Bạn có thể cài đặt tất cả bằng lệnh:

```bash
pip install pygame qrcode[pil] pillow
```

### 4.4. Chạy Trò Chơi

Sau khi cài đặt xong, bạn có thể chạy trò chơi bằng lệnh sau:

```bash
python main.py
```

### 4.5. Thưởng Thức Trò Chơi

Khám phá và tận hưởng trò chơi! Bạn có thể thử chơi với AI hoặc cùng bạn bè để tìm kiếm chiến thắng.

#### Các lưu ý cho người dùng Linux:

- Nếu có bất kỳ vấn đề gì về âm thanh hoặc giao diện đồ họa, bạn có thể cần phải cài đặt các thư viện bổ sung của hệ thống như đã nêu trên.
- Nếu cần, bạn có thể cấp quyền thực thi cho tệp main.py bằng lệnh:

```bash
chmod +x main.py
```

Sau khi hoàn tất các bước trên, trò chơi sẽ khởi chạy bình thường trên Linux.

---

## 5. Tính Năng Nổi Bật

- Chế độ chơi đơn và nhiều người chơi: Cho phép người dùng thi đấu với AI hoặc bạn bè. 
- AI thông minh: Dựa trên thuật toán Negamax để đưa ra các nước đi hợp lý.
- Giao diện trực quan: Thiết kế giao diện thân thiện và dễ sử dụng.
- Âm thanh sống động: Âm thanh và hiệu ứng được thiết kế để tăng trải nghiệm chơi game.

---

## 6. Kế Hoạch Tương Lai

Tôi dự định cập nhật dự án với những tính năng mới, bao gồm:

- Cải thiện AI với các thuật toán phức tạp hơn.
- Thêm tính năng lưu trữ ván cờ để người dùng có thể quay lại sau.
- Cải tiến giao diện người dùng với các tùy chọn tùy chỉnh phong cách chơi.

---

## 7. Tài Liệu Tham Khảo

Xin cảm ơn LeMaster Tech và Eddie Sharick (Eddie) về kiến thức phát triển dự án này.
- [LeMaster Tech](https://www.youtube.com/@lemastertech)
- [Eddie Sharick (Eddie)](https://www.youtube.com/@eddiesharick6649)

---

## 8. Liên Hệ

Nếu bạn có bất kỳ câu hỏi hoặc phản hồi nào, hãy liên hệ với chúng tôi qua địa chỉ email: [dungnguyen2661@gmail.com]

---

**_Cảm ơn bạn đã quan tâm đến dự án của tôi. Chúc bạn có những giờ phút chơi game vui vẻ!_**
