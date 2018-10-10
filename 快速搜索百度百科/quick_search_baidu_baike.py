# ex2tron's blog:
# http://ex2tron.wang


# 任务描述：
# 根据参数或者剪贴板内容中的关键字，打开浏览器并快速搜索百度百科


import sys
import pyperclip
import webbrowser


# 命令参数为主，为空时获取剪贴板内容
keyword = len(sys.argv) < 2 and pyperclip.paste() or sys.argv[1]

url = "http://baike.baidu.com/search/word?word=%s" % keyword
webbrowser.open(url)
