class TreeNode:
    def __init__(self) -> None:
        self.children = collections.defaultdict(TreeNode)
        self.is_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TreeNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        node = self.root
        return self.dfs(node, word, 0, 0)

    def dfs(self, node, word, index, count):
        ret = False
        if count > 1:
            return False
        if index == len(word):
            return count == 1 and node.is_word
        for c in node.children:
            if c != word[index]:
                ret |= self.dfs(node.children.get(c), word, index+1, count+1)
            else:
                ret |= self.dfs(node.children.get(c), word, index+1, count)             
        return ret

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