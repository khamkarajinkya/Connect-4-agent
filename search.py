# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:00:29 2016

@author: Ajinkya
"""
import board
import numpy as np

#perft(board, depth) that accepts a board object and a natural number called depth and returns the number of leaves of the search tree up to depth

def perft(b,depth):
    if (depth==0 or b.last_move_won()):
        return 1
    else:
        s=0
        child=b.generate_moves()
        #print child
        for move in child:
            b.make_move(move)
            
            
            s=s+perft(b,depth-1)
            b.unmake_last_move()


    return s

#implementation of the mini-max algorithm with alpha beta pruning search

def negamax(b,depth):
    if b.last_move_won():
            return -1
    if depth==0:
            return 0
    

    count=0
    child=b.generate_moves()
    #print child
    values=[]
    for move in child:
        b.make_move(move)
        values.append(-1*(negamax(b,depth-1)))
                        
        b.unmake_last_move()
        count+=1
    
    return max(values)
    
def negamax_root(b,depth):
    if b.last_move_won() and b.turn==False:
        return (1,None)
    if b.last_move_won() and b.turn==True:
        return (-1,None)
    
    values=[]
    child=b.generate_moves()
    for move in child:
        b.make_move(move)
        values.append((-1*(negamax(b,depth-1)),move))
        b.unmake_last_move()
    return (max(values,key=lambda k:k[0]))

def find_win(b,depth):
    value=negamax_root(b,depth)
    if value[0]==-1:
        return ("ALL MOVES LOSE")
    if value[0]==0:
        return ("NO FORCED WIN IN "+str(depth)+" MOVES")
    if value[0]==1:
        return ("WIN BY PLAYING "+str(value[1]))

def alphabeta_negamax(b,depth,a,be):
    if b.last_move_won():
            return -1
    if depth==0:
            return 0

    child=b.generate_moves()
    #print child
    values=[]
    if not child:
        return 0
    best=-1000
    for move in child:
        b.make_move(move)
        value=-(alphabeta_negamax(b,depth-1,-be,-a))
    
        b.unmake_last_move()
    
        if value>best:
            best=value
        if a > value:
            a=value
        if a>=be:
            break
    return best
    
def negamax_root_alphabeta(b):
    if b.last_move_won() and b.turn==False:
        return (1,None)
    if b.last_move_won() and b.turn==True:
        return (-1,None)
    
    values=[]
    child=b.generate_moves()
    for move in child:
        b.make_move(move)
        values.append((-1*(alphabeta_negamax(b,5,- 1000,1000)),move))
        b.unmake_last_move()
        if b.turn==True:
            b.turn=False
        else:
            b.turn=True
    return (max(values,key=lambda k:k[0]))