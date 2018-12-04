# ex2tron's blog:
# http://ex2tron.wang
# 任务描述：
# 将dir1下面的所有txt重命名到dir2
# 重命名规则：1.txt~50.txt更改为200.txt~249.txt，不要删除原有的文件


import os
import shutil

path1 = 'dir1/'
path2 = 'dir2/'

if not os.path.exists(path2):
    os.mkdir(path2)

for file in os.listdir(path1):
    old_dir = os.path.join(path1, file)
    filename, filetype = os.path.splitext(file)

    new_dir = os.path.join(path2, str(int(filename)+199)+filetype)
    # os.rename(old_dir, new_dir)
    # shutil.move(old_dir, new_dir)
    # 上面两种方式都会移动删除掉源文件
    shutil.copy(old_dir, new_dir)
