
from collections import deque


with open('day-19/input/part-1.txt') as f:
    cur_patterns, desired_patterns = f.read().split('\n\n')
    cur_patterns = cur_patterns.split(', ')
    desired_patterns = desired_patterns.split('\n')


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def dfs(self, node, pre):
        if node.is_end:
            self.output.append((pre + node.char))
        for child in node.children.values():
            self.dfs(child, pre + node.char)

    def search(self, x):
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.output = []
        self.dfs(node, x[:-1])
        return self.output


trie = Trie()
for pattern in cur_patterns:
    trie.insert(pattern)


def is_valid(d_pattern):
    if len(d_pattern) == 0:
        return True

    pos = trie.search(d_pattern[0])
    return any(
        is_valid(d_pattern[len(p):])
        for p in pos
        if d_pattern.startswith(p)
    )


s = sum(
    is_valid(pattern)
    for pattern in desired_patterns
)
print(s)
