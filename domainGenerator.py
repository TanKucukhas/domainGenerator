import find_first_txt_file;

# file_name = input("Enter the name of the file to split: ")
file_name = find_first_txt_file.find_first_txt_file('./input')

# line_count = int(input("Enter the number of lines per file: "))
line_count= 2000
# doman_names = input("Enter a comma-separated list of strings to add: ").split(',')
doman_names = ['.co','.us', '.com']
# filename
out_file_name = 'split'


lines_array = []

def generate_domain_names():
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            line = "".join(line.split())
            for x, word in enumerate(doman_names):
                new_line = line + word
                lines_array.append(new_line)


def split_into_files(strings, limit, file_prefix):
    chunks = [strings[i:i+limit] for i in range(0, len(strings), limit)]
    for i, chunk in enumerate(chunks):
        with open(f"{file_prefix}_{i}.txt", "w") as f:
            for string in chunk:
                f.write(string + "\n")

generate_domain_names()

split_into_files(lines_array, line_count, file_name)