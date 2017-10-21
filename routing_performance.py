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
    def __init__(self, g, topology_file_path, work):
        self.graph = g
        # init graph topology: routers, delay, capacity
        self.graph.parse_topology(topology_file_path)
        self.workload = WorkloadQueue()
        # TODO: track virtualcircuits in flight somehow, implement timer start/stop
        # variables (queue of connections, network/circuit mode etc), parseWorkload()
        # TODO parse workload file into sorted queue
        # TODO add other parameters when reqd

    # init VC requests
    def start_requests(self):
        # main loop of program
        # pop off item from queue
        # if flag not set, attempt make connection
        # calculate path
        # attempt to put connection on graph
        # if ok, add connection onto queue at duration (to remove)
        # if not, request is blocked. discard and handle next one
        # if flag set, we just need to remove this connection to free capacity
        # repeat until empty graph

        return None
    def close_program(self):
        # print final statistics to terminal here


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
