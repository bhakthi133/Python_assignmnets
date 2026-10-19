#(a) A fixture named sample_values providing {a, b, expected_sum}.
import pytest
@pytest.fixture
def sample_values():
    return {"a":10,"b":7,"res":17}
from calculator import add
def test_add(sample_values):
    a=sample_values["a"]
    b=sample_values["b"]
    res=sample_values["res"]
    assert add(a,b) == res

@pytest.fixture
def samp():
    return [4,6,10]
def test_addition(samp):
    a,b,res=samp
    assert add(a,b) == res

@pytest.fixture
def sampl():
    return 4,6,10
def test_addition(sampl):
    a,b,res=sampl
    assert add(a,b) == res

#(c) A parametrized test test_multiply with at least 4 combinations. 
from calculator import multiply
@pytest.mark.parametrize("a,b,res",[(3,2,6),(7,-2,-14),(-2,-2,4),(9,0,0)])
def test_mul(a,b,res):
    assert multiply(a,b) == res

#(d) pytest.raises to confirm divide(10,0) raises ZeroDivisionError. Edge case: divide(0,5) returns 0.0. 
from calculator import divide
def test_div():
    with pytest.raises(ZeroDivisionError):
        #10/0
        divide(10,0)
        #divide(10,1)
    assert divide(0,5) == pytest.approx(0)