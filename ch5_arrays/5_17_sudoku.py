# check a 9x9 matrix and see if it is a valid sudoku solution
# 3x3 is unique 1-9, row 1-9, column 1-9, diagonal doesnt amtter
def valid_sudoku(G: [[int]]):
    # need coordinates of beginning 3x3, row and column should be easy
    def valid_row(n):
        nums = set(range(1,10))
        for num in G[n]:
            if num in nums:
                nums.remove(num)
            else:
                return False
        return True
    def valid_col(n):
        nums = set(range(1,10))
        for i in range(9):
            if G[i][n] in nums:
                nums.remove(G[i][n])
            else:
                return False
        return True

    def valid_sq(i):
        r = i // 3 * 3
        c = i % 3 * 3
        nums = set(range(1,10))
        for i in range(3):
            for j in range(3):
                if G[r+i][c+j] in nums:
                    nums.remove(G[r+i][c+j])
                else:
                    return False
        return True

    for i in range(9):
        if not valid_col(i) or not valid_row(i) or not valid_sq(i):
            return False
    return True

    # square begins at 0,0, 0,3, 0,6, 3,0, 3,3 3,6 6,0 6,3 6,6

S = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
    ]
print(valid_sudoku(S))