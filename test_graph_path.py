#!/usr/bin/python3
import pytest
from pathing_algorithms import shortest_delay_mst, shortest_hop_mst, shortest_delay
from graph_rep import Graph


@pytest.fixture
def graph_topology():
    graph = Graph()
    graph.parse_topology('./topology.txt')
    return graph


@pytest.fixture
def graph():
    graph = Graph()
    cur_node = 'a'
    while cur_node <= 'i':
        graph.add_node(cur_node)
        cur_node = chr(ord(cur_node) + 1)
    graph.add_edge('a', 'b', 5, 1)
    graph.add_edge('a', 'c', 3, 1)
    graph.add_edge('a', 'e', 2, 1)
    graph.add_edge('b', 'd', 2, 1)
    graph.add_edge('c', 'b', 1, 1)
    graph.add_edge('c', 'd', 1, 1)
    graph.add_edge('d', 'g', 2, 1)
    graph.add_edge('d', 'h', 1, 1)
    graph.add_edge('e', 'h', 4, 1)
    graph.add_edge('e', 'i', 7, 1)
    graph.add_edge('f', 'b', 3, 1)
    graph.add_edge('f', 'g', 1, 1)
    graph.add_edge('g', 'c', 4, 1)
    graph.add_edge('g', 'i', 2, 1)
    graph.add_edge('h', 'c', 2, 1)
    graph.add_edge('h', 'f', 2, 1)
    graph.add_edge('h', 'g', 2, 1)
    return graph


def test_shortest_delay_path(graph):
    result_path, result_delays = shortest_delay(graph, 'a', 'i')
    assert result_path == ['a', 'c', 'd', 'g', 'i']
    assert result_delays['i'] == 8


def test_shortest_delay_txt_topology(graph):
    result_path, result_delays = shortest_delay(graph, 'a', 'i')
    assert result_path == ['a', 'c', 'd', 'g', 'i']
    assert result_delays['i'] == 8
