#!/bin/sh

shopt -s nullglob

# http://stackoverflow.com/questions/15216370/how-to-count-number-of-files-in-each-directory
find maildir -type d -print0 | while read -d '' -r dir; do
  files=("$dir"/[0-9]*)
  printf "%d messages: %s\n" "${#files[@]}" "$dir"
done

