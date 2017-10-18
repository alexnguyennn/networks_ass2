import pytest

def test_path_to_edge_tuples(graph, graph_topology, graph_topology_simple):
    result_path = ['a', 'c', 'd', 'g', 'i']
    assert graph.path_list_to_edges(result_path) == [('a', 'c'), ('c', 'd'), ('d', 'g'), ('g', 'i')]
    assert (len(graph.path_list_to_edges(result_path))) == len(result_path) - 1
    result_path = ['a', 'e', 'i']
    assert graph.path_list_to_edges(result_path) == [('a', 'e'), ('e', 'i')]
    assert (len(graph.path_list_to_edges(result_path))) == len(result_path) - 1
    result_path = ['A', 'C', 'D']
    assert graph_topology_simple.path_list_to_edges(result_path) == [('A', 'C'), ('C', 'D')]
    assert (len(graph_topology_simple.path_list_to_edges(result_path))) == len(result_path) - 1
    result_path = ['B', 'C']
    assert graph_topology_simple.path_list_to_edges(result_path) == [('B', 'C')]
    assert (len(graph_topology_simple.path_list_to_edges(result_path))) == len(result_path) - 1
    result_path = ['B', 'C', 'D']
    assert graph_topology_simple.path_list_to_edges(result_path) == [('B', 'C'), ('C', 'D')]
    assert (len(graph_topology_simple.path_list_to_edges(result_path))) == len(result_path) - 1
    result_path = ['A', 'B', 'D']
    assert graph_topology_simple.path_list_to_edges(result_path) == [('A', 'B'), ('B', 'D')]
    assert (len(graph_topology_simple.path_list_to_edges(result_path))) == len(result_path) - 1
    result_path = ['D', 'F', 'P', 'O', 'N']
    assert graph_topology.path_list_to_edges(result_path) == [('D', 'F'), ('F', 'P'), ('P', 'O'), ('O', 'N')]
    assert (len(graph_topology.path_list_to_edges(result_path))) == len(result_path) - 1
    result_path = ['I', 'J', 'K', 'N', 'O', 'G', 'H']
    assert graph_topology.path_list_to_edges(result_path) == [('I', 'J'), ('J', 'K'), ('K', 'N'), ('N', 'O'), ('O', 'G'), ('G', 'H')]
    assert (len(graph_topology.path_list_to_edges(result_path))) == len(result_path) - 1
    result_path = ['A', 'B', 'I', 'J', 'K', 'N', 'O']
    assert graph_topology.path_list_to_edges(result_path) == [('A', 'B'), ('B', 'I'), ('I', 'J'), ('J', 'K'), ('K', 'N'), ('N', 'O')]
    assert (len(graph_topology.path_list_to_edges(result_path))) == len(result_path) - 1

def test_connections(graph):
    result_path = ['a', 'c', 'd', 'g', 'i']
    connection_edges = graph.path_list_to_edges(result_path)
    assert graph.get_edge_list_capacities(connection_edges) == [1, 1, 1, 1]
    success = graph.add_connection(result_path)
    assert graph.get_edge_list_capacities(connection_edges) == [0, 0, 0, 0]
    assert graph.get_edge_list_delays(connection_edges) == [3, 1, 2, 2]
    assert success == True

    result_path = ['a', 'e', 'i']
    pass
def test_connections_topology_simple(graph_topology_simple):
    result_path = ['A', 'C', 'D']
    result_path = ['B', 'C']
    result_path = ['B', 'C', 'D']
    result_path = ['A', 'B', 'D']
def test_connections_topology_complex(graph_topology):
    result_path = ['D', 'F', 'P', 'O', 'N']
    result_path = ['I', 'J', 'K', 'N', 'O', 'G', 'H']
    result_path = ['A', 'B', 'I', 'J', 'K', 'N', 'O']
