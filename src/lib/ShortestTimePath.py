from common import Params
from lib.Grid import Node

class ShortestTimePath():

    def __init__(self, graph):
        self.graph = graph


    def minimum_time_taken(self, time_taken, visited): 
  
        # Initilaize minimum time_taken for next node 
        min = Params.INFINITY 

        for v in range(len(self.graph)): 
            Cllog.info(time_taken)
            Cllog.info(visited)
            if time_taken[v] < min and visited[v] == Params.NOT_VISITED: 
                min = time_taken[v] 
                min_index = v 
  
        return min_index

    def find_shortest_path(self, source, dest):

        u = Node(source)
        v = Node(dest)

        if u not in self.graph or v not in self.graph:
            # vertex does not exist in graph
            raise ValueError("Vertex %s or %s does not exist in grid"%(u, v))

        # mark all nodes unvisited
        visited = [Params.NOT_VISITED]*len(self.graph)

        # set infinite time_taken for all nodes
        time_taken = [Params.INFINITY]*len(self.graph)

        # set zero time_taken for starting node
        time_taken[source] = 0

        parent = [-1]*len(self.graph)

        for vertex in range(len(self.graph)):
            
            u = self.minimum_time_taken(time_taken, visited)

            visited[u] = Params.VISITED

            u = Node(u)

            for edge in self.graph[u]:
                end_vertex = edge['end_vertex']
                travel_time = edge['travel_time']

                if visited[end_vertex.vertex-1] != Params.VISITED:
                    if time_taken[end_vertex.vertex-1] > time_taken[u.vertex-1]+travel_time:
                        time_taken[end_vertex.vertex-1] = time_taken[u.vertex-1]+travel_time

                    parent[end_vertex.vertex-1] = u.vertex

        return time_taken, parent

    def print_shortest_path(self, parent, destination):

        # start vertex is the destination
        if parent[destination] == -1:
            print destination
            return

        self.print_shortest_path(parent, parent[destination])
        print destination