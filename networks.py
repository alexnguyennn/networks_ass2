#!/usr/bin/python3

import sys
from algos import shortest_delay_mst, shortest_hop_mst
from graphRep import Graph
"""
Routing Performance Program
"""


class RoutingPerf:
    def __init__(self, g, top, work):
        self.graph = g
        self.topology = top
        self.workload = work

    # init graph topology: routers, delay, capacity
    def init_topology(self):
        f = open(self.topology, "r")
        data = f.readlines()
        for line in data:
            line = line.split()
            x = line[0]
            y = line[1]
            delay = line[2]
            cap = line[2]
            #print("x = {}, y = {}, delay = {}, cap = {}".format(x, y, delay, cap))
            self.graph.add_node(x)
            self.graph.add_node(y)
            self.graph.add_edge(x, y, int(delay), int(cap))

    # init VC requests
    def start_requests(self):
        return None

    # display graph nodes, links, link delay values, link capacity, curr link load
    # NOTE: curr link load set to None since workload methods are not implemented yet
    def show_graph(self):
        for n in self.graph.nodes:
            print("router = {}".format(n))
            for e in self.graph.edges[n]:
                print("nb: {} | delay: {} | capacity: {} | load: {}" \
                .format(e, self.graph.delays[(n, e)], self.graph.cap[(n, e)], None))
            print("-----------------")
        return None


"""
Main Function
"""
if __name__ == '__main__':
    num_args = 6
    if len(sys.argv) != num_args:
        print(
            "Usage: ./networks.py NETWORK_SCHEME ROUTING_SCHEME TOPOLOGY_FILE WORKLOAD_FILE PACKET_RATE"
        )
    else:
        # empty graph
        graph = Graph()

        # grab argument objects
        NETWORK_SCHEME, ROUTING_SCHEME, TOPOLOGY_FILE, WORKLOAD_FILE, PACKET_RATE = sys.argv[
            1:]
        r = RoutingPerf(graph, TOPOLOGY_FILE, WORKLOAD_FILE)

        # init nodes, links, delay and capacity values
        r.init_topology()

        # test
        r.show_graph()

        # start virtual connection requests
        r.start_requests()

        # Select scheme
        if ROUTING_SCHEME == "SHP":
            print("[ SCHEME: SHORTEST HOP PATH ]")
            SHP = shortest_hop_mst(r.graph, 'A')
        elif ROUTING_SCHEME == "SDP":
            print("[ SCHEME: SHORTEST DELAY PATH ]")
            SDP = shortest_path_mst(r.graph, 'A')