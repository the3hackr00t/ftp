import socket

print("""       .__              
______ |__| ____  ____  
\____ \|  |/ ___\/  _ \ 
|  |_> >  \  \__(  <_> )
|   __/|__|\___  >____/ 
|__|           \/       """)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
target = input('Enter a IP address: ') 
  
t_IP = socket.gethostbyname(target) 
print("Scanning ", t_IP) 
  
  
def port_scan(port): 
    try: 
        s.connect((t_IP, port)) 
        return True
    except: 
        return False
  
  
port = int(input("Enter a port number: ")) 
  
if port_scan(port): 
    print('Port', port, 'is open') 
else: 
    print("port", port, "is closed") 
