#!/bin/bash

FILES=enron/*

for f in $FILES
do
  echo -n "Processing $f: "
  java -cp .:lib/javax.mail-1.5.6.jar:lib/mbox.jar ReadMbox $f | grep "Number of messages" | cut -d':' -f 2 | sed -e 's/^[[:space:]]*//'
done
