# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:34:09 2020

@author: ABC
"""

import random
import profile
 
#四则运算
 
def xxsf():
 
    sym = ['＋', '－', '×', '÷']
 
    f= random.randint(0, 3)#用于随机出算法题
 
    n1 = random.randint(1, 100)
 
    n2 = random.randint(1, 100)
 
    result = 0
    yu = 0
    flag = 0
 
    if f== 0:#加法
 
       result  = n1 + n2
 
    elif f == 1:#减法，要先比较大小，防止输出负数
 
        n1, n2 = max(n1, n2), min(n1, n2)
 
        result  = n1 - n2
 
    elif f== 2:#乘法
 
        result  = n1 * n2
 
    elif f == 3:#除法，要比较大小，并循环取整除
 
        n1, n2 = max(n1, n2), min(n1, n2)
 
        result  = int(n1 / n2)
        yu = n1%n2
        flag = 1
 
    print(n1, sym[f], n2, '= ', end='')
 
    return result,yu,flag
 
  
 
#制作题库
 
def test():
    sym = ['＋', '－', '×', '÷']
 
    print('输入所需要的题目数量')
 
    n=int(input())
 
    result =[]
    yu = []
    flag = []
 
    m=0
 
    while m<=(n-1):
 
        print(m+1,end='、')
        xxsf1 = xxsf()
        result .append(xxsf1[0])
        yu .append(xxsf1[1])
        flag .append(xxsf1[2])
 
        print(' ')
 
        m=m+1
 
    m=0
 
    print('对应的答案：')
 
    while m<=(n-1):
        if flag[m] == 1:
            print(m+1,'、',result [m],'   除法余数为：',yu [m])
        else:
            print(m+1,'、',result [m])
 
        m=m+1
 
  
profile.run('xxsf()')#对xxsf函数进行效能分析
print('\n')
profile.run('test()')#对test函数进行效能分析
print('\n')
 
print('选择想要的模式')
 
print('1、进行四则运算')
 
print('2、制作题库(可选择模式有：1与2)')
 
n=int(input())
 
#当输入1时，进行四则运算，调用函数xxsf()
 
if n==1:
 
    while True:
        xxsf1 = xxsf()
        result  = xxsf1[0]
        yu  = xxsf1[1]
        flag  = xxsf1[2]
        
        j= input()
        s= int(j)
        
        if flag ==1:
            x = input()
            y = int(x)
            if s== result and y== yu:
 
                print('right')
 
            else:
 
                print('error.the answer is', result ,'   余数为：',yu)
        elif flag != 1:
            if s== result:
 
                print('right')
 
            else:
 
                print('error.the answer is', result )
 
#当输入2时，进行制作题库
 
if n==2:
 
     test()