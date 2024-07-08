def filter_java_files_from_file(file_path):
    included_files = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and ' -> ' in line:
                    # Split the line into filename and line information
                    parts = line.split(' -> ')
                    filename = parts[0].strip()
                    line_info = parts[1].strip().split(', ')
                    
                    # Extract line_number and line_count
                    line_number = int(line_info[0].strip())
                    line_count = int(line_info[1].strip().split(' ')[0])  # Extract line_count
                    
                    # Check if it's a Java file with line_count > 0
                    if filename.endswith('.java') and line_count > 0:
                        # Ensure file name is not repeated
                        if filename not in included_files:
                            included_files.append(filename)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    
    return ','.join(included_files)

# Example usage:
file_path = '/Users/harsh.saini/Desktop/multi-module-project/parent/changedLines.txt'
included_files = filter_java_files_from_file(file_path)

# Print the included files
print(included_files)
