#! /usr/bin/env python3

import subprocess
import re

def main():
    args = ("uptime")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    output = output.decode("utf-8").strip()
    pattern = re.compile("\d{2}:\d{2}:\d{2}\sup\s(\d+)\sdays.*")
    match = pattern.match(output)
    days = int(match.group(1))

    if (days % 365 == 0):
        print ("Happy Birthday!")
    else:
        print ("Sorry, today is not your birthday")

if __name__ == "__main__":
    main()
