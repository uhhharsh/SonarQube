import subprocess
import re

def run_git_diff():
    print("Running git diff command...")
    result = subprocess.run(['git', 'diff', '-U0', 'remotes/origin/main', 'remotes/origin/test', '--', '*.java'], capture_output=True, text=True)
    print("Git diff command output:\n", result.stdout)
    return result.stdout

def parse_diff_output(diff_output):
    print("Parsing diff output...")
    file_changes = {}
    current_file = None
    lines_added_pattern = re.compile(r'^@@ -\d+(,\d+)? \+(\d+)(,\d+)? @@')

    for line in diff_output.splitlines():
        if line.startswith('diff --git'):
            parts = line.split(' ')
            current_file = parts[2][2:]
            file_changes[current_file] = []
            print(f"Found file: {current_file}")
        elif line.startswith('@@'):
            match = lines_added_pattern.match(line)
            if match:
                start_line = int(match.group(2))
                num_lines = int(match.group(3)[1:]) if match.group(3) else 1
                if num_lines > 0:
                    end_line = start_line + num_lines - 1
                    file_changes[current_file].append([start_line, end_line])
                    print(f"Added range in {current_file}: [{start_line}, {end_line}]")

    print("Parsed file changes:\n", file_changes)
    return file_changes

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    
def add_sonar_comments(file_changes):
    print(f"Adding Sonar comments to {file_changes}...")
    # Iterate through each file and its changes
    for file_path, changes in file_changes.items():
        # Read the file into lines
        with open(file_path, 'r') as file:
            lines = file.readlines()

        line_count = count_lines_in_file(file_path)

        # Print each line with its line number
        for line_num, line in enumerate(lines, start=1):
            # print(f"Line {line_num}: {line.strip()}")
            #checking if line 1 is in any range
            comment_at_line1 = True
            if(line_num == 1 and comment_at_line1):
                lines[0] = lines[0].rstrip() + " //START-NOSONAR\n"

            for change in changes:
                start, end = change
                if(start <= 1 <= end):
                    comment_at_line1 = False

                if line_num == start:
                    print(f"Line {line_num}: {line.strip()}")
                    if (start-1) > 0:
                        # Add // END-NOSONAR to the end of the previous line
                        lines[start-2] = lines[start-2].rstrip() + " //END-NOSONAR\n"
                        print(f'comment //END-NOSONAR added at line number {start-1}')
                if line_num == end:
                    print(f"Line {line_num}: {line.strip()}")
                    if end < line_count:
                        # Add // END-NOSONAR to the end of the previous line
                        lines[end] = lines[end].rstrip() + " //START-NOSONAR\n"
                        print(f'comment //START-NOSONAR added at line number {end+1}')

        # Write the modified lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)

        print(f"Sonar comments added to {file_path}.")
        print()  # Empty line for readability

def format_output(file_changes):
    print("Formatting output...")
    for file, lines in file_changes.items():
        line_ranges = []
        for i in range(len(lines)):
            if i == 0 or lines[i] != lines[i-1] + 1:
                line_ranges.append([lines[i], lines[i]])
            else:
                line_ranges[-1][1] = lines[i]

        formatted_ranges = [f'[{start},{end}]' if start != end else f'[{start}]' for start, end in line_ranges]
        print(f'{file}: {formatted_ranges}')


if __name__ == "__main__":
    diff_output = run_git_diff()
    file_changes = parse_diff_output(diff_output)
    format_output(file_changes)
    add_sonar_comments(file_changes)
