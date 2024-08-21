from cx_Freeze import setup, Executable

# Định nghĩa các file và thư mục cần đóng gói
build_exe_options = {
    "packages": ["pygame"],  # Bao gồm thư viện Pygame
    "include_files": ["images/"]  # Bao gồm thư mục hình ảnh
}

# Tạo executable từ file Main.py
executables = [
    Executable("Main.py", base="Win32GUI")  # base="Win32GUI" để ẩn cửa sổ console
]

# Thiết lập
setup(
    name="Chess Python",
    version="0.0.1",
    description="My Chess Python Game",
    options={"build_exe": build_exe_options},
    executables=executables,
)
