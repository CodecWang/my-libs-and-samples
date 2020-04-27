#!/bin/bash

# http://codec.wang 
# 功能描述：快速导出固定数据库的数据，以日期结尾命名
# 也可以在-p后面直接写上密码，不过不安全，不推荐。
# 2019年1月8日 20:16

today=$(date +%Y%m%d)
db_name="your_database_name"

echo "Exporting database: "$db_name
mysqldump -uroot -p $db_name > $db_name"_data_"$today.sql
