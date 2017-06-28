/* C# MySQL连接助手
 * Version：1.1
 * ex2tron 2017年5月31日
 * http://ex2tron.lofter.com
 */

using System;
using System.Data;
using System.Collections.Generic;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace Ex2tronLibs.Helper
{
    class MySQLHelper
    {
        /// <summary>
        /// MySQL连接
        /// </summary>
        MySqlConnection Connection;

        /// <summary>
        /// 用连接字符串初始化MySQL连接
        /// </summary>
        /// <param name="connStr">连接字符串</param>
        public MySQLHelper(string connStr)
        {
            Connection = new MySqlConnection(connStr);
            try
            {
                Connection.Open();
            }
            catch (Exception ex)
            {
                ShowErrorMessage(ex.Message);
            }
        }

        /// <summary>
        /// 用服务器相关信息初始化MySQL连接
        /// </summary>
        /// <param name="serverIp">服务器IP</param>
        /// <param name="uid">MySQL用户名</param>
        /// <param name="pwd">MySQL密码</param>
        /// <param name="database">数据库名</param>
        public MySQLHelper(string serverIp, string uid, string pwd, string database)
        {
            string connStr = string.Format("server={0};uid={1};password={2};database={3};charset=utf8", serverIp, uid, pwd, database);
            Connection = new MySqlConnection(connStr);

            try
            {
                Connection.Open();
            }
            catch (Exception ex)
            {
                ShowErrorMessage(ex.Message);
            }
        }

        /// <summary>
        /// 查询整表数据
        /// </summary>
        /// <param name="query">Sql语句</param>
        /// <returns>查询的数据表</returns>
        public DataTable SelectDataTable(string query)
        {
            DataTable dt = new DataTable();
            try
            {
                MySqlCommand cmd = new MySqlCommand(query, Connection);
                MySqlDataAdapter adp = new MySqlDataAdapter(cmd);
                adp.Fill(dt);
            }
            catch (Exception ex)
            {
                ShowErrorMessage(ex.Message);
            }

            return dt;
        }

        /// <summary>
        /// 查询数据库中的单条字段信息
        /// </summary>
        /// <param name="query">Sql语句</param>
        /// <param name="keyword">要查询的字段</param>
        /// <returns>查询结果</returns>
        public List<string> SelectValueByKeyWord(string query, string keyword)
        {
            List<string> result = new List<string>();

            try
            {
                MySqlCommand cmd = new MySqlCommand(query, Connection);
                MySqlDataReader dataReader = cmd.ExecuteReader();
                while (dataReader.Read())
                {
                    result.Add(dataReader.GetString(keyword));
                }
				dataReader.Close();
            }
            catch (Exception ex)
            {
                ShowErrorMessage(ex.Message);
            }

            return result;
        }

        /// <summary>
        /// 查询数量信息
        /// </summary>
        /// <param name="query">Sql语句</param>
        /// <returns>数量</returns>
        public int SelectCount(string query)
        {
            int count = -1;

            try
            {
                MySqlCommand cmd = new MySqlCommand(query, Connection);
                count = int.Parse(cmd.ExecuteScalar().ToString());
            }
            catch (Exception ex)
            {
                ShowErrorMessage(ex.Message);
            }

            return count;
        }

        /// <summary>
        /// 执行更新、插入、删除Sql命令
        /// </summary>
        /// <param name="query">Sql语句</param>
        /// <returns>是否执行成功</returns>
        public bool ExecuteCommand(string query)
        {
            bool isSucceed = false;

            try
            {
                MySqlCommand cmd = new MySqlCommand(query, Connection);
                cmd.ExecuteNonQuery();
                isSucceed = true;
            }
            catch (Exception ex)
            {
                ShowErrorMessage(ex.Message);
            }

            return isSucceed;
        }

        /// <summary>
        /// 关闭MySql连接并释放资源
        /// </summary>
        public void Dispose()
        {
            try
            {
                Connection.Close();
                Connection.Dispose();
            }
            catch (Exception ex)
            {
                ShowErrorMessage(ex.Message);
            }
        }

        /// <summary>
        /// 处理错误信息
        /// </summary>
        /// <param name="error">错误信息</param>
        private void ShowErrorMessage(string error)
        {
            MessageBox.Show(error);
        }
    }
}
