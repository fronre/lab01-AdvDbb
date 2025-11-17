import os

PAGE_SIZE = 4096

def create_test_file(file_name, num_pages=3):
    with open(file_name, 'wb') as f:
        for i in range(num_pages):
            f.write(bytes([i % 256] * PAGE_SIZE))


def read_page(file_name, param):
    pass


def test_read_page():
    file_name = "test_heap.dat"
    create_test_file(file_name, num_pages=3)

    data = read_page(file_name, 0)
    assert len(data) == PAGE_SIZE
    assert data[0] == 0

    data = read_page(file_name, 2)
    assert len(data) == PAGE_SIZE
    assert data[0] == 2

    try:
        read_page(file_name, 5)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        read_page(file_name, -1)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    print("All tests passed!")
    os.remove(file_name)

test_read_page()
