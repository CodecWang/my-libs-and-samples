# http://codec.wang
# 功能描述：
# 列出目录下特定的某一类文件或全部文件，第二个参数为类别，第三个参数指定是否包含目录中的子目录


import os
import sys
import pyperclip


def get_file_names(folder, postfix='*', is_contain_subfolders=False):
    ret = []
    # 包含子文件夹
    if is_contain_subfolders:
        for foldername, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                if postfix == '*':
                    ret.append(filename)
                elif os.path.splitext(filename)[1] == postfix:
                    ret.append(filename)
    else:
        for item in os.listdir(folder):
            # 如果是文件夹，则跳过
            if os.path.isdir(os.path.join(folder, item)):
                continue
            if postfix == '*':
                ret.append(item)
            elif os.path.splitext(item)[1] == postfix:
                ret.append(item)

    return ret


# 要操作的文件夹
folder_path = pyperclip.paste()
# 后缀名
postfix = sys.argv[1]
# 是否包含子目录
is_contain_subfolders = False if len(sys.argv) < 3 else bool(sys.argv[2])

result = get_file_names(folder_path, postfix=postfix,
                        is_contain_subfolders=is_contain_subfolders)
for item in result:
    print(item)
