class TreeNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TreeNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        node = self.root
        return self.dfs(node, word, 0, 0)

    def dfs(self, node, word, index, count):
        if index == len(word):
            return True if count == 1 and node.is_word else False
        for c in node.children:
            if c == word[index]:
                if self.dfs(node.children.get(c), word, index+1, count):
                    return True
            elif c != word[index] and count == 0:
                if self.dfs(node.children.get(c), word, index+1, count+1):
                    return True           
        return False

class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        if self.trie.search(searchWord):
            return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)