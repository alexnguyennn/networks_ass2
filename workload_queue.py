from virtual_connection import VirtualConnection
from helper_data_structures import UpdateablePriorityQueue
from collections import namedtuple

WorkloadTuple = namedtuple('WorkloadTuple', 'time, connection')


class WorkloadQueue:
    def __init__(self, workload_file_path):
        workload_tuple_list = self.parse_workload(workload_file_path)
        self.queue = UpdateablePriorityQueue(workload_tuple_list)

    def add(self, connection_tuple):
        # add virtual connection and sort as you go
        # add equivalent action on duration
        self.queue.insert(connection_tuple)

    def pop(self):
        return self.queue.pop()

    def parse_workload(self, file_path):
        # NOTE: add in cleanup connections at duration on the fly IF connection succeeds
        # Only parses initial workload
        # return list of tuple in form of (time to deal, virtualconnection)
        f = open(file_path, "r")
        data = f.readlines()
        result = []
        for line in data:
            line = line.split()
            time_start = float(line[0])
            src = line[1]
            dest = line[2]
            duration = float(line[3])
            #print("x = {}, y = {}, delay = {}, cap = {}".format(x, y, delay, cap))
            result.append(
                WorkloadTuple(
                    time=time_start,
                    connection=VirtualConnection(time_start, src, dest,
                                                 duration)))
        return result

    def peek_final_connection(self):
        return self.queue.peek_largest(1)[0]

    def peek_duration(self):
        return self.queue.peek_largest(1)[0].time
