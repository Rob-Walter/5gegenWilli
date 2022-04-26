from copy import deepcopy
from board import Board

import pygame

#Die Farbe der Steine
WHITE = (255,255,255)
BLACK = (0,0,0)

#board -> der Status des Boards also die Position der Steine
#depth -> wie tief man in den Tree vordringt (die bestmöglichen Züge vorraussagen)
#maximizing_player -> gucken ob maximieren oder minimieren | wenn maximizing_player = false => minimieren
def minimax(board, depth, maximizing_player): #alpha, beta

    board.is_human_turn = not maximizing_player
    children = board.get_all_possible_moves()

    if depth == 0 or board.is_draw or board.is_check_mate:
        return None, evaluate(board)

    best_move = random.choice(children)

    if maximizing_player:
        max_eval = -math.inf
        for child in children:
            board_copy = copy.deepcopy(board)
            board_copy.move(child)
            current_eval = minimax(board_copy, depth - 1, alpha, beta, False)[1]
            if current_eval > max_eval:
                max_eval = current_eval
                best_move = child
            alpha = max(alpha, current_eval)
            if beta <= alpha:
                break
        return best_move, max_eval

    else:
        min_eval = math.inf
        for child in children:
            board_copy = copy.deepcopy(board)
            board_copy.move(child)
            current_eval = minimax(board_copy, depth - 1, alpha, beta, True)[1]
            if current_eval < min_eval:
                min_eval = current_eval
                best_move = child
            beta = min(beta, current_eval)
            if beta <= alpha:
                break
        return best_move, min_eval