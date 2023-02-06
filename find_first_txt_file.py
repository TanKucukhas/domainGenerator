import os


def find_first_txt_file(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                return os.path.join(root, file)
    return None


file_path = find_first_txt_file("./input")

if file_path:
    print("The first txt file found:", file_path)
else:
    print("No txt file found in the given folder.")
