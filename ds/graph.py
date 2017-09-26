class Edge:
    def __init__(self, v, w, cost):
        self.v = v
        self.w = w
        self.cost = cost
    def get_cost(self):
        return self.cost
    def set_cost(self, cost):
        self.cost = cost


class Graph: #assume bidirectional edges?
    def __init__(self, size):
        self.n_vertices = size #vertices
        self.n_edges = 0 #edges
        self.edges = [[-1] * (size) for i in range(size)] # matrix of booleans for each vertex
    def insert_edge(self, edge):
        if self.edges[e.v][e.w] >= 0:
            return
        self.edges[e.v][e.w] = e.cost
        self.edges[e.w][e.v] = e.cost
        self.n_edges += 1
    def remove_edge(self, edge):
        if self.edges[e.v][e.w] < 0:
            return
        self.edges[e.v][e.w] = -1
        self.edges[e.w][e.v] = -1
        self.n_edges -= 1

    # def insert_vertex(self):
    #     self.edges.append([0] * self.n_vertices)
    #     for i in self.edges:
    #         i.append(0)
    #     self.n_vertices += 1

    # def remove_vertex(self):
    #     self.edges.append([0] * self.n_vertices)
    #     for i in self.edges:
    #         i.append(0)
    #     self.n_vertices += 1


    def get_edges(self):
        return self.edges
    def get_n_edges(self):
        return self.n_edges
    def get_n_vertices(self):
        return self.n_vertices

    def show(self):
        print("Vertices: {} Edges: {}", self.n_vertices, self.n_edges)
        for i in self.edges:
            n_shown = 0
            for j in self.edges[i]:
                if self.edges[i][j] >= 0:
                    print("edge: {}-{} cost: {}", i, j, self.edges[i][j])
                    n_shown += 1



