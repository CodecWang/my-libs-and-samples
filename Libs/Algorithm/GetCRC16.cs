/* CRC16 校验计算
 * ex2tron 2017年6月13日
 * http://ex2tron.lofter.com
 */

//函数测试：
byte[] data = { 0xAA,0x01 };
Console.WriteLine(GetCRC16(data, data.Length)[0]+"\r\n"+ GetCRC16(data, data.Length)[1]);

/// <summary>
/// http://baike.baidu.com/item/CRC/1453359?sefr=cr
/// </summary>
private static byte[] GetCRC16(byte[] data, int length)
{
    uint register = 0xFFFF;
    byte[] crc16 = new byte[2];

    for (int i = 0; i < length; i++)
    {
        register ^= data[i];
        for (int j = 0; j < 8; j++)
        {
            //最后一位为1，进行异或运算
            if ((register & 0x01) == 1)
            {
                //CRC-16:生成式：x16+x15+x2+1 即0x8005翻转->0xA001
                register = (register >> 1) ^ 0xA001;
            }
            else register = register >> 1;
        }
    }

    string num16 = register.ToString("X");
    crc16[0] = Convert.ToByte(num16.Substring(0, 2),16);
    crc16[1] = Convert.ToByte(num16.Substring(2, 2),16);

    return crc16;
}