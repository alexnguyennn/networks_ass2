import queue
import warnings
import heapq

# assume - unique items; will throw warning if duplicate is added. Duplicates are both updated if found
# NOTE: make sure item_tuple is always in form of (priority, item)
class UpdateablePriorityQueue:
    def __init__(self, init_list):
        self.heap_list = init_list
        heapq.heapify(self.heap_list)

    def __len__(self):
        return len(self.heap_list)

    def __contains__(self, vertex):
        for item_tuple in self.heap_list:
            if item_tuple[1] == vertex:
                return True
        return False

    # input in (priority, item)
    def insert(self, item_tuple):
        if (item_tuple in self.heap_list):
            warnings.warn(
                "tuple already exists; any updates will update both iterations",
                UserWarning)
        heapq.heappush(self.heap_list, item_tuple)

    def pop(self):
        return heapq.heappop(self.heap_list)

    # input in (priority, item)
    def update_priority(self, item_tuple):
        if len(item_tuple) > 2:
            raise AttributeError('expected tuple in the form (item, value)')
        update_flag = False
        for t in self.heap_list:
            if t[1] == item_tuple[1]:
                self.heap_list.remove(t)
                self.insert(item_tuple)
                update_flag = True
        if not update_flag:
            warnings.warn("tuple not found - no update made", UserWarning)


def shortest_path(graph, source, dest, path_type='SDP'):
    """
    Find shortest path to dest node from source using 2 path_types:
    Shortest Hop Path & Shortest Delay Path (specify with path_type)
    Calculates dist{v} - holds minimum distance to each v
    Follow chain of prev{v} to generate shortest path to dest node v

    NOTE: does same as MST, but SHP/SDP modes are parameterised
    Pseudocode Source: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    """
    vertices = UpdateablePriorityQueue([])
    dist = {}
    prev = {}
    for vertex in graph.nodes:
        dist[vertex] = float('inf')
        prev[vertex] = None  # set previous for a vertex when possible
        vertices.insert((dist[vertex], vertex))
    dist[source] = 0
    vertices.update_priority((dist[source], source))
    while len(vertices) > 0:
        # take lowest valued entries first; tuple (vertex, dist[vertex])
        u_cur_delay, u = vertices.pop()
        for neighbour_v in graph.edges[u]:
            if neighbour_v not in vertices:
               continue # skip stuff not in queue anymore
            # in SHP, all delays are 1 (only counting link hops)
            if path_type == 'SHP': 
                added_delay = 1
                altered_delay = u_cur_delay + added_delay
            elif path_type == 'SDP':
                added_delay = graph.delays[(u, neighbour_v)] 
                altered_delay = u_cur_delay + added_delay
            elif path_type == 'LLP':
                altered_delay = ( len(graph.virtual_connections) ) / ( graph.cap[(u, neighbour_v)] )
            else:
                raise ValueError("Invalid value for path_type to shortest_path")
            # if new altered cost is less than a current minimum dist TO a neighbour, update
            if altered_delay < dist[neighbour_v]:
                dist[neighbour_v] = altered_delay
                prev[neighbour_v] = u
                vertices.update_priority((dist[neighbour_v], neighbour_v))
    return get_path_dist_tuple(dist, prev, dest)

def shortest_hop_mst(graph, source, dest):
    """ Shortest Hop Minimum spannign tree (SHP) """
    # init visited = src, path, nodes
    visited = {source: 0}
    pred = {source: None}
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
    return get_path_dist_tuple(visited, pred, dest)


def shortest_delay_mst(graph, source, dest):
    """
    Shortest Delay Path Minimum spanning tree algorithm (SDP)
    Returns visited array and pred
    """
    # init visited = src, path, nodes
    visited = {source: 0}
    pred = {source: None}
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
    return get_path_dist_tuple(visited, pred, dest)
    #return visited, pred

def get_path_dist_tuple(distance_dict, prev_node_dict, dest):
    # calculate path, cost from source to dest:
    u = dest
    path = []
    while u is not None:
        path.insert(0, u)
        u = prev_node_dict[u]
    return (path, distance_dict[dest])

