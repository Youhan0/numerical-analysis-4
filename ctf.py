# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:53:18 2018

@author: Youhan0
"""

"""compound trapezoidal formula"""
"""复合梯形公式"""
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
T=[]
while(true==1):
    print("n=",n)
    h=(b-a)/n
    #T=0.0
    t=0.0
    for k in range(n):
        xk=a+k*h
        if xk==0.0: 
            t+=1+y.subs(x,xk+h)
        else:
            t+=y.subs(x,xk)+y.subs(x,xk+h)
    T.append(h/2*t)
    print("Tn=",T[n-1])
    
    if n>=2 and abs(T[n-2]-T[n-1])<=1e-6:
        true=0
    n=n+1

