import socket
import threading
import time

from utils import log


def run(host='', port=3000):
    log('start at', '{}:{}'.format(host, port))
    # Configure socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))

        # infinite loop, server forever
        while True:
            # passively wait, 3: maximum number of connections in the queue
            s.listen(3)
            # accept and establish connection
            conn, addr = s.accept()

            def process(conn, addr):
                # receive message
                request = conn.recv(1024)
                time.sleep(3)
                request = request.decode('utf-8')
                log('request is: ',request)
                log('Connected by', addr)

                # send message
                header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
                body = '<h1>Yes</h1>'
                response = header + '\r\n' + body
                conn.sendall(response.encode('utf-8'))
                # close connection
                conn.close()

            t = threading.Thread(target=process, args=(conn, addr))
            t.start()


if __name__ == '__main__':
    config = dict(
        host='',
        port=3000,
    )
    run(**config)