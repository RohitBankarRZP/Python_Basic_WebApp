"""

A sample python script for downloading the current non-redundant lists from
the RNA 3D Hub (http://rna.bgsu.edu/rna3dhub).

Usage:
python download_nrlist.py   
save data in a file

"""

from email.mime import base
import urllib
from urllib import request


# nrlist are provided at 8 resolution cutoffs
resolutions = ['1.5A', '2.0A', '2.5A', '3.0A', '3.5A', '4.0A', '20.0A', 'all']

base_url = 'http://rna.bgsu.edu/rna3dhub/nrlist/download'

local_file="try.txt"

for resolution in resolutions:
    release = 'current' # can be replaced with a specific release id, e.g. 0.70
    url = '/'.join([base_url, release, resolution])
    try:
        nrdata = urllib.urlopen( url ).read()
        # nrdata now contains the string with data in csv format
        print "Release %s, resolution %s: download complete" % \
              (release, resolution)
    except:
        print "Release %s, resolution %s: download failed" % \
              (release, resolution)

request.urlretrieve(base_url,local_file)

