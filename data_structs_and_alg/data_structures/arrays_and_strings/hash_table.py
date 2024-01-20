from typing import Any, List

from data_structs_and_alg.data_structures.linked_lists.singly_linked_list import SinglyLinkedList


class HashTable:
    def __init__(self, *data: Any) -> None:
        self.table: List[SinglyLinkedList] = []
        if data:
            for key, val in data:
                self.insert(key, val)

    def insert(self, key, value):
        index = self._get_index(self._hash_function(key))
        try:
            sll = self.table[index]
            sll.insert(value)
        except IndexError:
            self.table.append(SinglyLinkedList(value))

    def _hash_function(self, key):
        return hash(key)

    def _get_index(self, hash_value: int) -> int:
        if len(self.table) == 0:
            return 0
        index = hash_value % len(self.table)  # noqa: S001
        return index

    def __str__(self) -> str:
        res = ''
        for i in range(len(self.table)):
            res += f'{i} -> {self.table[i]}\n'
        return res
