import os
os.system('pip3 install python-nmap')
import nmap 
sc = nmap.PortScanner()
print("""       .__              
______ |__| ____  ____  
\____ \|  |/ ___\/  _ \ 
|  |_> >  \  \__(  <_> )
|   __/|__|\___  >____/ 
|__|           \/       """)

def main():
	n = input("1- Network Scanner\n2- Vulnerabilities Detection\n3- Exploit\n\nPlease enter a number :")

	if n == '1':
		nmap()

	if n == '2':
		vuln()

	if n == '3':
		os.system('msfconsole')

	else :
		print("Please ente a number between 1 and 3")
		delay(1500)
		main()

def nmap():
	print("**********Network Scanner**********")
	ip = input("\nPlease enter the IP address: ")
	sc.scan(ip , '1-1024')
	print(sc.scaninfo())
	print(sc[ip]['tcp'].key())

def vuln():
	print("**********Vulnerabilities Scanner**********")
	ip = input("\nPlease enter the IP address")
	print(os.system('nmap -sV --script=vulscan.nse ' +ip))

if __name__ == "__main__":
	main()