#!/usr/bin/env python3

# Snail Username Generator
# By Kyle 😎

import argparse

# set up the argument parser so we can just use this from the command line...
parser = argparse.ArgumentParser()
#parser.add_argument("-i", "--interactive", help="run in interactive mode", action="store_true")
parser.add_argument("name", default="lolcat")
parser.add_argument("number", default="420")
args = parser.parse_args()

print("sn" + args.name[1:] + args.number)
