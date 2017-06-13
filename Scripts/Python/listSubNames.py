# 列出剪贴板路径下的所有文件名和文件夹名
# 命令行参数：后缀名，如.exe，只会列出.exe的所有文件
# ex2tron 2017年5月31日
# http://ex2tron.lofter.com

import os
import sys
import pyperclip


# 获取命令行参数中的第一个参数：后缀名
postfix = ''
if len(sys.argv) == 2:
    postfix = sys.argv[1]


def file_name(f):
    '''获得文件夹下所有子文件（夹）的名称'''
    L = []
    for files in os.listdir(f):
        if postfix:
            if os.path.splitext(files)[1] == postfix:
                L.append(files)
        else:
            L.append(files)
    return L


# 获取剪贴板内容
lst = file_name(pyperclip.paste())
for file in lst:
    print(file)
