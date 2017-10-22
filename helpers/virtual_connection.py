class VirtualConnection:
    def __init__(self, start, src, dest, duration):
        self.path = []  # fill in with djikstras
        self.path_delay = 0  # delay of each node on path
        self.path_cost = 0  # cost calculated by algorithm (delay for SHP/SDP, load for LLP)
        self.src = src
        self.dest = dest
        self.start = start
        self.duration = duration
        # TODO fill out
        # track: circuitEdges (dictionary), duration, [packet_rate] (if type = circuit)
        # packet rate now moved to statistics manager
        # duration, isActive
        # getPath (call algorithm)
        self.is_processed = False  # set flag after attempt to fill path

    def fill_path(self, graph, path_algorithm, path_type):
        self.path, self.path_cost = path_algorithm(graph, self.src, self.dest,
                                                   path_type)
        path_edges = graph.path_list_to_edges(self.path)
        self.path_delay = sum(graph.get_edge_list_delays(path_edges))
        success = graph.add_connection(self)
        # if success is True:
        #     # TODO: update when stats manager does its thing - it worked!
        #     self.path = calc_path
        #     pass
        # else:
        #     # update blocked path
        #     pass
        return success  # pass status up
