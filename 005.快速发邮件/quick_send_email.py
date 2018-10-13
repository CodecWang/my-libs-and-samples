# ex2tron's blog:
# http://ex2tron.wang
# 任务描述：
# 根据剪贴板或命令行参数的邮件地址快速打开邮件应用


import sys
import pyperclip
import webbrowser

email = len(sys.argv) < 2 and pyperclip.paste() or sys.argv[1]
webbrowser.open("mailto:%s" % email)
