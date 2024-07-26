#!/bin/bash
#
# Script which takes an optional argument
# being the directory. Defaults to the current directory.
# Then all files will be added through a single commit.
# It will recurse through each folder.
# For each folder it will first add the README.md file,
# then any subsequent files.
#
root=$(git rev-parse --show-toplevel)/

_dir=$(pwd)
if [ $# -gt 0 ]; then
  _dir=$1
  shift
fi

echo "Will add all files, and sub-directory files in directory:"
echo "  $_dir"

function get_root_path {
  local f=$(realpath $1)
  shift
  f=${f//${root}/}
  printf "%s" "$f"
}

function add_directory {
  local d=$1
  shift

  pushd $d

  for f in ./* ; do
    case $f in
      .|..)
        continue
        ;;
    esac

    if [ -f $f ]; then
      git add $f
      f=$(get_root_path $f)
      git commit -m "Adding file: ${f}"
    elif [ -d $f ]; then
      add_directory $f
    fi
  done

  popd

}

add_directory $_dir
