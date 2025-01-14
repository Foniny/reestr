import winreg

import argparse
 
parser = argparse.ArgumentParser(description="argumemt list")
parser.add_argument("-r", help='''set value \n1:HKEY_CLASSES_ROOT\n2:HKEY_CURRENT_USER\n
	3:HKEY_LOCAL_MACHINE\n4:HKEY_USERS\n5:HKEY_CURRENT_CONFIG''')
parser.add_argument('-k', help='set key_path in " "')
parser.add_argument('-n', help='set name in " "')
parser.add_argument('-p', help='set executable_path in " "')
 
args = parser.parse_args()

def registry_path(key):
	if key == '1':
		r_path = winreg.HKEY_CLASSES_ROOT
	elif key=='2':
		r_path = winreg.HKEY_CURRENT_USER
	elif key=='3':
		r_path = winreg.HKEY_LOCAL_MACHINE
	elif key=='4':
		r_path = winreg.HKEY_USERS
	elif key=='5':
		r_path = winreg.HKEY_CURRENT_CONFIG
	return r_path

#key_path = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
#program_name = "Strike"
#executable_path = r"D:\Games\sozdanie puti.py"
r_path = registry_path(args.r)
key_path = args.k
program_name = args.n
executable_path = args.p
try:
	#
	with winreg.OpenKeyEx(r_path, key_path, 0, winreg.KEY_WRITE) as registry_key:
	
		winreg.SetValueEx(registry_key, program_name, 0, winreg.REG_SZ, executable_path)
	print(f"{program_name} complete")
        
except Exception as e:
	print(e)
