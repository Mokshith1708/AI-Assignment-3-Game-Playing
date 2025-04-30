import chess
from utils.evaluation1 import evaluate_board

class MinimaxAgent:
    def __init__(self, depth=2):
        self.depth = depth

    def select_move(self, board):
        best_move = None
        best_value = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            board_value = self.minimax(board, self.depth - 1, False)
            board.pop()
            if board_value > best_value:
                best_value = board_value
                best_move = move
        return best_move

    def minimax(self, board, depth, maximizing):
        if depth == 0 or board.is_game_over():
            return evaluate_board(board)

        if maximizing:
            max_eval = float('-inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, False)
                board.pop()
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, True)
                board.pop()
                min_eval = min(min_eval, eval)
            return min_eval
