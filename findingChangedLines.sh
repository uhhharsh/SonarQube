# Replace these with the actual commit hashes or references
COMMIT1="HEAD"
COMMIT2="5545b356e441a869a0a365f32912319d211665ae"

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
                               ' > changedLines.txt
