import os
import struct

PAGE_SIZE = 4096

def create_heap_file(file_name):
    with open(file_name, 'wb'):
        pass
def read_page(file_name, page_number):
        size = os.path.getsize(file_name)
        last = size // PAGE_SIZE - 1

        if page_number < 0 or page_number > last:
            raise ValueError("Invalid page number")

        with open(file_name, 'rb') as f:
            f.seek(page_number * PAGE_SIZE)
            data = f.read(PAGE_SIZE)

        if len(data) != PAGE_SIZE:
            raise IOError("Incomplete page read")

        return data

def append_page(file_name, page_data):
    if len(page_data) != PAGE_SIZE:
        raise ValueError("Invalid page size")
    with open(file_name, 'ab') as f:
        f.write(page_data)

def write_page(file_name, page_number, page_data):
    if len(page_data) != PAGE_SIZE:
        raise ValueError("Invalid page size")

    size = os.path.getsize(file_name)
    last = size // PAGE_SIZE - 1

    if page_number < 0 or page_number > last:
        raise ValueError("Invalid page number")

    with open(file_name, 'r+b') as f:
        f.seek(page_number * PAGE_SIZE)
        f.write(page_data)
def new_empty_page_bytes():
    buf = bytearray(PAGE_SIZE)
    struct.pack_into('>H', buf, 4092, 0)
    struct.pack_into('>H', buf, 4094, 0)
    return bytes(buf)

def read_footer(page):
    slot = struct.unpack('>H', page[4092:4094])[0]
    offset = struct.unpack('>H', page[4094:4096])[0]
    return slot, offset

def slot_entry_pos(i):
    return PAGE_SIZE - 4 - (i + 1) * 4
