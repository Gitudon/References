def load_lines_from_file(file_path) -> list:
    lines = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line == "\n":
                continue
            if line not in lines:
                lines.append(line)
    return lines


def write_lines_to_file(file_path, lines):
    with open(file_path, "w", encoding="utf-8") as file:
        header_done = False
        for line in lines:
            if line.startswith("## "):
                if header_done:
                    file.write("\n")
                else:
                    header_done = True
                file.write("\n")
            file.write(line)
            file.write("\n")


def remove_first_line_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines[1:])


def main():
    target_file = "references.md"
    lines = load_lines_from_file(target_file)
    write_lines_to_file(target_file, lines)
    remove_first_line_from_file(target_file)


if __name__ == "__main__":
    main()
