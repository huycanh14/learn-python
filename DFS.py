# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 21:04:25 2020

@author: Fluke Canh
"""

from collections import defaultdict

#Tạo node
class Node:
    def __init__(self, name, par = None):
        self.name = name
        self.par = par
        
    def display(self):
        print(self.name)
        

#Tạo data
data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['E', 'F']
data['C'] = ['G', 'H']
data['D'] = ['I', 'J']
data['F'] = ['K', 'L', 'M']
data['H'] = ['N', 'O']

def equal(O, G):
    return O.name == G.name

def chekInArray(temp, Open):
    for x in Open:
        if equal(x, temp):
            return True
    return False

def path(O):
    print(O.name)
    if O.par != None:
        path(O.par)
    else:
        return

def DFS(S = Node('A'), G = Node('F')):
    Open = []
    Closed = []
    Open.append(S)
    while True:
        if len(Open) == 0:
            print("Tim kiem that bai")
            return
        O = Open.pop(0)
        Closed.append(O)
        """
            Neu O la dinh dich => Tim kiem thanh cong
            Neu ko khong thi tat ca cac dinh con khong thuoc Open va Closed cho vao dau Open
        """
        if equal(O, G):
            print("Tim kiem thanh cong")
            path(O)
            return
        pos = 0
        for x in data[O.name]:
            temp = Node(x)
            temp.par = O
            ok1 = chekInArray(temp, Open)
            ok2 = chekInArray(temp, Closed)
            if not ok1 and not ok2:
                Open.insert(pos,temp)
                pos += 1
                

DFS()
            
            
    