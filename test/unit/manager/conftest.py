import pytest
from unittest.mock import patch

@pytest.fixture(autouse=True)
def prepend_module(monkeypatch):
    monkeypatch.syspath_prepend('../../source/api/chalicelib/')

@pytest.fixture
def manager_lambda(prepend_module):
    import efs_lambda
    yield efs_lambda