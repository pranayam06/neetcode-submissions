class TrieNode:
    def __init__(self):
        self.children = [None for _ in range (26)]
        self.word = False 

class WordDictionary:

    def __init__(self):  
        self.root = TrieNode()

    def addWord(self, word: str) -> None: 
        node = self.root
        for char in word: 
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word = True  

    def search(self, word: str) -> bool: 
        def helper(j, node):
            cur = node
            for i in range(j, len(word)): 
                if word[i] == ".":
                    for ch in range(26):
                        if cur.children[ch] and helper(i+1, cur.children[ch]):  # ✅ only recurse if child exists
                            return True 
                    return False
                else:
                    if not cur.children[ord(word[i]) - ord('a')]:
                        return False 
                    cur = cur.children[ord(word[i]) - ord('a')]
            return cur.word
        
        return helper(0, self.root)
                                
        
        
