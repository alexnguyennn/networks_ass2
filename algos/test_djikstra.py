import pytest
from djikstra import shortest_path
def create_graph_from_txt(file_path):
    pass

def test_graph_creation(graph, expected_graph):
    pass

def test_djikstra(graph, src, dest, expected_cost, expected_string):
    path_cost, path_string = shortest_path(graph, src, dest)
    assert path_cost == expected_cost
    assert path_string == expected_string
