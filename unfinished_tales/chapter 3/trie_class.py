class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        my_node = self.root

        for char in word:
            if char not in my_node.children:
                my_node.children[char] = TrieNode()
            my_node = my_node.children[char]

        my_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        my_node = self.root

        for char in word:
            if char not in my_node.children:
                return False
            my_node = my_node.children[char]

        return my_node.is_word

word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))

