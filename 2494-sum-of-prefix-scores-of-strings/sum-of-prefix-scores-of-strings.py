class TrieNode():
    def __init__(self):
        self.children = {}
        self.value = 0

class Solution:
    def makeTrie(self, arr):
        root = TrieNode()
        for word in arr:
            node = root
            for w in word:
                if w not in node.children:
                    node.children[w] = TrieNode()
                node.children[w].value += 1
                node = node.children[w]
        return root
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = self.makeTrie(words)
        res = [0]*len(words)
        for i,word in enumerate(words):
            node = root
            for w in word:
                res[i] += node.children[w].value
                node = node.children[w]
        return res