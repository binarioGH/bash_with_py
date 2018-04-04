#-*- coding: utf-8 -*-
import subprocess
import os

def clear():
	subprocess.call(["cmd.exe","/c","cls"])

def ls():
	dirlist = os.listdir('.')
	for file in dirlist:
		print(file)

def mkdir():
	try:
	    os.mkdir(cmd[6:])
	except Exception as e: 
		print("ese directorio ya existe") 

def cd(cdir):
	
	try:
		os.chdir(cdir)
	except Exception as e:
		print("el sistema no puede encontrar la ruta")
def rm(delfd):
	try:
		os.remove(cmd[2:])
	except Exception as e:
		print("no se ha encontrado la carpeta o directorio {}".format(delfd))


if __name__ == '__main__':
	wt = True
	while wt:
		cmd = str(raw_input("{}>".format(os.getcwd())))
		if cmd == "help":
			print('''de momento no pondré este comando porque el output es largo y hace dificil 
leer el codigo''')
		elif cmd == "clear":
			clear()

		elif cmd [:2] == "ls" and cmd[2:] == "":
			ls()

		elif cmd[:6] == "mkdir ":
			mkdir()

		elif cmd[:2] == "cd":
			cd(cmd[3:])

		elif cmd[:2] == "rm":
			rm(cmd[2:])


		elif cmd[:4] == "echo":
			print(cmd[5:])
		elif cmd[:5] == "touch":
			open(cmd[5:], "w")
		elif cmd[:3] == "pwd":
			print('''
		{}
				'''.format(os.getcwd()))

        
        