# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:34:05 2016

@author: Ajinkya
"""
import search
import numpy as np
class Board:
    def __init__(self):
        global board
        self.track=[0 for i in range(7)]
        global move_stack
        board=[[0 for i in range(7)]for j in range(6)]
        move_stack=[]
        global my_move
        my_move=[]
        global opp_move
        opp_move=[]
        self.turn=True

#generate all possible moves
        
    def generate_moves(self):
        all_moves=[]
        for i in range (7):
            if self.track[i]<6:
                all_moves.append(i)
        return all_moves
        
#make your move and set your turn to false

    def make_move(self,c):
        if self.turn:
            board[self.track[c]][c]=1
            self.track[c]+=1
            move_stack.append(c)
            temp=[self.track[c]-1,c]
            my_move.append(temp)
            self.turn=False
        else:
    
            board[self.track[c]][c]=2
            self.track[c]+=1
            move_stack.append(c)  
            temp=[self.track[c]-1,c]
            opp_move.append(temp)
            self.turn=True

#unmake your last move, update tree with reward
          
    def unmake_last_move(self):
        
        c=move_stack.pop()
        self.track[c]-=1
        board[self.track[c]][c]=0
        if self.turn:
            opp_move.pop()
        else:
            my_move.pop()
        if self.turn:
            self.turn=False
        else:
            self.turn=True
    


    def check_matrix(self):
        for i in range(7):
            for j in range(6):
                if board[i][j]==0:
                    return False
        return True
                
#check if the last move won the game

    def last_move_won(self):
        #check for horizontal
        for tile in (1,3):
            for y in range(7):
                for x in range(3):
                    if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                        return True

    # check vertical spaces
            for x in range(6):
                for y in range(4):
                    if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                        return True
        
            # check / diagonal spaces
            for x in range(3):
                for y in range(3, 7):
                    if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                        return True
        
            # check \ diagonal spaces
            for x in range(3):
                for y in range(4):
                    if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] ==tile:
                        return True
                        
            return False
    
    def __str__(self):
        return str(np.matrix(board))
        
        