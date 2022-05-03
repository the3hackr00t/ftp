import socket
import time

print("""       .__              
______ |__| ____  ____  
\____ \|  |/ ___\/  _ \ 
|  |_> >  \  \__(  <_> )
|   __/|__|\___  >____/ 
|__|           \/       """)
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  
target = input('Enter the host to be scanned: ') 
  
target_ip = socket.gethostbyname(target) 
print('Scanning', target_ip) 
  
  
  
def port_scan(port): 
    try: 
        s.connect((target_ip, port)) 
        return True
    except: 
        return False
  
  
start = time.time() 
  
for port in range(5): 
    if port_scan(port): 
        print(f'port {port} is open') 
    else: 
        print(f'port {port} is closed') 
  
end = time.time() 
print(f'Time taken {end-start:.2f} seconds')
