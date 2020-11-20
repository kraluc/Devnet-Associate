#!/bin/env python

import sys, os
import pytest

sys.path.append(os.path.join(os.path.curdir,'Unit_testing_45'))
from is_greater import is_greater


@pytest.fixture
def tools_lib():
    import tools
    # setup
    t = tools.Tools('admin') # Tools is not defined!
    yield t
    # teardown
    del t

    return tools.Tools('admin')

def test_true_when_greater(tools_lib):
    assert tools_lib.is_greater(5, 4)

def test_user(tools_lib):
    assert tools_lib.user == 'admin'

def test_false_when_equal(tools_lib):
    assert not tools_lib.is_greater(5, 5)

