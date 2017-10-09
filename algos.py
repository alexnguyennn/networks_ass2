class PathAlgorithms:
    def shortest_hop_mst(self, graph, source):
        """
        Shortest Hop Minimum spannign tree (SHP)
        """
        # init visited = src, path, nodes
        visited = {source: 0}
        pred = {}
        nodes = set(graph.nodes)

        # while nodes not empty
        while nodes:
            curr_node = None
            # grab neighbour node with lowest cost path
            for n in nodes:
                if n in visited:
                    # init curr = src node
                    if curr_node is None:
                        curr_node = n
                    # update lowest cost neighbour
                    elif visited[n] < visited[curr_node]:
                        curr_node = n
            if curr_node is None:
                break

            # remove curr node, grab curr delay so far
            nodes.remove(curr_node)
            curr_delay = visited[curr_node]

            # check connected edges
            for e in graph.edges[curr_node]:
                delay = curr_delay + 1
                # if edge !visited, update new path
                if e not in visited:
                    visited[e] = delay
                    pred[e] = curr_node

        print("MST {}".format(pred))
        print("SHP FROM {} {}\n".format(source, visited))
        return visited, pred

    def shortest_delay_mst(self, graph, source):
        """
        Shortest Delay Path Minimum spanning tree algorithm (SDP)
        Returns visited array and pred
        """
        # init visited = src, path, nodes
        visited = {source: 0}
        pred = {}
        nodes = set(graph.nodes)

        while True:
            min_node = None
            # grab node with min delay
            for n in nodes:
                if n in visited:
                    if min_node is None:
                        min_node = n
                    elif visited[n] < visited[min_node]:
                        min_node = n
            # all nodes visited, exit djikstras
            if min_node is None:
                break

            # grab min_node delay + remove min_node from set
            nodes.remove(min_node)
            curr_delay = visited[min_node]

            # edge relaxation
            for e in graph.edges[min_node]:
                delay = curr_delay + graph.delays[(min_node, e)]
                # if link delay < known link delay, update new path
                if e not in visited or delay < visited[e]:
                    visited[e] = delay
                    pred[e] = min_node

        print("MST {}".format(pred))
        print("SDP FROM {} {}\n".format(source, visited))
        return visited, pred
