# dracstart
## Easily open downloaded jnlp files from Dell.

usage: dracstart [-h]

optional arguments:
  -h, --help  show this help message and exit

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
==========
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
