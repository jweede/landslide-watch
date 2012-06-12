#!/usr/bin/env python
import subprocess, sys
import logging as l
from landslide import generator as landslide_gen


def watch(the_file):
	ret_code = 0
	cmd = "inotifywait -qq -e modify %s" % f

	while (ret_code==0):
		l.info("Generate %s", f)
		run(f)
		
		ret_code = subprocess.call(cmd, shell=True)
		l.debug("Change in %s. ret_code %d", f, ret_code)
	return ret_code

def run(the_file):
	landslide_gen.Generator(f).execute()

if __name__ == '__main__':
	f = sys.argv[1]
	l.basicConfig(level=l.INFO,format='[%(asctime)s]%(levelname)s: %(message)s')

	if watch(f) != 0:
		l.error( "inotify returned %d", ret_code )
	
	sys.exit(ret_code)
		
