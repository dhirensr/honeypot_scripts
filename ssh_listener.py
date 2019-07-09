#!/usr/bin/env python3
import socket, sys, threading, _thread
import paramiko

#generate keys with 'ssh-keygen -t rsa -f server.key'
HOST_KEY = paramiko.RSAKey(filename='/root/.ssh/id_rsa') #the directory needs to be configured
SSH_PORT = 22
LOGFILE = 'logins.txt' #File to log the user:password combinations to
LOGFILE_LOCK = threading.Lock()

class SSHServerHandler (paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        LOGFILE_LOCK.acquire()
        try:
            logfile_handle = open(LOGFILE,"a")
            print("New login: " + username + ":" + password)
            print(self.ipaddr, self._sshtun_port, self.ssh_user, self.ssh_user_pass)
            logfile_handle.write(self.ipaddr+self._sshtun_port+self.ssh_user+self.ssh_user_pass+ "\n")
            logfile_handle.close()
        finally:
            LOGFILE_LOCK.release()
        return paramiko.AUTH_FAILED


    def get_allowed_auths(self, username):
        print(self.__dict__)
        return 'password'

def handleConnection(client):
    transport = paramiko.Transport(client)
    transport.add_server_key(HOST_KEY)
    server_handler = SSHServerHandler()

    transport.start_server(server=server_handler)

    channel = transport.accept(1)
    if not channel is None:
        channel.close()

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("", SSH_PORT))
        server_socket.listen(100)
        paramiko.util.log_to_file('paramiko.log')

        while(True):
            try:
                client_socket, client_addr = server_socket.accept()
                thread.start_new_thread(handleConnection,(client_socket,))
            except Exception as e:
                print("ERROR: Client handling")
                print(e)

    except Exception as e:
        print("ERROR: Failed to create socket")
        print(e)
        sys.exit(1)

main()
