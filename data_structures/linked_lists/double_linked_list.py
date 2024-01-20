from typing import Any


class DoublyLinkedList:
    class Node:
        def __init__(self, data: Any, prev=None) -> None:
            self.data = data
            self.next = None
            self.prev = prev

    def __init__(self, data) -> None:
        self.head = self.Node(data)
        self.tail = self.head
        self.size = 1

    def insert(self, data: Any) -> None:
        self.tail.next = self.Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.size += 1

    def insert_at(self, index: int, data: Any):
        it = self.head
        new_node = self.Node(data)
        for _ in range(index):
            it = it.next
        new_node.next = it
        new_node.prev = it.prev
        it.prev.next = new_node
        it.prev = new_node

    def delete(self, index: int) -> None:
        it = self.head
        for _ in range(index - 1):
            it = it.next
        it.prev.next = it.next
        it.next.prev = it.prev
        self.size -= 1

    def get(self, index: int) -> Any:
        if index > self.size:
            raise IndexError()
        it = self.head
        for _ in range(index):
            it = it.next
        return it.data

    def __len__(self) -> Any:
        return self.size

    def __str__(self) -> str:
        result = 'head -> '
        it = self.head
        while it is not None:
            result += f'{it.data} <-> '
            it = it.next
        result += 'None'
        return result
