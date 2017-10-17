#!/usr/bin/python3
import pytest
from pathing_algorithms import shortest_delay_mst, shortest_hop_mst, shortest_path




def test_shortest_delay_path(graph):
    result_path, result_delays = shortest_path(graph, 'a', 'i')
    assert result_path == ['a', 'c', 'd', 'g', 'i']
    assert result_delays == 8

def test_shortest_delay_path_brian(graph):
    result_path, result_delays = shortest_delay_mst(graph, 'a', 'i')
    assert result_path == ['a', 'c', 'd', 'g', 'i']
    assert result_delays == 8

def test_shortest_hop_path(graph):
    result_path, result_hops = shortest_path(graph, 'a', 'i', path_type='SHP')
    assert result_path == ['a', 'e', 'i']
    assert result_hops == 2

def test_shortest_hop_path_brian(graph):
    result_path, result_hops = shortest_hop_mst(graph, 'a', 'i')
    assert result_path == ['a', 'e', 'i']
    assert result_hops == 2

def test_shortest_delay_txt_topology_simple(graph_topology_simple):
    result_path, result_delays = shortest_path(graph_topology_simple, 'A',
                                                'D')
    assert result_path == ['A', 'C', 'D']
    assert result_delays == 23
    result_path, result_delays = shortest_path(graph_topology_simple, 'B',
                                                'C')
    assert result_path == ['B', 'C']
    assert result_delays == 20
    result_path, result_delays = shortest_path(graph_topology_simple, 'B',
                                                'D')
    assert result_path == ['B', 'C', 'D']
    assert result_delays == 28

def test_shortest_delay_txt_topology_simple_brian(graph_topology_simple):
    result_path, result_delays = shortest_delay_mst(graph_topology_simple, 'A',
                                                'D')
    assert result_path == ['A', 'C', 'D']
    assert result_delays == 23
    result_path, result_delays = shortest_delay_mst(graph_topology_simple, 'B',
                                                'C')
    assert result_path == ['B', 'C']
    assert result_delays == 20
    result_path, result_delays = shortest_delay_mst(graph_topology_simple, 'B',
                                                'D')
    assert result_path == ['B', 'C', 'D']
    assert result_delays == 28

def test_shortest_hop_txt_topology_simple(graph_topology_simple):
    result_path, result_hops = shortest_path(graph_topology_simple, 'A',
                                                'D', path_type='SHP')
    assert result_path == ['A', 'B', 'D'] or result_path == ['A', 'C', 'D']
    assert result_hops == 2

def test_shortest_hop_txt_topology_simple_brian(graph_topology_simple):
    result_path, result_hops = shortest_hop_mst(graph_topology_simple, 'A',
                                                'D')
    # should be random choice between these 2
    assert result_path == ['A', 'B', 'D'] or result_path == ['A', 'C', 'D']
    assert result_hops == 2

def test_shortest_delay_txt_topology_brian(graph_topology):
    result_path, result_delays = shortest_delay_mst(graph_topology, 'D',
                                                    'N')
    assert result_path == ['D', 'F', 'P', 'O', 'N']
    assert result_delays == 180
    result_path, result_delays = shortest_delay_mst(graph_topology, 'I',
                                                'H')
    assert result_path == ['I', 'J', 'K', 'N', 'O', 'G', 'H']
    assert result_delays == 245
    result_path, result_delays = shortest_delay_mst(graph_topology, 'A',
                                                'O')
    assert result_path == ['A', 'B', 'I', 'J', 'K', 'N', 'O']
    assert result_delays == 235


def test_shortest_delay_txt_topology(graph_topology):
    result_path, result_delays = shortest_path(graph_topology, 'D',
                                                    'N', path_type='SDP')
    assert result_path == ['D', 'F', 'P', 'O', 'N']
    assert result_delays == 180
    result_path, result_delays = shortest_path(graph_topology, 'I',
                                                'H', path_type='SDP')
    assert result_path == ['I', 'J', 'K', 'N', 'O', 'G', 'H']
    assert result_delays == 245
    result_path, result_delays = shortest_path(graph_topology, 'A',
                                                'O', path_type='SDP')
    assert result_path == ['A', 'B', 'I', 'J', 'K', 'N', 'O']
    assert result_delays == 235

def test_shortest_hop_txt_topology_brian(graph_topology):
    result_path, result_hops = shortest_hop_mst(graph_topology, 'D',
                                                'N')
    assert result_path == ['D', 'F', 'O', 'N']
    assert result_hops == 3
    result_path, result_hops = shortest_hop_mst(graph_topology, 'I',
                                                'H')
    assert result_path == ['I', 'B', 'A', 'H']
    assert result_hops == 3
    result_path, result_delays = shortest_hop_mst(graph_topology, 'A',
                                                'O')
    assert result_path == ['A', 'H', 'G', 'O'] or result_path == ['A', 'H', 'F', 'O']
    assert result_hops == 3

def test_shortest_hop_txt_topology(graph_topology):
    result_path, result_hops = shortest_path(graph_topology, 'D',
                                                'N', path_type='SHP')
    assert result_path == ['D', 'F', 'O', 'N']
    assert result_hops == 3
    result_path, result_hops = shortest_path(graph_topology, 'I',
                                                'H', path_type='SHP')
    assert result_path == ['I', 'B', 'A', 'H']
    assert result_hops == 3
    result_path, result_delays = shortest_path(graph_topology, 'A',
                                                'O', path_type='SHP')
    assert result_path == ['A', 'H', 'G', 'O'] or result_path == ['A', 'H', 'F', 'O']
    assert result_hops == 3
