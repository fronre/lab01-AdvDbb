from lab01-AdvDbb.index import create_heap_file
import os

def test_create_heap_file():
    name = "tdd_heap.dat"
    if os.path.exists(name):
        os.remove(name)

    create_heap_file(name)

    assert os.path.exists(name)
    assert os.path.getsize(name) == 0
