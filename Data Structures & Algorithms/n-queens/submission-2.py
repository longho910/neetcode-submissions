class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # for each row, choose a column to place a queen 
        # then go to the next row, choose another column satisfied
        # if not satisfied, go backtrack it. 
        # do this for all columns --> this is the backtrack problem / find all paths
        # we use set data structure to track the satified rules.

        cols = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r -c) in negDiag:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                dfs(r + 1)

                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        dfs(0)
        return res 