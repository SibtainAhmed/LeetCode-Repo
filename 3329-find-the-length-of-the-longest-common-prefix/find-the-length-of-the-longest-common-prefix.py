class TrieNode():
    def __init__(self):
        self.children = {}
        # self.is_word = False

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = self.createTrie(arr1)
        ans = 0
        for num in arr2:
            temp = []
            while num:
                temp.append(num%10)
                num = num//10
            node = root
            cnt = 0
            for _ in range(len(temp)):
                value = temp.pop()
                if value not in node.children:
                    break
                node = node.children[value]
                cnt += 1
            ans = max(ans, cnt)
        return ans

    def createTrie(self, arr):
        root = TrieNode()
        for num in arr:
            temp = []
            while num:
                temp.append(num%10)
                num = num//10
            node = root
            for _ in range(len(temp)):
                value = temp.pop()
                if value not in node.children:
                    node.children[value] = TrieNode()
                node = node.children[value]
        return root

        