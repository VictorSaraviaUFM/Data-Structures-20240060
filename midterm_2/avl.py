# Espacio para inciso 2.1

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

    def __repr__(self):
        return f"({self.data})"

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))

    def get_balance(self, node):
        return self.get_height(node.left_child) - self.get_height(node.right_child) if node else 0

    def rotate_right(self, y):
        x = y.left_child
        T2 = x.right_child
        x.right_child = y
        y.left_child = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right_child
        T2 = y.left_child
        y.left_child = x
        x.right_child = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.data:
            node.left_child = self._insert(node.left_child, key)
        elif key > node.data:
            node.right_child = self._insert(node.right_child, key)
        else:
            return node  # duplicados no permitidos

        self.update_height(node)
        balance = self.get_balance(node)

        # Rotaciones
        if balance > 1 and key < node.left_child.data:
            return self.rotate_right(node)
        if balance < -1 and key > node.right_child.data:
            return self.rotate_left(node)
        if balance > 1 and key > node.left_child.data:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        if balance < -1 and key < node.right_child.data:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.data:
            return True
        elif key < node.data:
            return self._search(node.left_child, key)
        else:
            return self._search(node.right_child, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root
        elif key < root.data:
            root.left_child = self._delete(root.left_child, key)
        elif key > root.data:
            root.right_child = self._delete(root.right_child, key)
        else:
            if root.left_child is None:
                return root.right_child
            elif root.right_child is None:
                return root.left_child
            temp = self.get_min_value_node(root.right_child)
            root.data = temp.data
            root.right_child = self._delete(root.right_child, temp.data)

        self.update_height(root)
        balance = self.get_balance(root)

        # Rebalanceo
        if balance > 1 and self.get_balance(root.left_child) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left_child) < 0:
            root.left_child = self.rotate_left(root.left_child)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right_child) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right_child) > 0:
            root.right_child = self.rotate_right(root.right_child)
            return self.rotate_left(root)

        return root

    def get_min_value_node(self, node):
        if node is None or node.left_child is None:
            return node
        return self.get_min_value_node(node.left_child)

    def print_pretty(self):
        if self.root is not None:
            lines, *_ = self._build_tree_string(self.root)
            print("\n" + "\n".join(line.rstrip() for line in lines))
        else:
            print("\nEmpty tree...")

    def _build_tree_string(self, node):
        if node.right_child is None and node.left_child is None:
            line = str(node.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right_child is None:
            lines, n, p, x = self._build_tree_string(node.left_child)
            s = str(node.data)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left_child is None:
            lines, n, p, x = self._build_tree_string(node.right_child)
            s = str(node.data)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._build_tree_string(node.left_child)
        right, m, q, y = self._build_tree_string(node.right_child)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
