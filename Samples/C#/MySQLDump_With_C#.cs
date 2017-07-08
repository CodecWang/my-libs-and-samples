/* 使用CMD导入和导出数据库 
 * ex2tron 2017/07/05
 * http://ex2tron.lofter.com
*/
using System;
using System.Diagnostics;

namespace MySQLDump_With_CSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            /* 导出数据库 */
            //指定工作目录
            //RunCmd("D:\\", "mysqldump -uroot -ppwd books>books.sql");
            //或指定备份路劲
            //RunCmd("mysqldump -uroot -ppwd books> D:\\books.sql");

            /* 导入数据库 */
            RunCmd("mysql -uroot -ppwd -D books < D:\\books.sql");
            Console.ReadKey();
        }

        public static void RunCmd(String workingDirectory, String command)
        {
            Process proc = new Process();
            proc.StartInfo.FileName = "cmd.exe";
            proc.StartInfo.WorkingDirectory = workingDirectory;
            //禁用系统Shell启动 
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.RedirectStandardInput = true;
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.RedirectStandardError = true;
            //不新建窗口,相当于隐藏界面 
            proc.StartInfo.CreateNoWindow = true;
            proc.Start();
            proc.StandardInput.WriteLine(command);
            proc.StandardInput.WriteLine("exit");
        }

        public static void RunCmd(String command)
        {
            Process proc = new Process();
            proc.StartInfo.FileName = "cmd.exe";
            //禁用系统Shell启动 
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.RedirectStandardInput = true;
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.RedirectStandardError = true;
            //不新建窗口,相当于隐藏界面 
            proc.StartInfo.CreateNoWindow = true;
            proc.Start();
            proc.StandardInput.WriteLine(command);
            proc.StandardInput.WriteLine("exit");
        }
    }
}
