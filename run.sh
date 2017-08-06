#!/bin/bash
# Use this if you want guaranteed working behavior
# This runs the latest version on master
# If you want to test stuff you're developing run the python script directly

exit_command=""

if [ -n "$(git status --porcelain)" ]; then
  git stash
  exit_command+="git stash pop; "
fi

branch=`git branch | grep '*' | sed 's/* //'`
if [ "$branch" != "master" ]; then
  git checkout master
  exit_command+="git checkout $branch"
fi

if [ -n "$exit_command" ]; then
  trap "$exit_command" EXIT
fi

# run this in the background so it can finish immediately and undo git changes
src/update_sheet.py &

