# http://codec.wang
# 功能描述：
# 在当前目录下创建dir1并生成000.txt~999.txt 1000个文件
# 每个文件的内容是文件名本身

import os

# 创建文件夹
if not os.path.exists('dir1/'):
    os.mkdir('dir1/')

# 批量生成
for i in range(100):
    with open('dir1/%03d.txt' % i, 'w') as f:
        f.write('%03d' % i)
        # 内容为空的话，这里直接写pass
