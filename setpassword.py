#!/usr/bin/python

import os, sys, subprocess
from passlib.hash import md5_crypt

if len(sys.argv) == 3:
	username = sys.argv[1]
	hash = md5_crypt.encrypt(sys.argv[2])
	
	subprocess.call([
		'ansible-playbook',
		'-i',
		'production',
		'setpassword.yml',
		'--extra-vars=username=%s password=%s' % (username, hash)
	])


