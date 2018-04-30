#-*- coding: utf-8 -*-
import subprocess
import os
import itertools
import getpass
import time


def clear():
	subprocess.call(["cmd.exe","/c","cls"])

def ls():
	dirlist = os.listdir('.')
	count = 0
	while count <= len(dirlist) - 1:
		if count + 4 <= len(dirlist) -1:
			print("\n {}  {}  {}  {}  {} \n".format(dirlist[count], dirlist[count + 1], dirlist[count + 2], dirlist[count + 3], dirlist[count + 4]))
			count += 4
		elif count + 3 <= len(dirlist) -1:
			print("\n {}  {}  {}  {} \n".format(dirlist[count], dirlist[count + 1], dirlist[count + 2], dirlist[count + 3]))
			count += 3
		elif count + 2 <= len(dirlist) -1:
			print("\n {}  {}  {} \n".format(dirlist[count], dirlist[count+1], dirlist[count+2]))
			count += 2
		elif count + 1 <= len(dirlist) - 1:
			print("\n {}  {} \n".format(dirlist[count], dirlist[count + 1]))
			count += 1
		elif count == len(dirlist) - 1:
			print("\n {} \n".format(dirlist[count]))
			count += 1
def ls_flags(cmd):
	lscount = 2
	dirlist = os.listdir('.')
	for char in cmd[2:]:
		if char == "-":
			for c in cmd[lscount:]:
				if c == 'l':
					for file in dirlist:
						(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
						print("{} {} {} {}".format(getpass.getuser(),time.ctime(size), time.ctime(mtime),file))

			

def mkdir(mdir):
	try:
	    os.mkdir(mdir)
	except: 
		print("ese directorio ya existe") 
def cd(cdir): 
	try:
		os.chdir(cdir)
	except:
		print("el sistema no puede encontrar la ruta")
def rm(path):
	try:
		os.remove(path)
	except:
		print("[ERROR]: '{}' no encontrado".format(path))
def head(textfile):
    end = ''
    try:
        with open(textfile) as data:
            text_iterator = itertools.islice(data, 0, 10)
            for element in text_iterator:
                print(element, end)
    except:
        print("[ERROR] El archivo no existe o no puede ser abierto")

def tail(textfile):
    end = ''
    try:
        with open(textfile) as data:
        	all_lines = itertools.islice(data, 0, None)
        	num_lines = sum(1 for _ in all_lines)
        	data.seek(0)
        	line_begin = 0 if (num_lines < 10) else num_lines - 10
        	text_iterator = itertools.islice(data, line_begin, None)
        	for element in text_iterator:
        		print(element, end)
    except:
        print("[ERROR] El archivo no existe o no puede ser abierto")
def find(file):
	findfile = os.listdir(".")
	fcount = 1
	for f in findfile:
		if f == file:
			print(f)
			break
		else:
			fcount += 1
	if fcount > len(findfile):
		print("find: '{}': no encontrado".format(file))

		
if __name__ == '__main__':
	cmd = str()
	while cmd != "exit":
		cmd = str(raw_input("{}>".format(os.getcwd())))
		if cmd == "help":
			print('''de momento no pondré este comando porque el output es largo y hace dificil 
leer el codigo''')
		elif cmd == "clear":
			clear()
		elif cmd [:2] == "ls":
			if cmd[2:] == "":
				ls()
			elif cmd[2:] != "":
				ls_flags(cmd)
		elif cmd[:5] == "mkdir":
			mkdir(cmd[6:])
		elif cmd[:2] == "cd":
			cd(cmd[3:])
		elif cmd[:2] == "rm" and cmd[2] == " ":
			rm(cmd[3:])
		elif cmd[:4] == "echo":
			print(cmd[5:])
		elif cmd[:5] == "touch":
			open(cmd[6:], "w")
		elif cmd[:3] == "pwd":
			print('''
		{}
				'''.format(os.getcwd()))
		elif cmd[:4] == "head":
			head(cmd[5:])
		elif cmd[:4] == "tail":
			tail(cmd[5:])
		elif cmd[:3] == "cat":
			catfile = open(cmd[4:], "r")
			for line in catfile:
				print(line)
			catfile.close()
		elif cmd[:4] == "find":
			find(cmd[5:])
		elif cmd[:5] == "rmdir":
			try:
				os.rmdir(cmd[6:])
			except:
				print("no se ha podido borrar '{}'".format(cmd[6:]))

		else:
			if cmd != "exit":
					print("comando no reconocido")
	exit()