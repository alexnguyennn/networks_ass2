from collections import defaultdict


class Graph:
    """
    Adjacency list Graph Representation
    """

    def __init__(self):
        self.nodes = set()  # switches/routers
        self.edges = defaultdict(list)  # links
        self.delays = {}  # link delays
        self.cap = {}  # circuit capacity
        self.load = {}  # load = Active Circuits / Capacity

    # add a new switch/router
    def add_node(self, node):
        self.nodes.add(node)

    # add a new link
    # !neighbour = infinite delay
    def add_edge(self, from_n, to_n, delay, capacity):
        # init link
        self.edges[from_n].append(to_n)
        self.edges[to_n].append(from_n)
        # init link delay
        self.delays[(from_n, to_n)] = delay
        self.delays[(to_n, from_n)] = delay
        # init link capacity
        self.cap[(from_n, to_n)] = capacity
        self.cap[(to_n, from_n)] = capacity

    def add_circuit(circuit_edges):
        # TODO fill out. returns boolean based on success/blocked
        # maybe return a unique id instead?
        pass

    def remove_circuit(circuit_edges):
        # TODO fill out. returns boolean based on success/blocked
        # maybe pass in unique id instead?
        pass

    def parse_topology(file_path):
        # TODO fill in graph init from file, make __init__ call this
        pass
