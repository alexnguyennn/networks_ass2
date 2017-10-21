class VirtualConnection:
    def __init__(self, start, src, dest, duration):
        self.path = []  # fill in with djikstras
        self.path_delay = 0
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
        self.path, self.path_delay = path_algorithm(graph, self.src, self.dest,
                                                    path_type)
        success = graph.add_connection(self)
        # if success is True:
        #     # TODO: update when stats manager does its thing - it worked!
        #     self.path = calc_path
        #     pass
        # else:
        #     # update blocked path
        #     pass
        return success  # pass status up
