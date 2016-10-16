#!/bin/sh

FILES=enron/*

for f in $FILES
do
  echo "Processing $f: $out"
  java -cp .:lib/javax.mail-1.5.6.jar:lib/mbox.jar ReadMbox $f | grep "Number of messages"
done
