import os


def get_files_in_path(path, extension="pdf"):
    files = []
    for file in os.listdir(path):
        if file.endswith(extension):
            files.append(file)

    return files


def read_txt(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return text
