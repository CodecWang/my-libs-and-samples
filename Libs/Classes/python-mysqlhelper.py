# Python MySQL连接助手
# Version：1.0
# Python版本：3.6.3
# ex2tron 2017年11月18日
# http://ex2tron.top
# 官方文档：http://pymysql.readthedocs.io/en/latest/

#%%
import pymysql


#%%
class MySQLHelper():
    '''
    Python-MySQL数据库连接助手
    '''

    def __init__(self, host, user, passwd, db, charset='utf8'):
        '''
        初始化MySQL连接 
        '''
        try:
            self.connection = pymysql.connect(
                host, user, passwd, db, charset=charset)
            self.cursor = self.connection.cursor()
            self.cursor.execute('select version()')
            data = self.cursor.fetchone()
            print('Connected. Server version: %s' % data)
        except Exception as e:
            print(e)

    def close(self):
        '''
        释放相关资源
        '''
        self.connection.close()
        self.cursor.close()

    def execute_non_query(self, query):
        '''
        增、删、改及其他数据操作
        '''
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print('Operation succeeds.')
        except Exception as e:
            self.connection.rollback()
            print('Error: %s' % e)

    def execute_query(self, query):
        '''
        查数据操作
        '''
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print('Error: %s' % e)
            return None
