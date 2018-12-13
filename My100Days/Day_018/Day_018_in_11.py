"""
Turn the following unix pipeline into Python code using generators
$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""

# consider doing this with os.path and with pathlib
import fnmatch
import os
import re
from pathlib import Path

here = os.path.abspath(os.path.dirname(__file__))
top = os.path.abspath(os.path.join(here, os.pardir))
pattern = re.compile(r"(^import\s+)(\S+$)")

# lets do this a few different ways
def gen_files1(pat=None):
    if pat == None:
        pat = re.compile(r'\S*py\Z')
    walk = os.walk(top, topdown=True, onerror=None, followlinks=False)
    for dirpath, dirnames, filenames in walk:
        for filename in filenames: 
            match = re.search(pat, filename)
            if match:
                yield os.path.join(dirpath, filename)

print(len(list(gen_files1())))

def gen_files2(pat=None):
    if pat == None:
        pat = '*.py'
    walk = os.walk(top, topdown=True, onerror=None, followlinks=False)
    for dirpath, dirnames, filenames in walk:
        for filename in filenames: 
            if fnmatch.fnmatch(filename, pat):
                yield os.path.join(dirpath, filename)

def gen_files3(pat=None):
    if pat == None:
        pat = '**/*.py'
    top_path = Path(top)
    for file in top_path.glob(pat):
        yield str(file)

def gen_lines(files):
    for filename in files:
        with open(filename, 'r') as f:
            for line in f:
                yield line

files = gen_files1()
lines = gen_lines(files)

def gen_grep(lines, pattern):
    for line in lines:
        match = re.search(pattern, line)
        if match:
            yield match.group(2)

grepped = gen_grep(lines, pattern)

def gen_count(grepped):
    pass


for item in grepped:


if __name__ == "__main__":
    # call the generators, passing one to the other
    #files = gen_files1()
    #lines = gen_lines(files)
    #grep = gen_grep(lines, pattern)
    #print(list(grep))
    # etc

