from infrastructure.contrainer.init import _init_container
from punq import Container


def init_dummy_container() -> Container:
    container = _init_container()
    return container
