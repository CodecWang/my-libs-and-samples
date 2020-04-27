#!/bin/bash

# http://codec.wang 
# 功能描述：批量创建1000个.txt文件

for i in {000..999}; do
	echo "$i" > "$i".txt
	# 空文件：touch "$i".txt
done
