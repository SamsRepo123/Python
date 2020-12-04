# Get any website 's ip address
import socket as s
host = input("Enter website: ")
print(f'IP address of {str(host)} is {s.gethostbyname(str(host))}')