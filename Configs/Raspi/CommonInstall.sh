sudo apt-get update

# 安装中文输入法
sudo apt-get install scim-pinyin
scim

# 安装opencv
sudo apt-get install libopencv-dev
sudo apt-get install libcv-dev  

# 原来的opencv库目录在/usr/lib/arm-linux-gnueabihf中
# 现在拷贝到/usr/lib中
sudo cd /usr/lib/arm-linux-gnueabihf/  
sudo cp *opencv*.so /usr/lib 
cd /usr/lib
sudo find -name "*opencv*.so"

#安装qt
sudo apt-get install qt5-default  
sudo apt-get install qtcreator  

#安装QTSerialPort
sudo apt-get install libqt5serialport5-dev libudev-dev

# 更改键盘布局
sudo dpkg-reconfigure keyboard-configuration
# Generic 101-key PC -> Other -> Engligh(US) -> English(US)-English (US, alternative international)

# 重启
sudo reboot

# 最新版已经自带VNCServer，只需要启用一下
sudo raspi-config
-> Interfacing Options->VNC->Yes enable->sudo reboot

# 如果没有按照这个：安装和配置VNC
sudo apt-get install tightvncserver
# 设置密码
vncpasswd
# 删除密码重新设置
rm .vnc -r
vncpasswd
# 运行vncserver
tightvncserver


# 安装xclip
sudo apt-get install xclip

# deb文件安装
sudo dpkg -i xx.deb
