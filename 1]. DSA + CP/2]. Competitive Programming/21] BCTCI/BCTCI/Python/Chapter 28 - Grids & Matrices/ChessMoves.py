class Solution:
    def chess_moves(self, board, piece, r, c):
        N = len(board)
        res = []
        def is_valid(r, c):
            if 0 <= r < N and 0 <= c < N and board[r][c] == 0:
                res.append([r, c])
                return True
            return False
        if piece == "knight":
            knight_directions = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
            for dr, dc in knight_directions:
                is_valid(r + dr, c + dc)
        elif piece == "king":
            king_directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            for dr, dc in king_directions:
                is_valid(r + dr, c + dc)
        elif piece == "queen":
            qeen_directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            for dr, dc in qeen_directions:
                for i in range(1, N):
                    if not is_valid(r + dr * i, c + dc * i):
                        break
        return res

if __name__ == "__main__":
    s = Solution()
    board = [[0, 0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0]]
    piece = "king"
    r = 3
    c = 5
    print(s.chess_moves(board, piece, r, c))

    board = [[0, 0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0]]
    piece = "knight"
    r = 4
    c = 3
    print(s.chess_moves(board, piece, r, c))

    board = [[0, 0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0]]
    piece = "queen"
    r = 4
    c = 4
    print(s.chess_moves(board, piece, r, c))