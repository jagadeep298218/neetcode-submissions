class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check(line):
            seen = set()
            for i in line:
                if i == ".":
                    continue
                elif int(i) in seen:
                    return False
                else:
                    seen.add(int(i))
            
            return True
        

        l1, l2, l3 = [], [], []

        for i in range(9):
            if len(l1) == 9:
                if not check(l1) or not check(l2) or not check(l3):
                    return False
                l1, l2, l3 = [], [], []
            for j in range(9):
                if j < 3:
                    l1.append(board[i][j])
                elif j < 6:
                    l2.append(board[i][j])
                else: 
                    l3.append(board[i][j])
        
        for i in range(9):
            if not check(board[i]):
                return False
        
        l = []
        for i in range(9):
            for j in range(9):
                l.append(board[j][i])
            if not check(l):
                return False
            l = []
        return True

