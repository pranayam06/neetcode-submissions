class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not cur.children[ord(char) - ord('a')]:
                cur.children[ord(char) - ord('a')] = TrieNode()
            cur = cur.children[ord(char) - ord('a')]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if not cur.children[ord(char)-ord('a')]:
                return False 
            else:
                cur = cur.children[ord(char) - ord('a')]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if not cur.children[ord(char)-ord('a')]:
                return False 
            else:
                cur = cur.children[ord(char) - ord('a')]
        return True