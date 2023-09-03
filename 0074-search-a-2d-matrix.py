# NEETCODE Best Solution:
# First we'll search all the m rows in a matrix and find the row which should have target. Then when we find that row
# we'll search that row for the target- so we are doing Binary Search twice.

# For the first part, we are given in the q thhat all rows are sorted, 
# and he first integer of each row is greater than the last integer of the previous row.
# So we'll check:
# if t < first element of current row- then look at previous row
# if t > last element of the current row, then look at the next row
# we do this because there's no way we could find target in the current row.
# after multiple iterations, we get THE ROW- do a normal Binary Search in this row 
# If we do not find the row, and condition breaks(top > bot), this means the target is not in the matrix
# so we return False- Eg- [[1], [3]], target = 4

# Time Complexity = O(logm + logn) ~ O(log(mn)) because first part will search m rows- O(logm), then we pick a row
# and search n columns of that row~ O(log(n)
# Space Complexity = O(1)
     
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2

            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        if not (top <= bot):
            return False
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2

            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True

        return False
      
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
