# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:04:43 2018

@author: Youhan0
"""

from sympy import *
import numpy as np


def Tn(y,x,a,b,num):
    n=1    
    T=[]
    i=0
    while(i<=num):
        h=(b-a)/n
        t=0.0
        for k in range(n):
            xk=a+k*h
            if xk==0.0: 
                t+=1+y.subs(x,xk+h)#因为sin(x)/x的初值x=0时无法计算0/0，所以设函数初始值为1
            else:
                t+=y.subs(x,xk)+y.subs(x,xk+h)
        T.append(h/2*t)
        n=2*n
        i+=1
    return T

def Romberg(y,x,a,b,tol):
    n=10
    """
    此处n为一开始计算的梯形公式的结果的个数，
    并以此n为保存结果的矩阵的行数和列数。
    本题n=10已经足够使用，若在实际运算量大的
    应用中n=10不够，可以设为更高的值
    """
    TT=np.matrix(np.zeros((n,n)))
    temp=Tn(y,x,a,b,n)
    for i in range(n):
        TT[(i,0)]=temp[i]
    #先把计算好的T值输入矩阵TT的第一列中
    
    def func(TT,i,j):
        if j==0:
            return TT[(i,j)]
        else:
            TT[(i,j)]=(4**j/(4**j-1))*func(TT,i+1,j-1)-(1/(4**j-1))*func(TT,i,j-1)
            return TT[(i,j)]
    #迭代法求矩阵中的下一个元素
    
    i=0
    j=0
    while abs(func(TT,i,j+1)-func(TT,i,j))>tol:
        j+=1
    #如果不满足精度，则反复计算下一个值
    
    print("i=",i)
    print("j=",j)
    print("结果为:")
    print(TT[(i,j)])
    return TT


"""----------------------------"""
"""main"""
x=symbols('x')
y=sin(x)/x
a=0.0
b=1.0
tol=1e-6
result=Romberg(y,x,a,b,tol)
print("矩阵：")
print(result)

