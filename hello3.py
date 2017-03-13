#!/usr/bin/env python
# -*- coding: utf-8 -*-

#可变参数  在参数名前面加*
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum

print calc(1,2,3,4)

num = [1,3,4]

#如果把集合或者元组传入可变参数中 直接在要传入名字前加*
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print calc(*num)

#关键字参数 **

def person(name,age,**km):
    print 'name',name
    print 'age' ,age
    print km

person('Herry',18,sex='M',height='185')

extra = {'city:':'ShiJiazhuang','job:':'Programmer Engineer'}
person('Herry2',22, city=extra['city:'],job=extra['job:']) #繁琐写法
person('Herry3',22,**extra) #简易写法




