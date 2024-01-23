from typing import Any, Union


class SinglyLinkedList:
    class Node:
        def __init__(self, data: Any, _next=None) -> None:
            self.data = data
            self._next = _next

        def __eq__(self, other) -> bool:
            return self.data == other.data

    def __init__(self, *data) -> None:
        if data:
            self.head = self.Node(data[0])
            self.size = 1
            it = self.head
            for i in range(1, len(data)):
                it._next = self.Node(data[i])
                it = it._next
                self.size += 1
            self.tail = it

        else:
            self.head = None
            self.tail = None
            self.size = 0

    def insert(self, data: Any) -> None:
        if not self.size:
            self.head = self.Node(data)
            self.tail = self.head
        else:
            self.tail._next = self.Node(data)
            self.tail = self.tail._next
        self.size += 1

    def insert_at(self, data: Any, index: int) -> None:
        # TODO: make more concise
        if (self.size == 0) and (index == 0):
            self.head = self.Node(data)
            self.tail = self.head
        elif index == self.size - 1:
            self.tail._next = self.Node(data)
            self.tail = self.tail._next
        elif index == 0:
            tmp = self.Node(data, self.head)
            self.head = tmp
        elif index > self.size - 1:
            raise IndexError('List index out of range')
        else:
            it = self.head
            for _ in range(index - 1):
                it = it._next
            tmp = self.Node(data, it._next)
            it._next = tmp
        self.size += 1

    def delete(self, index: int) -> None:
        if index > self.size - 1:
            raise IndexError('List index out of range')
        elif index == 0:
            self.head = self.head._next
        else:
            it = self.head
            for _ in range(index - 1):
                it = it._next
            it._next = it._next._next
        self.size -= 1

    def get(self, index: int) -> Any:
        if index > self.size - 1:
            raise IndexError()
        it = self.head
        for _ in range(index):
            it = it._next
        return it.data

    def get_value(self, value: Any) -> Union[Any, None]:
        it = self.head
        while (it.data != value) and (it._next is not None):
            it = it._next
        return it.data if it.data == value else None

    def __len__(self) -> Any:
        return self.size

    def __str__(self) -> str:
        result = 'head -> '
        it = self.head
        while it is not None:
            result += f'{it.data} -> '
            it = it._next
        result += 'None'
        return result
