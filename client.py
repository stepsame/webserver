import socket

from utils import log


def run(host='', port=3000):
    # configure socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # send message
    request = 'GET / HTTP/1.1\r\nHost:localhost:3000\r\n\r\n'.encode('utf-8')
    s.sendall(request)
    # receive message
    reply = s.recv(1024)
    log('reply is: ', reply)
    # close connection
    s.close()


if __name__ == '__main__':
    config = dict(
        host='127.0.0.1',
        port=3000,
    )
    run(**config)
