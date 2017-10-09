#!/usr/bin/python3
import pytest
import networks as nw
import algos


@pytest.fixture
def graph():
    graph = nw.Graph()
    graph.add_edge('a', 'b', 5, 1)
    graph.add_edge('a', 'c', 3, 1)
    graph.add_edge('a', 'e', 2, 1)
    graph.add_edge('b', 'd', 2, 1)
    graph.add_edge('c', 'b', 1, 1)
    graph.add_edge('c', 'd', 1, 1)
    graph.add_edge('d', 'a', 1, 1)
    graph.add_edge('d', 'g', 2, 1)
    graph.add_edge('d', 'h', 1, 1)
    graph.add_edge('e', 'a', 1, 1)
    graph.add_edge('e', 'h', 4, 1)
    graph.add_edge('e', 'i', 7, 1)
    graph.add_edge('f', 'b', 3, 1)
    graph.add_edge('f', 'g', 1, 1)
    graph.add_edge('g', 'c', 3, 1)
    graph.add_edge('g', 'i', 2, 1)
    graph.add_edge('h', 'c', 2, 1)
    graph.add_edge('h', 'f', 2, 1)
    graph.add_edge('h', 'g', 2, 1)
    return graph


def test_shortest_delay_path(graph):
    shortest_path_algo = algos.PathAlgorithms().shortest_hop_mst
    visted, pred = shortest_path_algo(graph, 'a')
    # result_visited, result_pred = nw.find_shortest_path('a', 'i')
    # assert result == ['a', 'c', 'd', 'g', 'i']
    # assert shortest_path.path_weight['i'] == 8
