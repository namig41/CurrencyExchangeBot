from punq import Container
from pytest import fixture

from tests.fixtures import init_dummy_container


@fixture
def container() -> Container:
    return init_dummy_container()
