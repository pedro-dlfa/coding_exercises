from collections import defaultdict, deque


class Graph:
    """ BFS: Shortest Reach in a Graph

    Consider an undirected graph consisting of 'n' nodes where each node is labeled from '1' to 'n' and the edge
    between any two nodes is always of length '6'. We define node 's' to be the starting position for a BFS.
    Given a graph, determine the distances from the start node to each of its descendants and return the list
    in node number order, ascending. If a node is disconnected, its distance should be '-1'.

    Find more details on: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
    """

    def __init__(self, n):
        self.nodes_count = n
        self.nodes_dict = {}
        for i in range(n):
            self.nodes_dict[i] = set()

    def connect(self, x, y):
        self.nodes_dict[x].add(y)
        self.nodes_dict[y].add(x)

    def find_all_distances(self, start_node):
        q = deque()
        q.append((start_node, 0))
        weights = defaultdict(lambda: -1)
        weights[start_node] = 0

        # BFS with weights
        while len(q) > 0:
            node, weight = q.popleft()
            for child in self.nodes_dict[node]:
                if weights[child] == -1:
                    weights[child] = weight + 6
                    q.append((child, weight + 6))

        # Print answer
        distances = []
        for node in range(self.nodes_count):
            if start_node != node:
                distances.append(str(weights[node]))
        print(" ".join(distances))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
