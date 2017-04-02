from random import randrange

import pytest
from sorting import *

functions_from_sorting = [x[1].sort for x in globals().items()
                          if 'algorithms/sorting' in str(x[1])]
functions_names_from_sorting = [x.__module__.replace('.', ' ')
                                for x in functions_from_sorting]


@pytest.fixture(scope='session',
                params=functions_from_sorting,
                ids=functions_names_from_sorting)
def sort_func(request):
    return request.param


@pytest.mark.parametrize("arr", [[randrange(1000) for x in range(1, 500)],
                                 [randrange(-1000, 0) for x in range(1, 500)],
                                 [randrange(-100, 100) for x in range(1, 500)]],
                         ids=["positive", "negative", "positive and negative"])
def test_random_range(sort_func, arr):
    assert sort_func(arr) == sorted(arr)


@pytest.mark.parametrize("arr", [[1, 1, 1, 1, 1, 1], [42], []],
                         ids=["uniform", "one element", "empty"])
def test_edge_cases(sort_func, arr):
    assert sort_func(arr) == arr
