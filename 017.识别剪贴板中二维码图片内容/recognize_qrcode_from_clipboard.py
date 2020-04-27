# http://codec.wang
# 功能描述：识别剪贴板中的二维码图片内容
# 2020.04.27

from PIL import ImageGrab
from pyzbar.pyzbar import decode
import pyperclip

# 1. 从剪贴板中获取图片
img = ImageGrab.grabclipboard()
if img:
    try:
        # 2. 解码
        qrcode = str(decode(img)[0].data)
        # 3. 复制到剪贴板
        # pyperclip.copy(str(qrcode))
        print(qrcode)
        # 4. 显示图片
        # img.show()
    except:
        print('No QRCode Found.')
else:
    print('No Image Here.')
