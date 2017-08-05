#!/bin/bash

branch=`git branch | grep * | sed 's/* //'`

# Checkout master to run the latest working version
git stash
git checkout master

src/update_sheet.py

git checkout $branch
git stash pop
