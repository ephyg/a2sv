class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False

        def searchWord(row, col, idx):
            nonlocal ans
            if len(word) <= idx:
                ans = True
                return
            if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0:
                return
            if word[idx]!=board[row][col]:
                return
            if board[row][col] == " ":
                return
            
            x=board[row][col]
            board[row][col] = " "
            
            searchWord(row, col + 1, idx + 1)
            searchWord(row + 1, col, idx + 1)
            searchWord(row, col - 1, idx + 1)
            searchWord(row - 1, col, idx + 1)

            board[row][col] = x
        for r in range(len(board)):
            for c in range(len(board[0])):
                searchWord(r, c, 0)
        return ans
