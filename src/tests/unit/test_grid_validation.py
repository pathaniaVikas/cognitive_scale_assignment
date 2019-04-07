from common import validator
import pytest
import conftest
import json


__builtins__['Cllog'] = conftest.Log(conftest.get_cllog_logger())


def test_validator():

    test_input = {
    "no_of_vertices": 4,
    "edges": [
    {"start_vertex": 1, "end_vertex": 2, "length": 2, "speed_factor":10},
    {"start_vertex": 2, "end_vertex": 3, "length": 2, "speed_factor":10}
    ]
    }

    try:
        validator.validate_input(json.dumps(test_input))
        pytest.fail("Unexpected Error ..")
    except ValueError, fault:
        Cllog.info("expected here due to not connected status: %s", fault)

    test_input = {
    "no_of_vertices": 2,
    "edges": [
    {"start_vertex": 1, "end_vertex": 3, "length": 2, "speed_factor":10},
    {"start_vertex": 1, "end_vertex": 5, "length": 2, "speed_factor":10}
    ]
    }

    try:
        validator.validate_input(json.dumps(test_input))
        pytest.fail("Unexpected Error ..")
    except ValueError, fault:
        Cllog.info("expected here due to edge to vertex not in graph: %s", fault)


    test_input = {
    "no_of_vertices": 2,
    "edges": [
    {"start_vertex": 1, "end_vertex": 1, "length": 2, "speed_factor":10},
    {"start_vertex": 1, "end_vertex": 2, "length": 2, "speed_factor":10}
    ]
    }

    try:
        validator.validate_input(json.dumps(test_input))
        pytest.fail("Unexpected Error ..")
    except ValueError, fault:
        Cllog.info("expected here due to path to self: %s", fault)


    test_input = {
    "no_of_vertices": 2,
    "edges": [
    {"start_vertex": 1, "end_vertex": 2, "length": 2, "speed_factor":10},
    {"start_vertex": 1, "end_vertex": 2, "length": -2, "speed_factor":10}
    ]
    }

    try:
        validator.validate_input(json.dumps(test_input))
        pytest.fail("Unexpected Error ..")
    except ValueError, fault:
        Cllog.info("expected here due to negative values for length: %s", fault)
