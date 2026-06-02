class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        possible_words = set()
        self.visited = []

        def backtrack(i, j, curr):
            if len(curr) == len(word):
                possible_words.add(curr)
                return 
            
            if i > 0 and (i-1, j) not in self.visited:
                self.visited.append((i-1, j))
                backtrack(i-1, j, curr + board[i-1][j])
                self.visited.pop()
            
            if i < len(board) - 1 and (i+1, j) not in self.visited:
                self.visited.append((i+1, j))
                backtrack(i+1, j, curr +  board[i+1][j])
                self.visited.pop()
            
            if j > 0 and (i, j-1) not in self.visited:
                self.visited.append((i, j-1))
                backtrack(i, j-1, curr + board[i][j-1])
                self.visited.pop()
            
            if j < len(board[0]) - 1 and (i, j+1) not in self.visited:
                self.visited.append((i, j+1))
                backtrack(i, j+1, curr + board[i][j+1])
                self.visited.pop()

        for i, row in enumerate(board):
            for j, character in enumerate(row):
                if character == word[0]:
                    self.visited.append((i, j))
                    backtrack(i, j, character)
                    self.visited.pop()
        
        return word in possible_words