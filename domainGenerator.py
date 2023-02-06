import find_first_txt_file
from filter_strings import filter_strings

line_count = 499
domain_extensions = [".co", ".us", ".com", ".is"]
minimum_characters = 0
maximum_characters = 10
unwanted_characters_or_words = [
    "ğ",
    "ç",
    "ş",
    "ü",
    "ö",
    "ı",
    "/",
    "*",
    "?",
    "<",
    ">",
    "â",
]

lines_array = []

file_name = find_first_txt_file.find_first_txt_file("./input")


def generate_domain_names():
    with open(file_name, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            line = "".join(line.split())
            for x, word in enumerate(domain_extensions):
                if minimum_characters <= len(line) <= maximum_characters:
                    new_line = line + word
                    lines_array.append(new_line)


def split_into_files(strings, limit, file_prefix):
    chunks = [strings[i : i + limit] for i in range(0, len(strings), limit)]
    for i, chunk in enumerate(chunks):
        with open(f"{file_prefix}_{i}.txt", "w") as f:
            for string in chunk:
                f.write(string + "\n")


generate_domain_names()

filtered = filter_strings(
    lines_array,
    unwanted_characters_or_words,
)

split_into_files(filtered, line_count, file_name)
