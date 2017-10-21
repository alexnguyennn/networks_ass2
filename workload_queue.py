from virtual_connection import VirtualConnection
from helper_data_structures import UpdateablePriorityQueue


class WorkloadQueue:
    def __init__(self):
        workload_tuple_list = self.parse_workload('workload.txt')
        self.queue = UpdateablePriorityQueue(workload_tuple_list)

    def add(self, connection_tuple):
        # add virtual connection and sort as you go
        # add equivalent action on duration
        self.queue.insert(connection_tuple)

    def pop():
        return self.queue.pop()

    def parse_workload(self, file_path):
        pass

    def peek_duration(self):
        return self.queue.peek_largest()
