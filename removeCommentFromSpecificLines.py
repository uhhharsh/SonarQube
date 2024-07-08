import os
import re

def remove_nosonar_from_specific_lines(file_path, line_numbers):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        for line_num, line_count in line_numbers:
            for i in range(line_count):
                if line_num - 1 + i < len(lines) and '//NOSONAR' in lines[line_num - 1 + i]:
                    lines[line_num - 1 + i] = lines[line_num - 1 + i].replace('//NOSONAR', '').rstrip() + '\n'
        
        with open(file_path, 'w') as file:
            file.writelines(lines)
        
        print(f"Processed file: {file_path}")
    except Exception as e:
        print(f"Failed to process file {file_path}: {e}")

def parse_changed_lines(file_path):
    files_to_process = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = re.match(r"(.+) -> (\d+), \+(\d+)", line.strip())
                if match:
                    relative_path = match.group(1).strip()
                    line_num = int(match.group(2).strip())
                    line_count = int(match.group(3).strip())
                    if relative_path.endswith('.java'):
                        if relative_path not in files_to_process:
                            files_to_process[relative_path] = []
                        files_to_process[relative_path].append((line_num, line_count))
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")
    return files_to_process

def main():
    is_jenkins = os.getenv('JENKINS_ENV', 'false') == 'true'
    if is_jenkins:
        base_path = os.getenv('WORKSPACE', '.')
    else:
        # Local environment setup (replace with your local path)
        base_path = '/Users/harsh.saini/Desktop/multi-module-project/parent/'

    changed_lines_file = os.path.join(base_path, 'changedLines.txt')
    
    files_to_process = parse_changed_lines(changed_lines_file)
    
    for relative_path, line_numbers in files_to_process.items():
        full_file_path = os.path.join(base_path, relative_path)
        if os.path.isfile(full_file_path):
            remove_nosonar_from_specific_lines(full_file_path, line_numbers)
        else:
            print(f"File not found: {full_file_path}")

if __name__ == "__main__":
    main()
