# reboot指令重启
# ex2tron 2017年7月26日
# http://ex2tron.xin

import os

answer=input('Are you sure?(y/n)')
if answer=='y':
    os.system('shutdown -R -T 0')