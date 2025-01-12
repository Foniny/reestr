import winreg

import argparse
 
parser = argparse.ArgumentParser(description="argumemt list")
parser.add_argument("k", help="")
parser.add_argument("n", help="")
parser.add_argument("p", help="")

 
args = parser.parse_args()

registry_path = winreg.HKEY_CURRENT_USER
#key_path = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
#program_name = "Strike"
#executable_path = r"D:\Games\sozdanie puti.py"
key_path = args.k
program_name = args.n
executable_path = args.p
try:
	#
	with winreg.OpenKeyEx(registry_path, key_path, 0, winreg.KEY_WRITE) as registry_key:
	
		winreg.SetValueEx(registry_key, program_name, 0, winreg.REG_SZ, executable_path)
	print(f"{program_name} complete")
        
except Exception as e:
	print(e)