# -*- coding:utf-8 -*-
import os

#列举当前目录下的所有文件，并将文件的列表作为字符串返回
#优点：可以使用相同方法加载模块使接口更加通用，提供充分的扩展能力

def run(**args):
    print "[*] In dirlister module"
    files = os.listdir(".")

    return str(files)

