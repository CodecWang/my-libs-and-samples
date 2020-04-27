# http://codec.wang
# 功能描述：
# 打印出当前用户的常用目录，如图片、视频、音乐、文档、桌面、下载等


import winreg


def get_user_path():
    # 用户文件夹的地址可以在下面这个注册表中查找
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         "Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
    print('桌面', winreg.QueryValueEx(key, 'Desktop')[0])
    print('文档', winreg.QueryValueEx(key, 'Personal')[0])
    print('音乐', winreg.QueryValueEx(key, 'My Music')[0])
    print('图片', winreg.QueryValueEx(key, 'My Pictures')[0])
    print('视频', winreg.QueryValueEx(key, 'My Video')[0])
    print('下载', winreg.QueryValueEx(
        key, '{374DE290-123F-4565-9164-39C4925E467B}')[0])


get_user_path()
