# Dự án Chess Game bằng Python

## 1. Giới thiệu

Dự án này là một trò chơi cờ vua (Chess) được phát triển bằng Python, với giao diện đồ họa và các tính năng cơ bản của một ván cờ vua tiêu chuẩn. Dự án có cấu trúc thư mục rõ ràng và dễ quản lý, hỗ trợ việc phát triển và mở rộng tính năng trong tương lai.

## 2. Cấu trúc dự án

Dưới đây là mô tả ngắn gọn về các thư mục và file trong dự án:

- `__pycache__/`: Thư mục tự động được tạo bởi Python để lưu trữ các file bytecode.
- `.idea/`: Thư mục cấu hình của IDE (Integrated Development Environment), thường là PyCharm hoặc IntelliJ IDEA.
- `.ipynb_checkpoints/`: Thư mục chứa các checkpoint của file notebook (.ipynb) trong Jupyter.
- `assets/`: Thư mục chứa các tài nguyên cần thiết cho trò chơi như hình ảnh, âm thanh, hoặc các file hỗ trợ khác.
- `data_test/`: Thư mục dùng để lưu trữ dữ liệu thử nghiệm, có thể bao gồm các file test hoặc mẫu dữ liệu cho việc phát triển và kiểm thử.
- `pieces/`: Thư mục chứa các hình ảnh của quân cờ trong trò chơi.

### Các file Python

- `additions.py`: Chứa các chức năng phụ trợ bổ sung cho trò chơi, có thể bao gồm các tiện ích hoặc các hàm hỗ trợ.
- `alpha.py`: File này có thể chứa các thử nghiệm hoặc các tính năng đang trong giai đoạn phát triển ban đầu (alpha) của trò chơi.
- `board.py`: Quản lý logic của bàn cờ, bao gồm việc hiển thị và cập nhật trạng thái của bàn cờ khi các quân cờ di chuyển.
- `constants.py`: Chứa các hằng số được sử dụng trong toàn bộ dự án, như kích thước bàn cờ, màu sắc, hoặc đường dẫn đến các tài nguyên.

### Các file cấu hình

- `.gitattributes`: File cấu hình cho Git, dùng để quản lý các thuộc tính của repository, như cách xử lý các loại file khác nhau khi commit.
- `.gitignore`: File cấu hình cho Git, dùng để xác định các file hoặc thư mục không nên được theo dõi bởi Git, chẳng hạn như các file tạm thời hoặc các file nhị phân.

## 3. Hướng dẫn cài đặt và sử dụng

### Yêu cầu hệ thống

- Python 3.x

### Cài đặt

1. Clone repository về máy tính của bạn:
   ```bash
   git clone <repository-url>
