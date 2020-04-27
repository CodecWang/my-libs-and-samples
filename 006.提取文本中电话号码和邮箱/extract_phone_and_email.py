# http://codec.wang
# 功能描述：
# 搜索出文本中所有的电话号码和邮箱地址


import re
import pyperclip

# 中国手机号码正则匹配
phone_regex = re.compile(r'((\d{3})(\s|-|\.)?(\d{4})(\s|-|\.)?(\d{4}))')
# 邮箱地址正则匹配
email_regex = re.compile(
    r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')

text = pyperclip.paste()
print('匹配到的所有电话号码为：')
for group in phone_regex.findall(text):
    print(group[0])

print('匹配到的所有邮箱地址为：')
for group in email_regex.findall(text):
    print(group[0])

# 测试文本
# 我叫ex2tron，电话号码是188-8888-6666，邮箱是：ex2tron@outlook.com，另一个邮箱是：ex2tron@foxmail.com
