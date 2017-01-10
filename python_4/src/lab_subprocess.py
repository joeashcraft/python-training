#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_subprocess` -- subprocess module
============================================

LAB subprocess Learning Objective: Familiarization with subprocess

::

 a. Use the subprocess run function to run "ls -l" and print the output.

 b. Do the same as a), but don't print anything to the screen.

 c. Do the same as a), but run the command "/bogus/command". What happens?

 d. Use subprocess Popen to run "du -h" and output stdout to a pipe. Read the pipe
    and print the output.

 e. Create a new function commander() which takes any number of commands to execute
    (as strings) on the arg list, then runs them sequentially printing stdout.

"""
import subprocess

# PART A
subprocess.call(["ls", "-l"])

# PART B
subprocess.call(["ls", "-l"], stdout=subprocess.DEVNULL)

# PART C
# subprocess.call(["/bogus/command"])
# FileNotFoundError

# PART D
part_d = subprocess.Popen(["du", "-h"], stdout=subprocess.PIPE)
print(part_d.stdout.read().decode())

# PART E


def commander(*args):
    for c in args:
        print(subprocess.check_output([c]).decode())
