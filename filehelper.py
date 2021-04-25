import os

cd = os.path.dirname(os.path.realpath(__file__))


def open_file_cd(filename):
    filepath = cd + "/" + filename
    file = open(filepath)
    return file
