from typing import List, Optional


class TrieNode:
    """Trie node class

    Includes:
      * a dictionary with children nodes
      * a flag to determine whether the node indicates end of word or not
    """

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """Trie class

    Implements 'Trie' tree.
    Supported operations are:
      - insert: Inserts a word in the Trie
      - search: Indicates whether a word exists in the Trie or not
      - words_with_prefix: Finds all words that starts by a given prefix
    """

    def __init__(self):
        self.root = self.__get_node()

    @staticmethod
    def __get_node():
        return TrieNode()

    def insert(self, word) -> None:
        """
        Inserts a word in the trie if not present.
        In case the word is prefix of another word, the last node of the word will simply be marked as leaf node
        """
        current_node = self.root
        for char in word:
            child = current_node.children.get(char)
            if not child:
                # If not exists: create child
                child = self.__get_node()
                current_node.children[char] = child
            current_node = child

        # Mark as leaf node
        current_node.is_end = True

    def words_with_prefix(self, prefix: str) -> List[str]:
        """
        Returns all words in the trie starting by a given prefix
        """
        results: List[str] = []
        node = self.__get_node_by_prefix(prefix)
        self.__collect_children(node, prefix, results)
        return results

    @staticmethod
    def __collect_children(
        node: Optional[TrieNode], prefix: str, results: List[str]
    ) -> None:
        """
        Traverses the trie to find all the nodes starting by a given prefix.
        As a result, all words starting by a given prefix will be returned
        """
        if node is None:
            return
        if node.is_end:
            results.append(prefix)
        for char, child_node in node.children.items():
            Trie.__collect_children(child_node, prefix + char, results)

    def search(self, word) -> bool:
        """
        Indicates whether a given word exists in the trie or not.
        """
        node = self.__get_node_by_prefix(word)
        return node is not None and node.is_end

    def __get_node_by_prefix(self, prefix) -> Optional[TrieNode]:
        """
        Finds a node in the trie matching with a given prefix.
        Returns the node matching with the prefix, or None if the prefix does not exist in the trie
        """
        current_node = self.root
        for char in prefix:
            child = current_node.children.get(char)
            if not child:
                return None
            current_node = child

        return current_node
