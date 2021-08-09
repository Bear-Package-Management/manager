# Yes I know, system() is bad, but I'm currently working on a solution that uses execve.
# It will release soon.
import os
import sys
v = "1.1.0"

def installPackage(p):
	strP = str(p)
	print(f"Installing package: {strP}")
	os.system(f'git clone https://github.com/Bear-Package-Management/{p} {p}')

def removePackage(p):
	print(f"Removing {p} from Bear-Shell System")
	os.system(f'sudo rm -r {p}')

def version():
	print(f"Current bpm version: {v}")