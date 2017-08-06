#!/bin/bash

exit_command=""

if [ -n "$(git status --porcelain)" ]; then
  git stash
  exit_command+="git stash pop; "
fi

branch=`git branch | grep '*' | sed 's/* //'`
echo $branch
if [ "$branch" != "master" ]; then
  git checkout master
  exit_command+="git checkout $branch"
fi

if [ -n "$exit_command" ]; then
  trap "$exit_command" EXIT
fi

src/update_sheet.py

