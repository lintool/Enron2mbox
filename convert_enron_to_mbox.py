#!/usr/bin/env python

import mailbox
import sys
import email
import os
import glob
import shutil

def maildir2mailbox(maildirname, mboxfilename):
  # open the existing maildir and the target mbox file
  maildir = mailbox.Maildir(maildirname, email.message_from_file)
  mbox = mailbox.mbox(mboxfilename)

  # lock the mbox
  mbox.lock()

  # iterate over messages in the maildir and add to the mbox
  for msg in maildir:
    mbox.add(msg)

  # close and unlock
  mbox.close()
  maildir.close()


folders = []

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("maildir"):
  if files:
    folders.append(root)

for folder in folders:
  print("Processing " + folder)
  os.makedirs(folder + "/cur")
  os.makedirs(folder + "/new")
  for file in glob.glob(folder + "/[0-9]*."):
    shutil.move(file, folder + "/cur")

os.makedirs("enron")

for folder in folders:
  path = "enron/" + folder.replace("/", ".").replace("maildir", "enron")
  print("Writing " + folder + " -> " + path)
  maildir2mailbox(folder, path)
