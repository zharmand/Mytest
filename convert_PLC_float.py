# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:36:44 2016

@author: zharmand
"""
import struct

def convert_PLC_float(m):
    n=''
    l=len(m)
    for i in range(l):
        n=n+m[l-i-1]
    return struct.unpack('<f', n)[0]