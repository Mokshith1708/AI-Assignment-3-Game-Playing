import chess
import os
import cairosvg
import chess.svg
import chess.pgn
import cv2
import glob
from chess_env import make_chess_env
from agents.minimax_agent import MinimaxAgent
from agents.alphabeta_agent import AlphaBetaAgent

def save_board_as_png(board, move_number, folder='images'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    svg = chess.svg.board(board=board)
    filepath = os.path.join(folder, f'board_{move_number:03d}.png')
    cairosvg.svg2png(bytestring=svg.encode('utf-8'), write_to=filepath)

def save_pgn(moves, filename='pgn/game.pgn'):
    game = chess.pgn.Game()
    node = game
    for uci_move in moves:
        move = chess.Move.from_uci(uci_move)
        node = node.add_variation(move)
    if not os.path.exists('pgn'):
        os.makedirs('pgn')
    with open(filename, 'w') as pgn_file:
        print(game, file=pgn_file)

def create_video_from_images(image_folder='images', video_filename='videos/game2.mp4', fps=1):
    image_files = sorted(glob.glob(os.path.join(image_folder, 'board_*.png')))
    if not image_files:
        print("No board images found.")
        return

    # Read first image to get frame size
    frame = cv2.imread(image_files[0])
    height, width, _ = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

    for image_file in image_files:
        frame = cv2.imread(image_file)
        out.write(frame)

    out.release()
    print(f"Video saved to: {video_filename}")

def play_game(agent_white, agent_black, record=False):
    env = make_chess_env()
    board = env.reset() 
    moves = []

    if record:
        save_board_as_png(board, 0)

    while not board.is_game_over():
        if board.turn:
            move = agent_white.select_move(board)
        else:
            move = agent_black.select_move(board)

        board.push(move)
        moves.append(move.uci())
        print(board)
        print()

        if record:
            save_board_as_png(board, len(moves))

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
        print("Fivefold repetition!")

    result = board.result()
    print("Game Result:", result)

    if record:
        if not os.path.exists('videos'):
            os.makedirs('videos')
        with open('videos/game_moves4.txt', 'w') as f:
            for m in moves:
                f.write(m + '\n')

        save_pgn(moves)
        create_video_from_images()

if __name__ == "__main__":
    minimax1 = MinimaxAgent(depth=1)
    minimax2 = MinimaxAgent(depth=4)
    alphabeta1 = AlphaBetaAgent(depth=1)
    alphabeta2 = AlphaBetaAgent(depth=4)
    play_game(alphabeta1, alphabeta2, record=True)
