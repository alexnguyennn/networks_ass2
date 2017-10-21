#!/usr/bin/python3

import sys
from pathing_algorithms import shortest_delay_mst, shortest_hop_mst
from graph_rep import Graph
# NOTE: empty classes atm
from routing_timer import RoutingTimer
from virtual_circuit import VirtualCircuit
from statistics_manager import StatisticsManager
from workload_queue import WorkloadQueue


class RoutingPerformance:
    """
    Routing Performance Program
    """

    # NOTE: moved init_topology/ show_graph to graph_rep
    def __init__(self, g, top, work):
        self.graph = g
        # init graph topology: routers, delay, capacity
        self.graph.parse_topology(top)
        self.workload = work
        # TODO: track virtualcircuits in flight somehow, implement timer start/stop
        # variables (queue of connections, network/circuit mode etc), parseWorkload()
        # TODO parse workload file into sorted queue

    # init VC requests
    def start_requests(self):
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
        r = RoutingPerformance(graph, TOPOLOGY_FILE, WORKLOAD_FILE)

        # init nodes, links, delay and capacity values is done on creation
        # it should also parseworkload and create queue above

        # test
        r.graph.show_graph()

        # start virtual connection requests
        r.start_requests()

        # Select scheme
        if ROUTING_SCHEME == "SHP":
            print("[ SCHEME: SHORTEST HOP PATH ]")
            SHP = shortest_hop_mst(r.graph, 'A')
        elif ROUTING_SCHEME == "SDP":
            print("[ SCHEME: SHORTEST DELAY PATH ]")
            SDP = shortest_delay_mst(r.graph, 'A')
