from copy import deepcopy
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
            current_eval = minimax(position, depth - 1, False)[0]
            max_eval = max(max_eval, current_eval)
            if current_eval == max_eval:
                max_eval = current_eval
                best_move = move
        return best_move, max_eval

    else:
        min_eval = float('+inf') #für den MinPlayer ist positive Unendlichekit (+inf) am besten
        best_move = None
        for move in get_all_moves(position, "WHITE"): #Der Player ist immer weiß
            current_eval = minimax(move, depth - 1, True)[0]
            min_eval = min(min_eval, current_eval)
            if current_eval == min_eval:
                min_eval = current_eval
                best_move = move
        return best_move, min_eval


def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

#herausfinden wo alle steine stehen und deren möglichen Züge rausfinden
def get_all_moves(board, color):
    moves = []
    for index, piece in enumerate(board.get_all_pices(color)):
        valid_moves = board.checkPossibleMovesComp(piece[0],piece[1],color) #(row, col): [pieces]
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board) # immer ein neues Board "erstellen" 
            new_board = simulate_move(piece, move, temp_board, skip)
            moves.append(new_board)
    
    return moves



 # alpha = max(alpha, current_eval)
            # if beta <= alpha:
            #     break