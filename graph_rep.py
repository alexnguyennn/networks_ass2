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
        self.connections = set() # connections? #TODO explore?

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

    def add_connection(self, connection_path):
        # TODO - accept virtual connection class instead?
        # TODO fill out. returns boolean based on success/blocked
        # maybe return a unique id instead?
        # for node in connection_path:
        # 3.
        connection_edges = self.path_list_to_edges(connection_path)
        cap_list =self.get_edge_list_capacities(connection_edges)
        for cap in cap_list:
            if cap < 1:
                return False
        for edge_tuple in connection_edges:
            self.cap[edge_tuple] -= 1
        return True


    def remove_connection(self, connection_path):
        # TODO fill out. returns boolean based on success/blocked
        # maybe pass in unique id instead?
        # 4.
        # TODO check if THIS specific connection is on path first?
        connection_edges = self.path_list_to_edges(connection_path)
        try:
            for edge_tuple in connection_edges:
                self.cap[edge_tuple] -= 1
            return True
        except e:
            return False

    def path_list_to_edges(self, path):
        """convert to list of edge tuples (from_n, to_n), helper for above methods
        nEdges = nNodes - 1
        """
        # 1.
        nodes = iter(path)
        edges = []
        from_node = None
        for node in nodes:
            if from_node is None:
                from_node = node
                to_node = next(nodes)
            else:
                from_node = to_node
                to_node = node
            edges.append((from_node, to_node))
        return edges

    def get_edge_list_delays(self, edge_list):
        """
        Input: list of tuples (from_n, to_n)
        Return list of delays corresponding to each tuple
        """
        result = []
        for edge_tuple in edge_list:
            result.append(self.delays[edge_tuple])
        return result

    def get_edge_list_capacities(self, edge_list):
        #3.
        result = []
        for edge_tuple in edge_list:
            result.append(self.cap[edge_tuple])
        return result

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
