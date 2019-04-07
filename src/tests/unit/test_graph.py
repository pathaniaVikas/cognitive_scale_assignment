from common import validator
import pytest
import conftest
from lib import Grid, ShortestTimePath
import json

__builtins__['Cllog'] = conftest.Log(conftest.get_cllog_logger())


def test_create_grid():
    no_of_vertices = 4
    edges = [
        {
            'start_vertex': 1,
            'end_vertex': 2,
            'length': 3,
            'speed_factor': 3
        },
        {
            'start_vertex': 1,
            'end_vertex': 3,
            'length': 3,
            'speed_factor': 4
        },
        {
            'start_vertex': 1,
            'end_vertex': 4,
            'length': 3,
            'speed_factor': 5
        }
    ]
    graph_repr = {1: [{'travel_time': 1.0, 'end_vertex': 2}, {'travel_time': 1.0, 'end_vertex': 3}, {'travel_time': 1.0, 'end_vertex': 4}], 2: [], 3: [], 4: []}
    graph = Grid.Grid()
    graph.create_grid(no_of_vertices, edges)
    assert len(graph.get_grid()) == no_of_vertices
    assert graph.is_connected() == True


    stp = ShortestTimePath.ShortestTimePath(graph.get_grid())
    Cllog.info(stp.find_shortest_path(1,2))
    Cllog.info(stp.find_shortest_path(1,3))
    Cllog.info(stp.find_shortest_path(1,4))
