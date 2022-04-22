#!/usr/bin/python3

import sys, getopt
from itertools import tee, islice

# Each time the sliding window moves, one new value is added and one drops off.
# The window's sum increases exactly when the added value is larger than the 
# dropped value.  So there is no need to calculate the sums, just compare the 
# new value.  Note that part 1 is equivalent to just having a window of size 1
def imperative(offset, stream):    
    prevVals = []
    increases = 0
    for line in stream:
        curVal = int(line)
        if len(prevVals) < offset:
            prevVals.append(curVal)
        else:
            if curVal > prevVals[0]:
                increases += 1
            prevVals = prevVals[1:]
            prevVals.append(curVal)
    return increases

# More functional/pythonic, zip the input with itself delayed by windowsize
# to get our comparisons lined up, then just count
def pythonic(offset, stream):
    values, nextValues = tee((int(l) for l in stream), 2)
    nextValues = islice(nextValues, offset, None)
    return sum(1 for a,b in zip(values, nextValues) if a < b)

def printHelp():
    print(f'Usage {sys.argv[0]} [options]')
    print("Options: ")
    print(" -w[N]       : Size of sliding window, default 1")
    print(" -i[fname]   : File to read input from, default stdin")

def args(argv):
    offset = 1
    inputStream = sys.stdin
    try:
        opts, args = getopt.getopt(argv,"hw:i:",["window=", "input="])
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
    if len(args) > 0:
        printHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            printHelp()
            sys.exit()
        elif opt in ("-w", "--window"):
            offset = int(arg)
        elif opt in ("-i", "--input"):
            inputStream = open(arg, "r")
    return (offset, inputStream)

if __name__ == "__main__":
    offset, inputStream = args(sys.argv[1:])
    print(pythonic(offset, inputStream))
    inputStream.close()
