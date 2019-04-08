#!/bin/bash

git status

read -r -p 'Commit message: ' desc  # prompt user for commit message

git add .

git commit -m "$desc"               # commit with message

git push