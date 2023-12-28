import socket
import shutil


socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketClient.connect(("127.0.0.1",9879))


action = input("Hi, would you like to upload or download a file ? press u/d \n")
while(action != '0'):
    if (action == 'u'):
        socketClient.send(action.encode())
        answer = socketClient.recv(1024).decode('utf-8').strip('\r\n')
        path = input(answer + '\n')
        socketClient.send(path.encode())
    elif (action == 'd'):   
        socketClient.send(action.encode())
        answer = socketClient.recv(1024).decode('utf-8').strip('\r\n')
        filename = input(answer + '\n')
        socketClient.send(filename.encode())
        answer = socketClient.recv(1024).decode('utf-8').strip('\r\n')
        path = input("where would u like to keep your file ? \n")
        path = path + '\\' + filename
        if(filename in answer):
            try:
                shutil.copyfile(answer, path)   
            except EnvironmentError:
                print("Something went wrong \n")
        else:
            print(answer + '\n')

    action = input("please enter again u/d or 0 for exit \n")

socketClient.close()