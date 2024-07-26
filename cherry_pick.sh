#!/usr/bin/bash
#
# Small helper script to cherry-pick a specific file
# to the stripped branch.
# This will take the most recent commit where <file>
# was edited, and cherry pick that to the stripped branch.
#

if [ $# -eq 0 ]; then
  echo "Please supply one or more file name(s) for cherry-picking"
  echo "them to the stripped branch"
fi

branch=stripped

# Ensure we are on main, this should probably
# not be there.
git checkout main

declare -a lines=($(git log --reverse --oneline --no-abbrev-commit -- $@ | awk '{print $1}'))

git checkout $branch

for hash in ${lines[@]}
do
  # Check if the commit has already been cherry-picked
  # to branch.
  # We search the commit log for the hash name.
  # In case users forget -x, this probably won't work.
  out=$(git log --oneline --grep=$hash $branch)
  # If there is no cherry-pick of the commit, the log command
  # will return an empty string. Hence we test the length of the
  # variable.
  if [ ${#out} -le 1 ]; then
    # We can't find it, so we should cherry-pick it ;)
    git cherry-pick -x $hash
  else
    echo "$hash already cherry-picked by: $out"
  fi
done

git checkout main
