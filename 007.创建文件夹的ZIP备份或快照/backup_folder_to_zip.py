# http://codec.wang
# 功能描述：
# 将整个文件夹备份成一个zip文件，zip文件名每次都随时间变换，如backup 2018-10-15.zip/backup 2018-10-16.zip
# 文件夹路径从剪贴板中获取


import os
import zipfile
import pyperclip
from datetime import datetime


def backup(origin_path):
    # 上一层路径和文件夹的名称
    parent_path, folder = os.path.dirname(
        origin_path), os.path.basename(origin_path)
    os.chdir(parent_path)

    # 备份路径：默认在所要备份路径的上一层级，以当前日期为结尾
    backup_path = os.path.join(parent_path, folder+" " +
                               datetime.now().strftime('%Y-%m-%d')+".zip")

    with zipfile.ZipFile(backup_path, 'w') as backup:
        for foldername, subfolders, filenames in os.walk(folder):
            print("Adding files in %s" % foldername)
            backup.write(foldername)
            for filename in filenames:
                backup.write(os.path.join(foldername, filename))


# 要备份的文件夹路径
origin_path = os.path.abspath(pyperclip.paste())
backup(origin_path)
