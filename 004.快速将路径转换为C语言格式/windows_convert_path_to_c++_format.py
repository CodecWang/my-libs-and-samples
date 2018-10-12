# ex2tron's blog:
# http://ex2tron.wang
# 任务描述：
# 适用于Windows系统，将剪贴板中的路径快速转换成C语言识别的格式（斜杠转换），并且复制到剪贴板


import pyperclip

# 获取剪贴板中的源路径
origin_path = pyperclip.paste()

c_format = origin_path.replace("\\", "//")
pyperclip.copy(c_format)
