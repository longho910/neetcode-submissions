class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        res = 0
        while top <= bot:
            row = (top + bot) // 2
            res = row
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[res][mid]:
                l = mid + 1
            elif target < matrix[res][mid]:
                r = mid - 1
            else:
                return True

        return False


