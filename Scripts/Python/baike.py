# 获取剪贴板或命令行第一个参数作为关键字，打开该关键字的百度百科介绍
# ex2tron 2017年5月31日
# http://ex2tron.lofter.com

import pyperclip
import sys
import webbrowser


keyword = len(sys.argv) < 2 and pyperclip.paste() or sys.argv[1]
url = "http://baike.baidu.com/search/word?word=%s" % (keyword)

webbrowser.open(url)
