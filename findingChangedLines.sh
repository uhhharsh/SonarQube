# Replace these with the actual commit hashes or references
COMMIT1="remotes/origin/test"
COMMIT2="main"

# Determine the environment (local or Jenkins)
if [ -n "$JENKINS_ENV" ]; then
  # Running in Jenkins
  OUTPUT_PATH="$WORKSPACE/changedLines.txt"
else
  # Running locally
  OUTPUT_PATH="/Users/harsh.saini/Desktop/multi-module-project/parent/changedLines.txt"
fi

# Get the changed lines between two commits, filter for added lines, and extract line numbers
git diff -U0 $COMMIT1 $COMMIT2 | awk '
  /^diff --git/ {
    file = ""
  }
  /^---/ {
    if ($2 != "/dev/null") {
      file = substr($2, 3)
    }
  }
  /^@@ -/ {
    if (file) {
      split($0, a, " ")
      split(a[2], b, ",")
      start_line = substr(b[1], 2)
      num_lines = b[2]
      printf "%s -> %d, +%d\n", file, start_line, num_lines
    }
  }
' > "$OUTPUT_PATH"

echo "Changed lines have been written to $OUTPUT_PATH"
