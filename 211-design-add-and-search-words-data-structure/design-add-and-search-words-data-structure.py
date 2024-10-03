class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.head
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.head
        return self.recur(word, node)
        
    def recur(self, word, node):
        if not(word):
            return node.is_word
        # for w in word:
        w = word[0]
        word = word[1:]
        if w == '.':
            res = False
            for k in node.children.keys():
                res |= self.recur(word, node.children[k])
            return res
        else:
            if w not in node.children:
                return False
            node = node.children[w]
        return self.recur(word,node)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)