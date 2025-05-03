class Node:
    """Represents a node in a graph."""
    def __init__(self, name):
        """Assumes name is a string."""
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge:
    """Represents a directed edge in a graph."""
    def __init__(self, src, dest):
        """Assumes src and dest are nodes."""
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.src.get_name() + '->' + self.dest.get_name()


class Digraph:
    """Edges is a dict mapping each node to a list of its children."""
    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.edges

    def get_node(self, name):
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.get_name() + '->' + dest.get_name() + '\n'
        return result[:-1] if result else ''


class Graph(Digraph):
    """Represents an undirected graph."""
    def add_edge(self, edge):
        super().add_edge(edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        super().add_edge(rev)


class CityPlanner:
    def __init__(self):
        self.print_queue = True
        self.g = None

    def print_path(self, path):
        """Assumes path is a list of nodes."""
        result = ''
        for i, node in enumerate(path):
            result += str(node)
            if i != len(path) - 1:
                result += '->'
        return result

    def DFS(self, graph, start, end, path, shortest, to_print=False):
        """Assumes graph is a Digraph; start and end are nodes;
           path and shortest are lists of nodes.
           Returns a shortest path from start to end in graph."""
        if not graph.has_node(start) or not graph.has_node(end):
            return None
        path = path + [start]
        if to_print:
            print('Current DFS path:', self.print_path(path))
        if start == end:
            return path
        for node in graph.children_of(start):
            if node not in path:
                if shortest is None or len(path) < len(shortest):
                    new_path = self.DFS(graph, node, end, path, shortest, to_print)
                    if new_path is not None:
                        shortest = new_path
            elif to_print:
                print('Already visited', node)
        return shortest

    def BFS(self, graph, start, end, to_print=False):
        """Assumes graph is a Digraph; start and end are nodes.
           Returns a shortest path from start to end in graph."""
        if not graph.has_node(start) or not graph.has_node(end):
            return None
        init_path = [start]
        path_queue = [init_path]
        while path_queue:
            if to_print:
                print('Queue:', len(path_queue))
                for p in path_queue:
                    print(self.print_path(p))
            tmp_path = path_queue.pop(0)
            if to_print:
                print('Current BFS path:', self.print_path(tmp_path))
                print()
            last_node = tmp_path[-1]
            if last_node == end:
                return tmp_path
            for next_node in graph.children_of(last_node):
                if next_node not in tmp_path:
                    new_path = tmp_path + [next_node]
                    path_queue.append(new_path)
        return None

    def shortest_path_dfs(self, graph, start, end, toPrint=False):
        """Returns shortest path using DFS."""
        return self.DFS(graph, start, end, [], None, toPrint)

    def shortest_path_bfs(self, graph, start, end, toPrint=False):
        """Returns shortest path using BFS."""
        return self.BFS(graph, start, end, toPrint)

    def get_shortest_path(self, source, destination, method='dfs'):
        """Prints the shortest path from source to destination."""
        if not self.g or not isinstance(self.g, Digraph):
            return
        if method == 'bfs':
            sp = self.shortest_path_bfs(self.g, self.g.get_node(source), self.g.get_node(destination), True)
        else:
            sp = self.shortest_path_dfs(self.g, self.g.get_node(source), self.g.get_node(destination), True)
        if sp is not None:
            print('Shortest path from', source, 'to', destination, 'is', self.print_path(sp))
        else:
            print(f'There is no path from {source} to {destination}')

# Module-level functions for tests

def printPath(path):
    """Assumes path is a list of nodes."""
    result = ''
    for i, node in enumerate(path):
        result += str(node)
        if i != len(path) - 1:
            result += '->'
    return result


def BFS(graph, start, end, toPrint=False):
    """Module-level BFS"""
    cp = CityPlanner()
    return cp.BFS(graph, start, end, toPrint)


def shortestPath(graph, start, end, toPrint=False):
    """Module-level shortest path (DFS)"""
    cp = CityPlanner()
    return cp.shortest_path_dfs(graph, start, end, toPrint)