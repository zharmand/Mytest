# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 21:13:10 2016

@author: zharmand
"""


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("192.168.100.107", 3000))
s.connect(("192.168.100.10", 3000))

#s.close()