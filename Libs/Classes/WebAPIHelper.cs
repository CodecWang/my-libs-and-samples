/* C# WebAPI访问助手
 * Version：1.0
 * ex2tron 2017/06/28
 * 测试的URL：string url = "https://api.douban.com/v2/book/isbn/:9787121022982";
 * http://ex2tron.lofter.com
 */

using System.IO;
using System.Net;

namespace Ex2tronLibs.Helper
{
    class WebAPIHelper
    {
        /// <summary>
        /// 得到URL响应的原始字符串
        /// </summary>
        /// <param name="url">要请求的URL</param>
        /// <returns>URL响应字符串</returns>
        public static string GetResponseString(string url)
        {
            string originString=string.Empty;

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();

            using (StreamReader sr = new StreamReader(response.GetResponseStream()))
            {
                originString = sr.ReadToEnd();
            }

            return originString;
        }
    }
}
