#!/bin/bash

# ex2tron's blog:
# http://ex2tron.wang 
# 任务描述：批量创建1000个.txt文件

for i in {000..999}; do
	echo "$i" > "$i".txt
	# 空文件：touch "$i".txt
done
