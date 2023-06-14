def isIntersection(board: list, x, y) -> bool:
    return board[x-1][y-1] == board[x-1][y+1] == board[x+1][y+1] == board[x+1][y-1] == '#' 

def solve(board: list):
    for y in range(1,7):
        for x in range(1,7):
            if board[y][x] == '#':
                if isIntersection(board, y, x):
                    print(y+1, x+1)
                    return

for _ in range(int(input())):
    board = []
    input()
    for row in range(8):
        board.append(input())
    solve(board)
    
