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

# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
# 先定义一个函数，传入一个list，添加一个END再返回：
# def add_end(L=[]):
#     L.append('END')
#     return L
# 当你正常调用时，结果似乎不错：
# >>> add_end([1, 2, 3])
# [1, 2, 3, 'END']
# >>> add_end(['x', 'y', 'z'])
# ['x', 'y', 'z', 'END']
# 当你使用默认参数调用时，一开始结果也是对的：
# >>> add_end()
# ['END']
# 但是，再次调用add_end()时，结果就不对了：
# >>> add_end()
# ['END', 'END']
# >>> add_end()
# ['END', 'END', 'END']
# 很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#
# 要修改上面的例子，我们可以用None这个不变对象来实现：
#
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# 现在，无论调用多少次，都不会有问题：
#
# >>> add_end()
# ['END']
# >>> add_end()
# ['END']
# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

def add_end(L=[]):
    L.append('end')
    return L

print add_end([1,2,3])
print add_end(['x','y','z'])
print add_end()
print add_end()


#不变对象 none
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end2()
print add_end2()




