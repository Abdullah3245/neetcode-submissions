class Node:
    def __init__(self):
        self.childrens = [None] * 26
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root_node = Node()

    def getIndex(self, character) -> int:
        return ord(character) - 97

    def insert(self, word: str) -> None:
        curr_node = self.root_node
        for character in word:
            if not curr_node.childrens[self.getIndex(character)]:
                curr_node.childrens[self.getIndex(character)] = Node()
            curr_node = curr_node.childrens[self.getIndex(character)]
        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root_node
        for character in word:
            if curr.childrens[self.getIndex(character)] is None:
                return False
            curr = curr.childrens[self.getIndex(character)]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root_node
        for character in prefix:
            if curr.childrens[self.getIndex(character)] is None:
                return False
            curr = curr.childrens[self.getIndex(character)]
        return True