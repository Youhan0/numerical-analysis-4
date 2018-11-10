# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:57:36 2018

@author: 闫汝海
"""

"""compound Simpson formula"""
"""复合辛普森公式"""
from sympy import *

"""
这里用函数f(x)=sin(x)/x,区间为(0,1),区间上积分的准确值为I=0.9460831
"""
#I=0.9460831
x=symbols('x')
y=sin(x)/x
a=0.0
b=1.0
n=1
true=1
S=[]
i=0
while(true==1):
    print("n=",n)
    h=(b-a)/n
    t=0.0
    for k in range(n):
        xk=a+k*h
        if xk==0.0: 
            t+=1+4*y.subs(x,xk+h/2)+y.subs(x,xk+h)
        else:
            t+=y.subs(x,xk)+4*y.subs(x,xk+h/2)+y.subs(x,xk+h)
    S.append(h/6*t)
    print("Sn=",S[i])
    if i>=2 and abs(S[i-2]-S[i-1])<=1e-8:
        true=0
    n=2*n
    i=i+1

