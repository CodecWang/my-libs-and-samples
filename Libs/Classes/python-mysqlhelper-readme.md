# Python-MySQLHelper帮助文档

- Python版本：3.6.3
- 需要导入模块pymysql（如无，可通过`pip install pymysql`安装）

## 示例数据库

```sql
create database db_movies charset = utf8
CREATE TABLE `tb_download` (`id` int(11) NOT NULL AUTO_INCREMENT,
                            `cn_name` char(20) DEFAULT NULL,
                            PRIMARY KEY(`id`)
                            ) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8
INSERT INTO `tb_download` VALUES(1, '肖申克的救赎'), (2, '辩护人'), (3, '西西里的美丽传说')

```

## 示例数据操作
```python
#%%
mysql = MySQLHelper('ex2tron.top', 'root', '142857', 'db_movies')
# 增
mysql.execute_non_query("insert into tb_download values(4,'泰坦尼克号')")
# 删
mysql.execute_non_query("delete from tb_download where id = 4")
# 改
mysql.execute_non_query("update tb_download set cn_name = '辩护人' where id = 2")
# 查
data = mysql.execute_query("select * from tb_download where id = 1")
print(data)
mysql.close()
```