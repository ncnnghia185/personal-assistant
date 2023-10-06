import os
import random
import ctypes

def change_wallpaper():
    path = "D:\\wallpp"  # Đường dẫn tới thư mục chứa hình nền
    wallpapers = os.listdir(path)
    wallpaper = random.choice(wallpapers)

    # Tạo đường dẫn đầy đủ tới hình nền
    wallpaper_path = os.path.join(path, wallpaper)

    # Sử dụng hàm SystemParametersInfo để đặt hình nền
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 3)

    return "Wallpaper Changed"



