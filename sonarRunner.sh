#!/bin/bash

# Function to run git diff command
run_git_diff() {
    source_branch=hardcodeRemoval
    target_branch=main

    if [ -z "$source_branch" ] || [ -z "$target_branch" ]; then
        echo "Environment variables CI_MERGE_REQUEST_SOURCE_BRANCH_NAME and CI_MERGE_REQUEST_TARGET_BRANCH_NAME must be set"
        exit 1
    fi

    echo "Running git diff command..."
    git diff -U0 "remotes/origin/$target_branch" "remotes/origin/$source_branch" -- '*.java'
}

# Function to run git diff --name-only command and extract file names
run_git_diff_for_changed_files_names() {
    source_branch=hardcodeRemoval
    target_branch=main

    if [ -z "$source_branch" ] || [ -z "$target_branch" ]; then
        echo "Environment variables CI_MERGE_REQUEST_SOURCE_BRANCH_NAME and CI_MERGE_REQUEST_TARGET_BRANCH_NAME must be set"
        exit 1
    fi

    echo "Running git diff --name-only command..."
    git diff --name-only "remotes/origin/$target_branch" "remotes/origin/$source_branch" -- '*.java'
}

# Function to parse git diff output for file changes
parse_diff_output() {
    diff_output="$1"
    echo "Parsing diff output..."
    file_paths=()

    while IFS= read -r line; do
        if [[ $line == "diff --git"* ]]; then
            current_file=$(echo "$line" | awk '{ print $3 }' | sed 's/^a\///')
            file_paths+=("$current_file")
            echo "Found file: $current_file"
        elif [[ $line == "@@"* ]]; then
            lines_added=$(echo "$line" | grep -oP '(?<=\+)(\d+)')
            num_lines=$(echo "$line" | grep -oP '(?<=\+\d+,)(\d+)' || echo "1")
            end_line=$(( lines_added + num_lines - 1 ))
            echo "Added range in $current_file: [$lines_added, $end_line]"
            # Optionally, you can store ranges in a separate array if needed
        fi
    done <<< "$diff_output"

    echo "Parsed file paths:"
    printf '%s\n' "${file_paths[@]}"
}

# Function to count lines in a file
count_lines_in_file() {
    file_path="$1"
    if [ ! -f "$file_path" ]; then
        echo "Error: File '$file_path' not found."
        return 1
    fi

    line_count=$(wc -l < "$file_path")
    echo "$line_count"
}

# Function to add SonarQube comments to files
add_sonar_comments() {
    file_changes="$1"
    echo "Adding Sonar comments..."

    for file_path in "${file_changes[@]}"; do
        line_count=$(count_lines_in_file "$file_path")

        if [ "$line_count" -eq 0 ]; then
            echo "Error: File '$file_path' is empty or not found."
            continue
        fi

        echo "File: $file_path"

        # Check if the first line needs a comment
        if [ "$file_path" = "0" ]; then
            sed -i '1s/$/ //START-NOSCAN/' "$file_path"
            echo "  Added //START-NOSCAN at line 1"
        fi

        # Add Sonar comments based on changes (logic here may need adjustment)
        # Example logic to add comments
        # sed -i '2s/$/ //END-NOSCAN/' "$file_path"
        # sed -i '3s/$/ //START-NOSCAN/' "$file_path"

        echo "  Sonar comments added to $file_path."
    done
}

# Function to run Gradle SonarQube analysis
run_gradle_sonar() {
    paths="$1"
    project_key="$PROJECT_KEY"
    sonar_host_url="$SONARQUBE_URL"
    sonar_user="$SONARQUBE_USER_ID"
    sonar_pwd="$SONARQUBE_USER_PWD"

    echo "Running Gradle SonarQube analysis..."
    command="./gradlew sonar --info"
    echo "Running command: $command"

    if ! eval "$command"; then
        echo "Error running Gradle command."
        exit 1
    fi
}

# Main script flow
main() {
    diff_output=$(run_git_diff)
    echo "$diff_output"
    file_paths=$(run_git_diff_for_changed_files_names)
    echo "$diff_output"
#    parse_diff_output "$diff_output"
#    add_sonar_comments "$file_paths"
#    run_gradle_sonar "$file_paths"
}

# Invoke main function
main
