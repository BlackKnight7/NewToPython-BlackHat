import socket
import threading

host = '127.0.0.1'
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print '[*] Listening on %s:%d' % (host, port)


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print '[*] Reviced %s' % request

    client_socket.send('ACK')
    client_socket.close()


while True:
    client, addr = server.accept()
    print '[*] Accepted connection from %s:%d' % (addr[0], addr[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
