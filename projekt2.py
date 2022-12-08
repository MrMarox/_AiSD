from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.right_child = None
        self.left_child = None

    def __str__(self) -> str:
        return str(self.value)

    def min(self) -> 'BinaryNode':
        if self.left_child is not None:
            return self.left_child.min()
        return self

    def is_leaf(self) -> bool:
        if self.left_child and self.right_child:
            return False
        return True

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, node: 'BinaryNode'):
        self.root = node

    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node.value > value:
            if node.left_child is None:
                node.left_child = BinaryNode(value)
            else:
                self._insert(node.left_child, value)
        else:
            if node.right_child is None:
                node.right_child = BinaryNode(value)
            else:
                self._insert(node.right_child, value)
        return node


tree = BinarySearchTree(BinaryNode(8))
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(10)
tree.insert(14)
tree.insert(13)





