from copy import deepcopy
from locale import currency
from board import Board

import pygame

#position -> der Status des Boards also die Position der Steine
#depth -> wie tief man in den Tree vordringt (die bestmöglichen Züge vorraussagen)
#maximizing_player -> boolean | gucken ob maximieren oder minimieren | wenn maximizing_player = false => minimieren
#game -> ist das Game was gespielt wird
def minimax(position, depth, maximizing_player): #alpha, beta

    # board.is_human_turn = not maximizing_player
    # children = board.get_all_possible_moves()

#erstmal testen ob das Game noch läuft bzw. vorbei ist
    if depth == 0:
        return position.evaluate(), position

    

    if maximizing_player:
        max_eval = float('-inf') #für den MaxPlayer ist negative Unendlichekit (-inf) am besten
        best_move = None
        for move in get_all_moves(position, "black"): #Die Ki ist immer Schwarz
            
            current_eval = minimax(move, depth - 1, False)[1]
            print("current",current_eval)

            max_eval = max(max_eval, current_eval)
            
            if current_eval >= max_eval:
                max_eval = current_eval
                best_move = move
        return best_move, max_eval

    else:
        min_eval = float('+inf') #für den MinPlayer ist positive Unendlichekit (+inf) am besten
        best_move = None
        for move in get_all_moves(position, "white"): #Der Player ist immer weiß
            current_eval = minimax(move, depth - 1, True)[1]
            min_eval = min(min_eval, current_eval)
            if current_eval <= min_eval:
                min_eval = current_eval
                best_move = move
        return best_move, min_eval


def simulate_move(piece, move, board):
    board.move(piece, move)
    return board

#herausfinden wo alle steine stehen und deren möglichen Züge rausfinden
def get_all_moves(board, color):
    moves = []
    for index, piece in enumerate(board.get_all_pices(color)):
        valid_moves = board.checkPossibleMovesComp(piece[0],piece[1],color) #(row, col): [pieces]
        for item in valid_moves:
            if(item):
                for move in item:
                    for rowIndex, column in enumerate(board.fieldArray2D):
                        for columnIndex, field in enumerate(column):
                            field.unsetSurface()
                            if(field.getPawn()!=None):
                                field.getPawn().unsetSprite()

                    temp_surface = board.surface
                    board.surface = None
                    temp_board = deepcopy(board) # immer ein neues Board "erstellen" 
                    for rowIndex, column in enumerate(board.fieldArray2D):
                        for columnIndex, field in enumerate(column):
                            field.setSurface()
                            if(field.getPawn()!=None):
                                field.getPawn().setSprite()
                    board.surface = temp_surface
                    new_board = simulate_move(piece, move, temp_board)
                    moves.append(new_board)
    return moves



 # alpha = max(alpha, current_eval)
            # if beta <= alpha:
            #     break