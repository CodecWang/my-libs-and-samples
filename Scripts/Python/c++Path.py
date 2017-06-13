# 获取剪贴板的路径内容，将其转换成C++风格路径，并复制到剪贴板
# ex2tron 2017年5月31日
# http://ex2tron.lofter.com


import pyperclip

# 原路径
originalPath = pyperclip.paste()
# print(originalPath)

# c格式路径
cFormat = originalPath.replace('\\', '//')
# print(cFormat)

pyperclip.copy(cFormat)
