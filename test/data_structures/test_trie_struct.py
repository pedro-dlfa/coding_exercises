from src.data_structures.trie_struct import Trie


def test_trie__search():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    for word in ["the", "these", "their", "thaw", "anas"]:
        assert t.search(word) == (word in keys)


def test_trie__prefix_empty__matches_all_trie():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    assert set(t.words_with_prefix("")) == set(keys)


def test_trie__prefix_non_empty_existing__matches():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    prefix = "th"

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    assert set(t.words_with_prefix(prefix)) == set(
        key for key in keys if key.startswith(prefix)
    )


def test_trie__prefix_non_empty_non_existing__no_matches(faker):
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    assert t.words_with_prefix(faker.pystr()) == []
