#!/usr/bin/env python
# -*- coding: utf-8 -*-

#集合 & tuple
list = [1, 2, 3]
trupe = ('x', 'y', 'z')
#loop
for x in trupe:
    print x

#use method
print abs(-100)
print cmp(1, 1)
a = abs
print 'a=abs', a(-1)

#function
def my_abs(x):
    if x >= 0:
        return x;
    if x < 0:
        return -x;

print my_abs(-2)

age = 19
#if elif else
if age>18:
    pass
print my_abs('A')


def my_abss(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operad type") #抛出一个异常 如果x的值不是整型或者浮点数
    if x >= 0:
        return x
    else:
        return -x

print my_abss(-3) #调用自定义方法
