from rotacao_lista import rotacao
import pytest

def test_rotacao_k():
    assert rotacao([1,2,3,4,5,6,7,8], 5) == [1, 2, 3, 4, 5]