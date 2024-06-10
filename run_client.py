import argparse
import socket


def run_tcp_socket_client(
        host,
        port
    ):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall("hello world".encode())
        data = s.recv(1024)
        print(f"Data received: {data}")


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

    run_tcp_socket_client(args.host, args.port)
