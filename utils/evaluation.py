import chess

piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}

def evaluate_board(board):
    if board.is_checkmate():
        if board.turn:
            return -9999  # White lost
        else:
            return 9999   # Black lost
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    value = 0
    for piece_type in piece_values:
        value += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        value -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
    return value
