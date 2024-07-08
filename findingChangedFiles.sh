# Check if running in Jenkins environment
if [ "$JENKINS_ENV" == "true" ]; then
    # Set workspace path dynamically
    workspace="$WORKSPACE"
else
    # Local environment setup (replace with your local path)
    workspace="/Users/harsh.saini/Desktop/multi-module-project/parent"
fi

# Run git diff command and save output to changedFiles.txt
git diff --name-only remotes/origin/test main | sort -u > "$workspace/changedFiles.txt"
