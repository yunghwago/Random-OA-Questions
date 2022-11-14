class TrieNode:
    def __init__(self):
        self.children = {} #key = letter itself, value = trienodes of other letters
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(index, currNode):
            curr = currNode
            for i in range(index, len(word)):
                if word[i] == ".": #move down automatically
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.endOfWord #all letters found but is it a word?
        return dfs(0, self.root)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
Console
