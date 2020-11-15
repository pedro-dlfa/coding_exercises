import string
import random
import logging

log = logging.getLogger("HashTable")
log.level = logging.DEBUG


class HashTable:
    """Class to implement custom HashTable/Dictionary functionality

    This implementation uses chain hashing to avoid collisions.
    I.e: it keeps in each cell of the HashTable a list of elements
    that have the same hash value.
    """

    __fill_factor = 2 / 3

    def __init__(self, size: int = 10):
        """
        Initializes the HashTable object
        :param size: (int) Initial size of the HashTable
        """
        self.__initialize_table(size)

    def __initialize_table(self, size):
        """
        Initialize the storage table
        :param size: Size of the storage table
        """
        self.__table = [None] * size
        self.__elements = 0

    def __resize(self):
        """
        Doubles the size of the HashTable
        :return:
        """
        # Keep old storage table and initialize a new one with double size
        old_table = self.__table
        self.__initialize_table(len(old_table) * 2)

        # Copy existing elements
        for e_list in old_table:
            # Skip empty positions
            if not e_list:
                continue
            # Copy inner chain of non-empty positions
            for e in e_list:
                self.add(e[0], e[1])

    def __get_key_position(self, key):
        """
        Computes the position of the key in the storage table
        :param key: (object) Input object key
        :return: (int) Position of the key in the storage table
        """
        return hash(key) % len(self.__table)

    def __setitem__(self, key, value):
        """
        Stores a key-value pair in the HashTable using the brackets notation.
        Example: hastTable[key] = value
        :param key: (object) Key object
        :param value: (object) Value object
        """
        self.add(key, value)

    def add(self, key, value):
        """
        Stores a key-value pair in the HashTable
        :param key: (object) Key object
        :param value: (object) Value object
        """
        position = self.__get_key_position(key)

        if not self.__table[position]:
            # If the index is empty: initialize a list with the new keyValuePair
            # It will support collisions
            self.__table[position] = [(key, value)]
            self.__elements += 1
        else:
            # If not empty: find if the key in list, and update if exists
            for index, elem in enumerate(self.__table[position]):
                if elem[0] == key:
                    self.__table[position][index] = (key, value)
                    break
            else:
                # Key not found in keyValuePair list -> add element
                self.__table[position].append((key, value))
                self.__elements += 1

        if self.__elements > (len(self.__table)) * self.__fill_factor:
            log.debug("HashTable is pretty filled. Resizing...")
            self.__resize()
            log.debug(f"New HashTable size is: {len(self.__table)}")

    def __getitem__(self, key):
        """
        Gets the value associated to a given item in the HashTable
        Throws "KeyError" if the key is not in the HashTable
        :param key: (object) Key object
        :return: (object) Value associated to the key in the HashTable
        """
        kvp = self.__get(key)
        if kvp:
            return kvp[1]
        raise KeyError(key)

    def get(self, key, default_value=None):
        """
        Gets the value associated to a given item in the HashTable
        Throws "KeyError" if the key is not in the HashTable
        :param key: (object) Key object
        :param default_value: Value returned when the key is not in the HashTable
        :return: (object) Value associated to the key in the HashTable, or "default_value"
        """
        kvp = self.__get(key)
        return kvp[1] if kvp else default_value

    def __get(self, key):
        """
        Gets the value associated to a given item in the HashTable
        Throws "KeyError" if the key is not in the HashTable
        :param key: (object) Key object
        :return: (tuple) KeyValuePair associated to the key in the HashTable, None if not found
        """
        position = self.__get_key_position(key)

        if self.__table[position]:
            for kvp in self.__table[position]:
                if kvp[0] == key:
                    return kvp

        return None

    def __contains__(self, key):
        """
        Checks whether a given key exists in the HashTable or not.
        :param key: (object) Key object
        :return: True if the key is in the HashTable, False otherwise.
        """
        return self.__get(key) is not None

    def __delitem__(self, key):
        """
        Removes a key-value pair from the HashTable given its key using the notation "del"
        :param key: (object) Key object
        """
        self.remove(key)

    def remove(self, key):
        """
        Removes a key-value pair from the HashTable given its key using the notation.
        Throws "KeyError" if the key is not in the HashTable
        :param key: (object) Key object
        """
        position = self.__get_key_position(key)

        if self.__table[position]:
            for index, elem in enumerate(self.__table[position]):
                if elem[0] == key:
                    del self.__table[position][index]
                    self.__elements -= 1
                    return

        raise KeyError(key)


keys = [
    "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
    for _ in range(1000)
]
# log_mock = mocker.patch.object(hashtable_struct.log, "debug")
sut = HashTable()
for k in keys:
    sut.add(k, str(k))

for k in keys:
    val = sut[k]
    assert val == str(k)
