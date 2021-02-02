# https://www.techiedelight.com/chess-knight-problem-find-shortest-path-source-destination/
# Find the shortest distance for a chess knight from source to destination

from collections import deque


class Node:
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)

    # As we are using Node as a key in a dictionary (by checking for 'node in set')
    # we need to implement hashCode() and equals()
    def __hash__(self):
        return hash((self.x, self.y, self.dist))


class ShortestDistance:
    def __init__(self, src, dest, N):
        self.src = src
        self.dest = dest
        self.N = N
        # Define possible relative moves for a knight, starting at row = 0, col = 0
        self.rows = [2, 2, -2, -2, 1, 1, -1, -1]
        self.cols = [-1, 1, 1, -1, 2, -2, 2, -2]

    def isValid(self, x, y):
        return 0 <= x <= self.N and 0 <= y <= self.N

    def bfs(self):
        visited = set()
        queue = deque()

        queue.append(self.src)

        while queue:
            node = queue.popleft()

            if node.x == self.dest.x and node.y == self.dest.y:
                return node.dist

            if node not in visited:
                visited.add(node)

            for i in range(len(self.rows)):
                x = node.x + self.rows[i]
                y = node.y + self.cols[i]
                dist = node.dist + 1
                if self.isValid(x, y):
                    queue.append(Node(x, y, dist))

        return float('inf')


if __name__ == "__main__":
    source = Node(0, 7)
    destination = Node(7, 0)
    s = ShortestDistance(source, destination, 8)
    print("Min steps between src and dest are ", s.bfs())