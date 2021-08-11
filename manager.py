# Yes I know, system() is bad, but I'm currently working on a solution that uses execve.
# It will release soon.
import os
import sys
v = "1.2.1"

def installPackage(p):
	strP = str(p)
	print(f"Installing package: {strP}")
	os.system(f'git clone https://github.com/Bear-Package-Management/{p} packages/{p}')

def removePackage(p):
	print(f"Removing {p} from Bear-Shell System")
	os.system(f'sudo rm -r {p}')

def version():
	print(f"Current bpm version: {v}")

def list():
	dir = "packages"
	dirFound = os.path.isdir(dir)
	if dirFound:
		path = "packages"
		packs = sum([len(folder) for r, d, folder in os.walk(path)])
		print(f"There are currently {packs} installed.")
	else:
		print("No packages installed!")