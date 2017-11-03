/// <summary>
/// 图片转二进制
/// </summary>
/// <param name="picPath">图片路径</param>
/// <returns></returns>
private byte[] GetPictureBytes(string picPath)
{
	using (FileStream fs = new FileStream(picPath, FileMode.Open, FileAccess.Read))
	{
		byte[] fileData = new byte[fs.Length];
		fs.Read(fileData, 0, fileData.Length);
		return fileData;
	}
}