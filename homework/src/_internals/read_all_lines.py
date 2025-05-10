import os


def read_all_lines(input_folder):

    lines = []

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            lines.extend(file.readlines())

    print(lines)

    return lines
