from sympy import *


def tudy(a,b,c):
    a = complex(a)
    b = complex(b)   
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        return a/b 