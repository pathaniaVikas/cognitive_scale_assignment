# cognitive_scale_assignment
Optimal Route Identification:

This will find the shortest time it will take to move from point A to point B.

Input structure for graph:
{
  "no_of_vertices": N,
  "edges": [
  {
    start_vertex: u,
    end_vertex: v,
    length: l,
    speed_factor: s
  },
  ....
  ]
}

** if there are two edges with same start_vertex and end_vertex, then only latest edge will prevail in graph.
N - number of vertices

Validation conditions based on requirements:
1. There should be atleast two points in graph.(N>=2)
2. There should be edge between every two vertices.(connected graph)
3. There will be no circular edge, like edge between 3 and 3.(start_vertex != end_vertex)
4. Negative values for speed or length are not allowed.(l>=0, s>=0)



    
