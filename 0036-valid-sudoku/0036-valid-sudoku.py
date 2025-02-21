class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N=9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        for r in range(N):
            for c in range(N):
                val=board[r][c]
                if val == ".":
                    continue
                #check if an element is present only once in a row 
                if val in rows[r]:
                    return False
                rows[r].add(val)
                #check if an element is present only once in a column 
                if val in cols[c]:
                    return False
                cols[c].add(val)
                #check if an element is present only once in a box 
                index = (r//3)*3+(c//3)
                if val in boxes[index]:
                    return False 
                boxes[index].add(val)
        return True

        