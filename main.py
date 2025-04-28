import chess
import gym
import gym_chess
import time
import os 

from chess_env import make_chess_env
from agents.minimax_agent import MinimaxAgent
from agents.alphabeta_agent import AlphaBetaAgent

def play_game(agent_white, agent_black, record=False):
    env = make_chess_env()
    board = env.reset() 
    moves = []

    while not board.is_game_over():
        if board.turn:  # White's turn
            move = agent_white.select_move(board)
        else:  # Black's turn
            move = agent_black.select_move(board)

        board.push(move)
        moves.append(move.uci()) 
        print(board)
        print()
    
    if board.is_game_over():
        print("The game is over.")
        if board.is_checkmate():
            print("Checkmate!")
        elif board.is_stalemate():
            print("Stalemate!")
        elif board.is_insufficient_material():
            print("Insufficient material!")
        elif board.is_fifty_moves():
            print("Fifty-move rule!")
        elif board.is_fivefold_repetition():
            print("fivefold repetition!")


    result = board.result()
    print("Game Result:", result)

    if record:
        if not os.path.exists('videos'):
            os.makedirs('videos')
        with open('videos/game_moves.txt', 'w') as f:
            for m in moves:
                f.write(m + '\n')


if __name__ == "__main__":
    minimax1 = MinimaxAgent(depth=1)
    minimax2 = MinimaxAgent(depth=4)
    alphabeta = AlphaBetaAgent(depth=1)
    print("Playing Minimax vs AlphaBeta")
    play_game(minimax1, minimax2, record=True)
