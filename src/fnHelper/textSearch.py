import re

def countKeyword(searchBar, paragraph):
    match = re.findall(searchBar, paragraph)
    length = match.__len__()
    print(length)
    return length