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

    def add_circuit(self, circuit_edges):
        # TODO fill out. returns boolean based on success/blocked
        # maybe return a unique id instead?
        pass

    def remove_circuit(self, circuit_edges):
        # TODO fill out. returns boolean based on success/blocked
        # maybe pass in unique id instead?
        pass

    def parse_topology(self, file_path):
        f = open(file_path, "r")
        data = f.readlines()
        for line in data:
            line = line.split()
            x = line[0]
            y = line[1]
            delay = line[2]
            cap = line[2]
            #print("x = {}, y = {}, delay = {}, cap = {}".format(x, y, delay, cap))
            self.add_node(x)
            self.add_node(y)
            self.add_edge(x, y, int(delay), int(cap))

# display graph nodes, links, link delay values, link capacity, curr link load
# NOTE: curr link load set to None since workload methods are not implemented yet

    def show_graph(self):
        for n in self.nodes:
            print("router = {}".format(n))
            for e in self.graph.edges[n]:
                print("nb: {} | delay: {} | capacity: {} | load: {}" \
                .format(e, self.graph.delays[(n, e)], self.graph.cap[(n, e)], None))
            print("-----------------")
        return None
