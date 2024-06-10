import socket
import argparse


def create_tcp_server_socket(
        host,
        port
    ):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                print(f"data received: {data}")
                if not data:
                    break
                conn.sendall(data)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "host",
        default="0.0.0.0",
        type=str
    )
    argparser.add_argument(
        "port",
        default=8080,
        type=int
    )

    args = argparser.parse_args()

    create_tcp_server_socket(args.host, args.port)
