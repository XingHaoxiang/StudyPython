#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi / 6)

print x,y

#默认的参数定义 用来计算x的平方
def power(x):
    return x * x

#参数的定义 def power(x,n)  用来扩展上面的方法，N为具体的几次方
# def power(x,n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s;

#把n设置为默认参数 如果不传入就使用默认
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s;

print power(2)

# #写一个学生注册的方法
# def enroll(name,gender):
#     print 'name',name
#     print 'gender',gender
#
# #调用学生注册
# enroll('herry',"M")

#重写上面的方法 age 和 city为默认

def enroll(name,gender,age = 16,city='ShiJiazhuang'):
    print 'name',name
    print 'gender',gender
    print 'age',age
    print 'city',city
enroll('herry','M')
enroll('XingHaoxiang','M',city='HeBeiSJZ')
