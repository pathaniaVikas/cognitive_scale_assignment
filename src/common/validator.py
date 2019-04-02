
import json

def validate_input(grid_data):
    """
    validate input params for creating grid
    Cllog is provided in builtins, when server starts
    """
    try:
        json.loads(grid_data)
    except Exception, fault:
        Cllog.error("Error parsing input json data. \
            Input data is not in correct json format. Error: %s", fault)
        raise

    # must contain more than two vertices
    no_of_vertices = int(grid_data.get('no_of_vertices'))

    if not no_of_vertices or no_of_vertices < 2:
        Cllog.error("Error while validating input data. No of vertices should be \
                    greater than 2")
        raise Exception("Input data is not valid, no of vertices are less than 2")

    edges = grid_data.get('edges')
    try:
        for edge in edges:
            u = edge['start_vertex']
            v = edge['end_vertex']
            l = edge['length']
            s = edge['speed_factor']

            if u == v:
                raise Exception("Start edge and End edge should be different as \
                    circular edges are not allowed")
            elif l < 0 or s < 0:
                raise Exception("Negative values are not allowed for length or \
                    speed_factor")
    except Exception, fault:
        Cllog.error("Error while parsing edges of grid. Error: %s", fault) 
        raise