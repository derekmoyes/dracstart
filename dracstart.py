#!/usr/bin/env python
"""
Use this script to easily open downloaded jnlp files from Dell. Typically, the
  file names aren't in a useful format, security settings won't easily allow
  you to easily start by double-clicking, etc.

You'll probably want to move this script to a location where it's easily
  executable, like maybe ~/bin. Don't forget to chown it +x if you want to.

Also check out the adjustable variables at the top of the script, things like
  the location to your Downloads folder, etc.

Once that's done, simply download a jnlp file into your Downloads folder, then
  run this script. You don't need to specify any parameters, as long as the
  jnlp is the newest file in your Downloads folder, it'll find it.

Tested mostly with iDRAC6 files, as you can upgrade iDRAC7 to allow HTML5
  console access. I highly recommend you do that, if you're able.

Written for Python 2.7, as that's the default on my Mac.

---
Copyright 2021 derek.moyes @ gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. https://opensource.org/licenses/MIT
"""

import argparse
import textwrap
import glob
import os
from datetime import datetime
from time import sleep


# Adjust these variables for your environment.
DebugString        = "==> DEBUG:"
DownloadsPath      = "/Users/dmoyes/Downloads/"
FileExt            = "jnlp"
Snippet            = "drac"
JavaRunner         = "/usr/bin/javaws"
DeleteFileAfterUse = 1
DeleteAfterSeconds = 15


# Setup command-line arguments.
verbose = False
debug   = False

parser = argparse.ArgumentParser(
        prog='dracstart',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__)
parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help="Print verbose information")
parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help="Print additional debug information")
args = parser.parse_args()

if args.verbose:
    verbose = True
    print("Setting verbose to %s." % verbose)

if args.debug:
    debug = True
    print("Setting debug to %s." % debug)


# Begin.
# Locate the latest FileExt file in DownloadsPath.
if verbose:
    print("Checking for new %s files in %s." % (FileExt, DownloadsPath))

list_of_files = glob.glob(DownloadsPath + '*' + FileExt)

if not list_of_files:
    if verbose:
        print("Specific %s file not found, checking all files in %s." 
              % (FileExt, DownloadsPath))
    list_of_files = glob.glob(DownloadsPath + '*')
    try:
        latest_file = max(list_of_files, key=os.path.getctime)
    except ValueError as ve:
        raise SystemExit("Sorry, I don't see any files in %s." % DownloadsPath)
else:
    try:
        latest_file = max(list_of_files, key=os.path.getctime)
    except ValueError as ve:
        raise SystemExit("Sorry, I don't see any files in %s." % DownloadsPath)

if verbose:
    print("Found newest file %s." % (latest_file))


# Validate that it is a DRAC config file.
try:
    validate = open(latest_file, 'r').readlines()
except IOError as err:
    print("Error: %s" % err)

matches = []
for word in validate:
    if Snippet in word.lower():
        matches.append(word)
if debug:
    print("%s List of read lines matching %s: " % (DebugString, Snippet))
    print("%s %s" % (DebugString, matches))

if not matches:
    raise SystemExit("Sorry, the newest file %s doesn't seem to be of %s type."
                     % (latest_file, FileExt))


# Rename it to something we can use.
dt = datetime.now().strftime('%Y%m%d%M%S')
new_file_name = DownloadsPath + Snippet + dt + "." + FileExt
os.rename(latest_file, new_file_name)
if verbose:
    print("Renamed to: %s" % (new_file_name))


# Run it with JavaRunner.
builtcommand = JavaRunner + " " + new_file_name
print("Starting: %s" % builtcommand)
os.system(builtcommand)


# Optionally move the file to trash after a specified period.
if DeleteFileAfterUse:
    print("Waiting %s seconds to remove %s..."
          % (DeleteAfterSeconds, new_file_name))
    sleep(DeleteAfterSeconds)
    os.remove(new_file_name)
    print("Removed.")

