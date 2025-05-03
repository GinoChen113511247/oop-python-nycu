import pytest
from lecture3_graph import CityPlanner, Digraph, Node, Edge
from lecture3_graph import shortestPath, BFS, printPath
from lecture3_graph import Graph

# Fixture 定義城市圖，供多個測試重用
@pytest.fixture
def city_graph():
    g = Digraph()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):
        g.add_node(Node(name))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('Providence')))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('Boston')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('New York'), g.get_node('Chicago')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Denver')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))
    return g


def test_shortest_path_dfs(city_graph):
    # Chicago -> Boston 有向圖中無法到達，應回 None
    sp = shortestPath(city_graph,
                      city_graph.get_node('Chicago'),
                      city_graph.get_node('Boston'))
    assert sp is None

    # Boston -> Phoenix 經由最短路徑 New York -> Chicago -> Phoenix
    sp = shortestPath(city_graph,
                      city_graph.get_node('Boston'),
                      city_graph.get_node('Phoenix'))
    assert printPath(sp) == 'Boston->New York->Chicago->Phoenix'


def test_shortest_path_bfs(city_graph):
    # BFS 查找最近鄰連結
    sp = BFS(city_graph,
             city_graph.get_node('Chicago'),
             city_graph.get_node('Phoenix'), False)
    assert printPath(sp) == 'Chicago->Phoenix'

    sp = BFS(city_graph,
             city_graph.get_node('Boston'),
             city_graph.get_node('Phoenix'), False)
    assert printPath(sp) == 'Boston->New York->Chicago->Phoenix'


def test_city_planner_shortest_path_dfs(city_graph):
    cp = CityPlanner()
    cp.g = city_graph
    # Chicago->Boston 無路徑
    sp = cp.shortest_path_dfs(city_graph,
                               city_graph.get_node('Chicago'),
                               city_graph.get_node('Boston'))
    assert sp is None
    # Boston->Phoenix 預期最短路徑
    sp = cp.shortest_path_dfs(city_graph,
                               city_graph.get_node('Boston'),
                               city_graph.get_node('Phoenix'))
    assert cp.print_path(sp) == 'Boston->New York->Chicago->Phoenix'


def test_city_planner_shortest_path_bfs(city_graph):
    cp = CityPlanner()
    cp.g = city_graph
    sp = cp.shortest_path_bfs(city_graph,
                               city_graph.get_node('Chicago'),
                               city_graph.get_node('Phoenix'))
    assert cp.print_path(sp) == 'Chicago->Phoenix'
    sp = cp.shortest_path_bfs(city_graph,
                               city_graph.get_node('Boston'),
                               city_graph.get_node('Phoenix'))
    assert cp.print_path(sp) == 'Boston->New York->Chicago->Phoenix'


def test_city_planner_get_shortest_path(capsys, city_graph):
    cp = CityPlanner()
    cp.g = city_graph
    cp.get_shortest_path('Chicago', 'Boston')
    captured = capsys.readouterr()
    assert 'There is no path from Chicago to Boston' in captured.out
    cp.get_shortest_path('Boston', 'Phoenix')
    captured = capsys.readouterr()
    assert 'Shortest path from Boston to Phoenix is Boston->New York->Chicago->Phoenix' in captured.out


def test_city_planner_empty_graph():
    cp = CityPlanner()
    cp.g = Digraph()
    sp = cp.shortest_path_dfs(cp.g, Node('A'), Node('B'))
    assert sp is None


def test_city_planner_print_path():
    cp = CityPlanner()
    path = [Node('A'), Node('B'), Node('C')]
    assert cp.print_path(path) == 'A->B->C'
    assert cp.print_path([Node('X')]) == 'X'