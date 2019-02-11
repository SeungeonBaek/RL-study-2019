# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:30:09 2018

@author: seung eon
"""
import math as m
import collections as collec
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
p1 = Point2D(x=30, y=20) # 점1
p2 = Point2D(x=60, y=50) # 점2

print('p1: {} {}'.format(p1.x, p1.y))
print('p2: {} {}'.format(p2.x, p2.y))

a = p2.x - p1.x
b = p2.y - p1.y

c = m.sqrt(a**2+b**2)
print('(30,20)과 (60,20)사이 거리는:',c)

point_2D = collec.namedtuple('Point2D',['x', 'y'])
