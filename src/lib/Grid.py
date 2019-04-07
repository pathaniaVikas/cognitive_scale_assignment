
from common import Params
class Node():
    def __init__(self, vertex):
        self.vertex = vertex
        self.travel_time = Params.INFINITY

    def __str__(self):
        return str(self.vertex)

    def __repr__(self):
        return str(self.vertex)

    def __hash__(self):
        return hash((self.vertex))

    def __eq__(self, other):
        return (self.vertex) == (other.vertex)

    def __ne__(self, other):
        return not(self.vertex == other.vertex)

class Grid:
    """
    Class to initiate graph, create it, update it.
    """
    
    def __init__(self):
        self.graph = {}

    def __str__(self):
        return str(self.graph)

    def __repr__(self):
        return str(self.graph)

    def __init_graph(self, no_of_vertices):
        for x in range(no_of_vertices):
            node = Node(x+1)
            self.graph[node] = []

    def _check_and_update_existing_edge(self, u, v, t, remove_edge=False):
        for edge in self.graph[u]:
            if edge["end_vertex"] == v:
                if remove_edge:
                    self.graph[u].remove(edge)
                else:
                    edge["travel_time"] = t
                return True
        return False

    def create_grid(self, no_of_vertices, edges):
        self.__init_graph(no_of_vertices)
        
        for edge in edges:
            u = Node(edge['start_vertex'])
            v = Node(edge['end_vertex'])
            l = edge['length']
            s = edge['speed_factor']

            t = float(l)/s

            if u not in self.graph or v not in self.graph:
                # vertex does not exist in graph
                raise ValueError("Vertex %s or %s does not exist in grid"%(u, v))
                
            # if edge exists update it else
            if not self._check_and_update_existing_edge(u, v, t):
                self.graph[u].append({"end_vertex": v, "travel_time": t})

    def update_grid(self, edges):
        for edge in edges:
            u = Node(edge['start_vertex'])
            v = Node(edge['end_vertex'])
            l = edge['length']
            s = edge['speed_factor']
            remove_edge = edge['remove_edge']

            if not self.graph.get(u) or not self.graph.get(v):
                # vertex does not exist in graph
                raise ValueError("Vertex %s or %s does not exist in grid"%(u, v))
            
            t = float(l)/s

            if remove_edge:
                self._check_and_update_existing_edge(u, v, t, remove_edge=True)
            else:
                # if edge exists update it
                if not self._check_and_update_existing_edge(u, v, t):
                    self.graph[u].append({"end_vertex": v, "travel_time": t})

    def get_grid(self):
        """
        returns 
        {
            "vertex_no": [{end_vertex: e, travel_time: t}.....]
        }
        """
        return self.graph


    def dfs(self, node, visited):
        adj_list = self.graph.get(node)

        for edge in adj_list:
            end_vertex = edge["end_vertex"]
            if visited[end_vertex.vertex-1] == Params.NOT_VISITED:
                visited[end_vertex.vertex-1] = Params.VISITED
                self.dfs(end_vertex, visited)


    def is_connected(self):
        visited = [Params.NOT_VISITED]*len(self.graph)

        if len(self.graph) == 0:
            return False

        node = Node(1)
        visited[0] = Params.VISITED
        self.dfs(node, visited)
        # if all elements in visited is 1, it means we have traversed every
        # vertex in graph and hence all vertices are connected
        if sum(visited) == len(visited):
            return True

        return False
