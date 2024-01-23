from typing import Any, List, Optional, Union

from data_structs_and_alg.data_structures.linked_lists.singly_linked_list import SinglyLinkedList


class HashTable:
    class KeyValuePair:
        def __init__(self, key: Any, value: Any) -> None:
            self.key = key
            self.value = value

        def __eq__(self, __value: object) -> bool:
            return self.key == __value.key

        def __str__(self) -> str:
            return f'({self.key},{self.value})'

    def __init__(self, *data: Any, size: Optional[int] = 10) -> None:
        if size < 0:
            raise ValueError('Size of table cannot be negative')
        if (len(data) > 0) and (size == 0):
            raise ValueError('Size of table cannot be 0 if you want to insert data')
        self.table: List[SinglyLinkedList] = [SinglyLinkedList() for _ in range(size)]
        if data:
            for key, val in data:
                self.insert(key, val)

    def insert(self, key: Any, value: Any) -> None:
        key_value = self.KeyValuePair(key, value)
        index = self._get_index(self._hash_function(key))
        sll = self.table[index]
        it = sll.head
        if not it:
            sll.insert(key_value)
        else:
            while (it.data != key_value) and (it._next is not None):
                it = it._next
            if it.data == key_value:
                it.data.value = key_value.value
            else:
                sll.insert(key_value)

    def get(self, key: Any) -> Union[Any, None]:
        sll = self.table[self._get_index(self._hash_function(key))]
        if not sll:
            return None
        it = sll.head
        while (it.data.key != key) and (it._next is not None):
            it = it._next
        return it.data.value if it.data.key == key else None

    def delete(self, key: Any) -> None:
        index = self._get_index(self._hash_function(key))
        sll = self.table[index]
        it = sll.head
        if it is None:
            return
        elif it.data.key == key:
            self.table[index] = None
        else:
            while it._next is not None:
                if it._next.data.key != key:
                    it = it._next
                else:
                    it._next = it._next._next
                    return

    def _hash_function(self, key) -> int:
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
