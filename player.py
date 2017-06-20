# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:21:51 2016

@author: Ajinkya
"""
import board
import search
class Player:
    def __init__(self):

#player board

        self.b=board.Board()

#define player name

    def name(self):
        name=" "
        return name

#make move

    def make_move(self,c):
        self.b.make_move(c)

#return move using alpha beta pruning 
    
    def get_move(self):
        move=search.negamax_root_alphabeta(self.b)
        return move[1]
    
    def __str__(self):
        return (self.b.__str__())