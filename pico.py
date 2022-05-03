import socket

print("""       .__              
______ |__| ____  ____  
\____ \|  |/ ___\/  _ \ 
|  |_> >  \  \__(  <_> )
|   __/|__|\___  >____/ 
|__|           \/       """)

import socket

t_host = input("Enter the host to be scanned: ")   # Target Host, www.example.com
t_ip = socket.gethostbyname(t_host)     # Resolve t_host to IPv4 address
print("Scanning ", t_ip)

while 1:

	t_port = input("Enter the port: ")	

	try:
		sock = socket.socket()			
		res = sock.connect((t_ip, t_port))
		print("Port {}: Open" .format(t_port))
		sock.close

	except:
		print("Port {}: Closed" .format(t_port))

	
print("Port Scanning complete")