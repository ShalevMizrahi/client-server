import socket 
import shutil
import os
import pickle

ip = "127.0.0.1"
port = 9879
def Server():
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created succsesfully \n")

    try:
        socketServer.bind((ip,port)) 
        print("Socket in listening mode \n")
    except socket.error as msg:
        print("Bind failed \n")
    socketServer.listen(1) 
    (clientConnection,clientAddress)= socketServer.accept()
    backupPath = "D:\\python2.0\\clientsBackups"
    action = clientConnection.recv(1024).decode('utf-8').strip('\r\n')

    while(action != '0'): 
        if(action == 'u'):
            clientConnection.send("which file ?".encode())
            path = clientConnection.recv(1024).decode('utf-8').strip('\r\n')
            pathList = path.split("\\")
            filename = pathList[len(pathList)-1]
            workPath = backupPath + "\\" + filename
            print(workPath)
            print(path)
            try:
                shutil.copyfile(path,workPath)
            except EnvironmentError:
                print("Something went wrong \n")
        if(action == 'd'):
            clientConnection.send("which file ?".encode())
            filename = clientConnection.recv(1024).decode('utf-8').strip('\r\n')
            workPath = backupPath + "\\" + filename
            filesList = os.listdir(backupPath)
            if filename in filesList:
                clientConnection.send(workPath.encode())
            else:
                clientConnection.send("Sorry, dont have this file :(".encode())

                   
               

    clientConnection.close()
    socketServer.close()

Server()

