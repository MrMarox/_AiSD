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

class BinaryTree:
    root: BinaryNode

    def __init__(self, node: 'BinaryNode') -> None:
        self.root = node

    def __str__(self) -> str:
        return str(self.root.value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.root.left_child:
            self.root.left_child.traverse_post_order(visit)
        if self.root.right_child:
            self.root.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.root.left_child:
            self.root.left_child.traverse_pre_order(visit)
        if self.root.right_child:
            self.root.right_child.traverse_pre_order(visit)




korzen = BinaryNode(10)
korzen.add_left_child(9)
korzen.left_child.add_left_child(1)
korzen.left_child.add_right_child(3)

korzen.add_right_child(2)
korzen.right_child.add_left_child(4)
korzen.right_child.add_right_child(6)

# korzen.traverse_pre_order(print)

root = BinaryTree(korzen)

root.traverse_in_order(print)


