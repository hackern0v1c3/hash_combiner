#!/usr/bin/python
import os
import sys

def print_usage():
	print "USAGE: "+sys.argv[0]+" {path to file containing Username:Hash} {path to file containing Hash:Password}"
	print "Example: "+sys.argv[0]+" users_with_hashes.txt cracked_hashes.txt"

def combineInput():
  userHashes = {}
  crackedPasswords = {}

  with open(sys.argv[1], 'r') as f:
    for line in f:
      splitLine = line.split(":")
      userHashes[splitLine[0]] = splitLine[1].rstrip()

  with open(sys.argv[2], 'r') as f:
    for line in f:
      splitLine = line.split(":")
      crackedPasswords[splitLine[0]] = splitLine[1].rstrip()

  for user in userHashes:
    value = crackedPasswords.get(userHashes[user], "")
    print user, ":", value

#MAIN
if len(sys.argv) != 3:
	print_usage()
	sys.exit()

if os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]):
	combineInput()
else:
	print "Invalid file"
