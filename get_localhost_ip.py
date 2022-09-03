import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("Your localhost ====> ", s.getsockname()[0])
s.close()
