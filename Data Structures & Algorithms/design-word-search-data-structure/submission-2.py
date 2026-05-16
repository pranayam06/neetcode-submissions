class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True 

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for let in range(26):
                        if cur and dfs(i+1, cur.children[let]):
                            return True
                    return False
                else: 
                    if not cur: 
                        return False
                    cur = cur.children[ord(c) - ord('a')]
            return cur and cur.endOfWord
        return dfs(0, self.root)
