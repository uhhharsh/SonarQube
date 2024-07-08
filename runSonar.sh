#!/bin/bash

# Step 1: Python script to filter and generate SonarQube inclusions
generate_sonar_inclusions() {
    python3 /Users/harsh.saini/Desktop/multi-module-project/parent/settingInclusions.py
}

# Step 2: Run the SonarQube analysis using Gradle
run_sonar_analysis() {
    inclusions=$(generate_sonar_inclusions)
    echo $inclusions

    if [ -n "$inclusions" ]; then
        ./gradlew sonarqube \
        -Dsonar.inclusions="${inclusions}"
    else
        echo "No .java files found to include."
    fi
}

# Execute the SonarQube analysis
run_sonar_analysis
