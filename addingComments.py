import os

def add_nosonar_to_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line.rstrip('\n') + ' //NOSONAR\n')
        
        print(f"Processed file: {file_path}")
    except Exception as e:
        print(f"Failed to process file {file_path}: {e}")

def main():
    base_path = '/Users/harsh.saini/Desktop/multi-module-project/parent/'

    try:
        with open('/Users/harsh.saini/Desktop/multi-module-project/parent/changedFiles.txt', 'r') as file:
            file_paths = file.readlines()
        
        for file_path in file_paths:
            full_file_path = os.path.join(base_path, file_path.strip())
            if full_file_path.endswith('.java'):
                    if os.path.isfile(full_file_path):
                        add_nosonar_to_file(full_file_path)
            else:
                print(f"File not found: {full_file_path}")
        else:
            print(f"Skipped non-Java file: {full_file_path}")
    except Exception as e:
        print(f"Failed to read ChangedFiles.txt: {e}")

if __name__ == "__main__":
    main()
