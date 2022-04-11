class TrieNode:
    def __init__(self):
        self.isend = False
        self.children = [None] * 26

    def insert(self, s):
        if s == None:
            return
        node = self
        for c in s:
            i = ord(c) - ord('a')
            if node.children[i] == None:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isend = True


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        words.sort(key=len)
        root = TrieNode()

        def check(node, word, index):
            if index == len(word):
                return True
            n = len(word)
            for i in range(index, n):
                j = ord(word[i]) - ord('a')
                if node.children[j] != None:
                    node = node.children[j]
                else:
                    return False
                if node.isend and check(root, word, i + 1):
                    return True
            return False

        for word in words:
            if len(word) == 0:
                continue
            if check(root, word, 0):
                res.append(word)
            else:
                root.insert(word)
        return res