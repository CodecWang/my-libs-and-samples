import webbrowser
import pyperclip
import sys

email = len(sys.argv) < 2 and pyperclip.paste() or sys.argv[1]
url = "mailto:%s" % (email)
webbrowser.open(url)
