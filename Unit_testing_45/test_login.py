import os, sys
import pytest

sys.path.append(os.path.join(os.path.curdir, 'Unit_testing_45'))

@pytest.fixture
def tools_lib():
    from login import Login
    # setup
    t = Login()
    yield t
    # teardown
    del t

def test_fails_without_loging(tools_lib):
    assert tools_lib.msg == None

def test_true_when_authenticated(tools_lib):
    t = tools_lib
    t.login('guest', 'guest')
    print(f'result = {t.msg}')
    assert  tools_lib.msg == "success"

def test_true_when_authentication_fails(tools_lib):
    t = tools_lib
    t.login('guest', 'wrong')
    print(f'result = {t.msg}')
    assert tools_lib.msg == "ERR:authentication_failed"

def test_false_when_authentication_fails(tools_lib):
    t = tools_lib
    t.login('guest', 'wrong')
    print(f'result = {t.msg}')
    assert not tools_lib.msg == "success"