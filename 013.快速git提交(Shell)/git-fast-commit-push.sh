#!/bin/bash

# http://codec.wang 
# 功能描述：输入备注，快速git提交

echo "输入你的提交信息：" 
read commit_info

if [ -n "$commit_info" ]; then
	git add .
	git commit -m "$commit_info"
	git push -u origin master
else
	echo "信息为空，未执行操作。"
fi
