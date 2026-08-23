class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen=set()
        for r in range(9):
            for c in range(9):
                value=board[r][c]
                if value != ".":
                    a=("row",r,value)
                    b=("col",c,value)
                    box = ("box",r//3,c//3,value)
                    if a in seen or b in seen or box in seen:
                        return False
                    else:
                        seen.add(a)
                        seen.add(b)
                        seen.add(c)
        return True