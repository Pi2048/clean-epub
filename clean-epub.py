#!/usr/bin/python3

import os
import sys, getopt
import shutil
import random
from subprocess import Popen

# Every book was written on New Year's day of 2020
TIMESTAMP = "202001010000"

if __name__ == "__main__":
    inputfile = ''
    outputfile = ''
    if len(sys.argv) < 2:
        print("clean-epub.py -i <inputfile> [-o <outputfile>]")
        sys.exit(2)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
    except getopt.GetoptError:
        print("clean-epub.py -i <inputfile> [-o <outputfile>]")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("clean-epub.py -i <inputfile> [-o <outputfile>]")
            sys.exit()
        elif opt == "-i":
            inputfile = arg
        elif opt == "-o":
            outputfile = arg
    # Create temporary directory
    cwd = os.getcwd()
    tempdirname = "/tmp/tmp-epub-{}".format(random.randint(1000000,9999999))
    os.mkdir(tempdirname)
    # Unpack epub into temp dir
    process = Popen(['unzip', inputfile, '-d', tempdirname])
    process.wait()
    # Update timestamps
    os.chdir(tempdirname)
    process = Popen(['find', '.', '-exec', 'touch', '-t', TIMESTAMP, '{}', '+'])
    process.wait()
    # Create output epub-zip
    tempfilename = "my-clean-{}.epub".format(random.randint(1000000,9999999))
    process = Popen(['zip', '-X', '-r', tempfilename, '.', '-i', '*'])
    process.wait()
    os.chdir(cwd)
    if outputfile != '':
        os.rename(f"{tempdirname}/{tempfilename}", outputfile)
    else:
        os.rename(f"{tempdirname}/{tempfilename}", f"{cwd}/{tempfilename}")
    # Remove temporary directory
    shutil.rmtree(tempdirname)
