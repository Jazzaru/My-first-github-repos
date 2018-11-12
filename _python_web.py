"""
Develeper(s): JHL(Jeremy)
FROM: jeremyables42@yahoo.com
_Tested in Windows 10

"""

import os
import time
import webbrowser

def main(url1):
    print "opening google from python!"
    url = url1
    webbrowser.open(url)
main("www.google.com")
