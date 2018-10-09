# ex2tron's blog:
# http://ex2tron.wang


# 任务描述：
# 批量在某一文件夹下所有文本类文件的开头加一句话


import os

# 文件夹路径：
folder_path = "/home/chen/Documents/ex2tron-wang/LeetCode-Python3/"
# 要在开头添加的文本：
append_str = "# ex2tron's blog:\n# http://ex2tron.wang"
# 要修改特定文件的后缀名：
postfix = '.py'

for file in os.listdir(folder_path):
    if os.path.splitext(file)[1] == postfix:
        with open(os.path.join(folder_path, file), 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(append_str+"\n\n"+content)

print('已修改所有的%s文件' % postfix)
