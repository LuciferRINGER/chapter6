# -*- coding:utf-8 -*-
import os

#获取远程机器上的环境变量
def run(**args):
    print "[*] In environment module"
    return str(os.environ)
