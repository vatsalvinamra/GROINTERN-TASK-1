import random

def create_board():
  board = []
  for i in range(3):
    row = []
    for j in range(3):
      row.append("-")
    board.append(row)
  return board

def print_board(board):
  for row in board:
    print(" ".join(row))

def get_player_move(board):
  while True:
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "-":
      return row, col
    else:
      print("Invalid move.")

def check_winner(board):
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != '-':
      return board[i][0]
    if board[0][i] == board[1][i] == board[2][i] != '-':
      return board[0][i]
  if board[0][0] == board[1][1] == board[2][2] != '-' or board[0][2] == board[1][1] == board[2][0] != '-':
    return board[1][1]
  return None

def main():
  board = create_board()
  player = random.randint(1, 2)
  while True:
    if player == 1:
      symbol = "X"
    else:
      symbol = "O"
    row, col = get_player_move(board)
    board[row][col] = symbol
    winner = check_winner(board)
    if winner:
      print(f"Player {winner} wins!")
      break
    print_board(board)
    player = 3 - player

if __name__ == "__main__":
  main()
