#!/usr/bin/python
import os
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("user_hash", help="File containing username:hash combos")
parser.add_argument("hash_password", help="File containing hash:password combos")
parser.add_argument("-sb", "--show_blank", help="Add as option if you want to display users who do not have a hash in the hash:password file (uncracked passwords)", action="store_true")

args = parser.parse_args()

def combineInput():
  userHashes = {}
  crackedPasswords = {}

  with open(args.user_hash, 'r') as f:
    for line in f:
      try:
        splitLine = line.split(":")
        userHashes[splitLine[0]] = splitLine[1].rstrip()
      except:
        pass
  with open(args.hash_password, 'r') as f:
    for line in f:
      try:
        splitLine = line.split(":")
        crackedPasswords[splitLine[0]] = splitLine[1].rstrip()
      except:
        pass

  for user in userHashes:
    value = crackedPasswords.get(userHashes[user], "")
    if not value:
      if args.show_blank:
        print user, ":"
      else:
        pass
    else:
      print user, ":", value

#MAIN
combineInput()
