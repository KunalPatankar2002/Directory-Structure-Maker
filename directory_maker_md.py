import os

def generate_md_structure(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        generate_md(directory, f, 0)


def generate_md(directory, f, depth):
    files = sorted(os.listdir(directory))
    for i, file in enumerate(files):
        if file.startswith('.'):
            continue
        is_last = i == len(files) - 1
        prefix = "└── " if is_last else "├── "
        f.write("|    " * depth + prefix + file + "\n")
        if os.path.isdir(os.path.join(directory, file)):
            generate_md(os.path.join(directory, file), f, depth + 1)


directory_path = "PATH TO DIRECTORY"
output_file_path = "directory_structure.md"
with open(output_file_path, 'w') as f:
    f.write("```markdown\n")
generate_md_structure(directory_path, output_file_path)
with open(output_file_path, 'a') as f:
    f.write("```")
print(f"Directory structure written to {output_file_path}")
