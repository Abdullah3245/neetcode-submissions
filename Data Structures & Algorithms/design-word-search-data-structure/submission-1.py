class TrieNode:
    def __init__(self):
        self.childrens = [None] * 26
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for character in word:
            if curr.childrens[ord(character) - 97] is None:
                curr.childrens[ord(character) - 97] = TrieNode()
            curr = curr.childrens[ord(character) - 97]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        def dfs(index: int, curr_node: TrieNode) -> True:
            if curr_node is None:
                return False
            if index == len(word):
                return curr_node.is_word
            
            character = word[index]
            
            if character != '.':
                return dfs(index + 1, curr_node.childrens[ord(character) - ord('a')])
            else:
                # Try every possible path
                for node in curr_node.childrens:
                    if node and dfs(index + 1, node):
                        return True
                return False
        return dfs(0, curr_node)