{
  git diff --name-only HEAD 5545b356e441a869a0a365f32912319d211665ae
  git diff --cached --name-only HEAD 5545b356e441a869a0a365f32912319d211665ae
} | sort -u > /Users/harsh.saini/Desktop/multi-module-project/parent/changedFiles.txt
