class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True

        
"""
To solve this, we use a hash set for the rows, columns, and 3x3 squares within the sudoku set.

To calculate which square we're in, we divide the row and column by 3 to figure out if it's in square 0, 1, 2, ... nth square.

Within each hash maps contain a set for each row, column, or square, which is used to track duplicates.

Return false if we find a duplicate in one of the hashmaps during iteration, True if we are finished iteration of the board.
"""