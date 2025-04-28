import chess
from utils.evaluation import evaluate_board

class AlphaBetaAgent:
    def __init__(self, depth=2):
        self.depth = depth

    def select_move(self, board):
        best_move = None
        best_value = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        for move in board.legal_moves:
            board.push(move)
            board_value = self.alphabeta(board, self.depth - 1, alpha, beta, False)
            board.pop()
            if board_value > best_value:
                best_value = board_value
                best_move = move
        return best_move

    def alphabeta(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or board.is_game_over():
            return evaluate_board(board)

        if maximizing:
            max_eval = float('-inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.alphabeta(board, depth - 1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.alphabeta(board, depth - 1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
