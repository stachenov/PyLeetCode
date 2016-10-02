from itertools import product
from timeit import timeit


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        # original idea by @lixx2100, Fibonacci Heap implementation mine

        class FibonacciNode:
            def __init__(self, value):
                self.value = value
                self.next = self.prev = self
                self.child = self.parent = None
                self.marked = False
                self.degree = 0

            def append(self, next):
                old_next = self.next
                self.next = next
                next.next = old_next
                next.prev = self
                old_next.prev = next

            def add_child(self, child):
                if not self.child:
                    self.child = child
                    child.next = child.prev = child
                else:
                    self.child.append(child)
                child.parent = self
                self.degree += 1

            def remove_child(self, child):
                if child.prev is child:
                    self.child = None
                else:
                    child.next.prev = child.prev
                    child.prev.next = child.next
                    if self.child is child:
                        self.child = child.next
                    child.prev = child.next = child
                child.parent = None
                self.degree -= 1

            def dump(self, indent):
                assert self.value not in dumped
                dumped.add(self.value)
                print ' ' * indent, self.value, self.degree
                if self.child:
                    node = self.child
                    while True:
                        node.dump(indent + 4)
                        node = node.next
                        if node is self.child:
                            break

        class NodesByDegree:
            def __init__(self):
                self.nodes = {}

            def insert(self, node):
                if node.degree not in self.nodes:
                    self.nodes[node.degree] = node
                else:
                    old_node = self.nodes[node.degree]
                    del self.nodes[node.degree]
                    if old_node.value <= node.value:
                        new_node = old_node
                        new_node.add_child(node)
                    else:
                        new_node = node
                        node.add_child(old_node)
                    self.insert(new_node)

            def __iter__(self):
                return self.nodes.itervalues()

        class FibonacciHeap:

            def __init__(self):
                self.head = None

            def __nonzero__(self):
                return bool(self.head)

            def insert(self, value):
                node = FibonacciNode(value)
                if self.head:
                    self.head.append(node)
                    if node.value < self.head.value:
                        self.head = node
                else:
                    self.head = node
                return node

            def peek(self):
                return self.head

            def pop(self):
                roots = NodesByDegree()
                count = 0
                # insert roots except head (min)
                node = self.head.next
                while node is not self.head:
                    next = node.next
                    count += 1
                    roots.insert(node)
                    node = next
                if self.head.child:
                    # insert head's children
                    node = self.head.child
                    while True:
                        next = node.next
                        count += 1
                        roots.insert(node)
                        node = next
                        if node is self.head.child:
                            break
                node = self.head
                # link the new roots back into a linked list
                self.head = None
                for root in roots:
                    self.append_root(root)
                if count > 30:
                    print count
                return node

            def append_root(self, root):
                root.parent = None
                root.marked = False
                if not self.head:
                    self.head = root
                    root.next = root.prev = root
                else:
                    self.head.append(root)
                    if root.value < self.head.value:
                        self.head = root

            def decrease(self, node, value):
                node.value = value
                if not node.parent:
                    if node.value < self.head.value:
                        self.head = node
                elif node.value < node.parent.value:
                    self.mark_or_cut(node.parent)
                    node.parent.remove_child(node)
                    self.append_root(node)

            def mark_or_cut(self, node):
                if node.marked:
                    if node.parent:
                        self.mark_or_cut(node.parent)
                        node.parent.remove_child(node)
                    self.append_root(node)
                elif node.parent:
                    node.marked = True

            def dump(self):
                dumped.clear()
                node = self.head
                while True:
                    node.dump(0)
                    node = node.next
                    if node is self.head:
                        break

        dumped = set()
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0

        def within(i, j):
            return 0 <= i < m and 0 <= j < n

        m, n = len(heightMap), len(heightMap[0])
        nearby = ((0, -1), (0, +1), (-1, 0), (+1, 0))
        fh = FibonacciHeap()
        level = [[None] * n for __ in xrange(m)]
        # the starting virtual "node" is the outside world
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    value = heightMap[i][j], i, j
                else:
                    value = float('+inf'), i, j
                level[i][j] = fh.insert(value)
        while fh:
            h, i, j = fh.pop().value
            for di, dj in nearby:
                if within(i + di, j + dj):
                    new_high = max(h, heightMap[i + di][j + dj])
                    if new_high < level[i + di][j + dj].value[0]:
                        fh.decrease(level[i + di][j + dj], (new_high, i + di, j + dj))
        return sum(level[i][j].value[0] - heightMap[i][j]
                   for i, j in product(xrange(m), xrange(n)))
