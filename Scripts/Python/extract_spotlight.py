import os
import winreg
import shutil


def get_desktop_path():
    '''
    获取当前系统的桌面文件夹路径
    '''
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         "Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
    return winreg.QueryValueEx(key, 'Desktop')[0]


pic_path = os.path.join(os.path.expanduser(
    '~'), "AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")

desktop_path = get_desktop_path()

desktop_pic_path = os.path.join(desktop_path, "Windows聚焦图片提取")

# 复制整个Windows聚焦图片文件夹到桌面
if os.path.exists(desktop_pic_path):
    shutil.rmtree(desktop_pic_path)
shutil.copytree(pic_path, desktop_pic_path)

# 添加后缀名
for file in os.listdir(desktop_pic_path):
    shutil.move(os.path.join(desktop_pic_path, file),
                os.path.join(desktop_pic_path, file + ".png"))

# 删除小于50kb的照片
for file in os.listdir(desktop_pic_path):
    file_path = os.path.join(desktop_pic_path, file)
    if(os.path.getsize(file_path) // 1000 <= 50):
        os.unlink(file_path)
