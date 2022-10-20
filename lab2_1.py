class Node:
    value: any
    next_: 'Node'

    def __init__(self, value: any) -> None:
        self.value = value
        self.next_ = None


class LinkedList:
    head: Node
    tail: Node

    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def push(self, value: any) -> None:
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next_ = self.head
            self.head = node