# -*- coding: utf-8 -*-
"""Taller2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u_ZX2-ANib_8dZ4oeV9CLyThQyLvpdBg
"""

A={6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
B={2,4,6,8,10,12,14,16,18,20,22,24}
C={1,4,8,10,12,15,18,20}
D={2,3,5,7,11,13,17,19,23,29,31,37,41,43}
def union(C1,C2):
  C3=C1|C2
  return C3
def interseccion(C1,C2):
  C3=C1&C2
  return C3
def diferencia(C1,C2):
  C3=C1-C2
  return C3
def difsimetrica(C1,C2):
  C3=C1^C2
  return C3
O1=interseccion(B,difsimetrica(C,D))
O2=union(B,interseccion(A,C))
O3=diferencia(union(B,D),C)
O4=difsimetrica(diferencia(A,B),interseccion(A,D))

O1

O2

O3

O4