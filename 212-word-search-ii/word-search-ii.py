class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None
class Solution:
    def makeTrie(self, arr):
        rootTemp = TrieNode()
        # print(rootTemp.isWord, 'not None')
        for word in arr:
            node = rootTemp
            for w in word:
                if w not in node.children:
                    node.children[w] = TrieNode()
                # node.children[w].value += 1
                node = node.children[w]
            node.isWord = True
            node.word = word
        return rootTemp

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.makeTrie(words)
        res = []
        m, n = len(board)-1, len(board[0])-1
        def dfs(r,c, node):
            temp = []
            if node.isWord:
                node.isWord = False
                res.append(node.word)
            temp.append(board[r][c])
            board[r][c] = '#'
            if r < m and board[r+1][c] in node.children:
                dfs(r+1,c,node.children[board[r+1][c]])
            if c < n and board[r][c+1] in node.children:
                dfs(r,c+1,node.children[board[r][c+1]])
            if r > 0 and board[r-1][c] in node.children:
                dfs(r-1,c,node.children[board[r-1][c]])
            if c>0 and board[r][c-1] in node.children:
                dfs(r,c-1,node.children[board[r][c-1]])
            board[r][c] = temp.pop()
        for r in range(m+1):
            for c in range(n+1):
                if board[r][c] in root.children:
                    print(r, c)
                    dfs(r,c, root.children[board[r][c]])
        return res
