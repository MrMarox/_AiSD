from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.value.append(self)



class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head: Node, tail: Node) -> None:
        self.head = head
        self.tail = tail

    def push(self, data) -> Any:
        self.head = LinkedList.head
        self.value.push(data)

    def append(self) -> Any:
        self.tail = LinkedList.tail
        self.value.append(self)




list_ = LinkedList(Node, Node)
print(list_)

list_.push(2)
