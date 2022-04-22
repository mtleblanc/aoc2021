#!/usr/bin/python3
import argparse
import subprocess
import sys

SESSION = "53616c7465645f5f0861cf0650d0e8a76cd1c1f2b25fb39959376c07f9db7971717d6398bef8d295e652099c39ee9f54"  
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2021)
parser.add_argument('--day', type=int, default=3)
args = parser.parse_args()

cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session={}"'.format(
                args.year, args.day, SESSION)
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)
