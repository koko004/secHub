#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__ = "Josh"

import os
#import pip

content = """
#!/bin/bash

cd /usr/share/sechub
python2 sechub.py "$@"
"""

def main():
	if os.name != "nt":
		if os.getuid() == 0:
			os.system("git clone https://github.com/koko004/secHub.git /usr/share/sechub")
			
			file = open("/usr/bin/sechub", "w")
			file.write(content)
			file.close()
			
			os.system("chmod +x /usr/bin/sechub")

			print "\n\n[+] Installation finished, type 'sechub' to use program!"
		else:
			print "Run as root!"
	else:
		print "This script doesn't work on Windows!"

if __name__ == "__main__":
	main()
