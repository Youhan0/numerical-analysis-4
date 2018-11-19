# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:53:10 2018

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
                t+=1+y.subs(x,xk+h)
            else:
                t+=y.subs(x,xk)+y.subs(x,xk+h)
        T.append(h/2*t)
        n=2*n
        i+=1
    return T

def Sn(y,x,a,b,num):
    S=[]
    T=Tn(y,x,a,b,num+1)
    for i in range(num):
        S.append(4/3*T[i+1]-1/3*T[i])
    return S

def Cn(y,x,a,b,num):
    C=[]
    S=Sn(y,x,a,b,num+1)
    for i in range(num):
        C.append(16/15*S[i+1]-1/15*S[i])
    return C

def R(y,x,a,b,num):
    R=[]
    C=Cn(y,x,a,b,num+1)
    for i in range(num):
        R.append(64/63*C[i+1]-1/63*C[i])
    return R

def romberg(y,x,a,b,tol):
    R1=R(y,x,a,b,1)
    R2=R(y,x,a,b,2)
    i=2
    while abs(R1[len(R1)-1]-R2[len(R2)-1])>tol:
        R1=R2
        R2=R(y,x,a,b,i)
        i+=1
    return R2[len(R2)-1]

"""main"""
x=symbols('x')
y=sin(x)/x
a=0.0
b=1.0
tol=1e-6
I=romberg(y,x,a,b,tol)
print(I)

