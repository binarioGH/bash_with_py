#-*- coding: utf-8 -*-
import subprocess
import os
# de momento este programa no esta tan avanzado, pero con el tiempo lo voy a mejorar.
if __name__ == '__main__':
	wt = True
	while wt:
		cmd = str(raw_input("{}>".format(os.getcwd())))
		if cmd == "help":
			print('''de momento no pondré este comando porque el output es largo y hace dificil 
leer el codigo''') 	
		elif cmd == "clear":
			subprocess.call(["cmd.exe","/c","cls"])
		elif cmd [:2] == "ls" and cmd[2:] == "":
			dirlist = os.listdir('.')
			
			for file in dirlist:
				print(file)
						
		elif cmd[:6] == "mkdir ":
			try:
				os.mkdir(cmd[6:])
			except Exception as e: 
				print("ese directorio ya existe") 
		elif cmd[:3] == "cd ":
			try:
				os.chdir(cmd[3:])
			except Exception as e:
				print("el sistema no puede encontrar la ruta")
		elif cmd[:2] == "rm":
			try:
				os.remove(cmd[3:])
			except Exception as e:
				print("carpeta o archivo '{}' no encontrado".format(cmd[3:]))
		elif cmd[:4] == "echo":
			print(cmd[5:])
		elif cmd[:5] == "touch":
			open(cmd[6:], "w")
			




		    		