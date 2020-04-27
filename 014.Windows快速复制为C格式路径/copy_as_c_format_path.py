# http://codec.wang
# 功能描述：Windows下的默认路径是反斜杠，比如：D:\Surface\Documents\01.Build\MyLibsAndSamples
# C或者一些语言中这个路径显然是不对的，可以先拷贝这个路径，然后执行脚本，快速转换成双反斜杠或斜杠
# 2019年1月6日 21点23分

import pyperclip

# 双反斜杠
cFormat = pyperclip.paste().replace('\\', '\\\\')

pyperclip.copy(cFormat)
