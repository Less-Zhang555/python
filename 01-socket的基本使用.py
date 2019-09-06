import socket


def main():
    """udp通信"""
    # 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 使用socket套接字收发数据
    udp_socket.sendto(b"hahahaha", ("127.0.0.1", 60000))
    # 关闭socket
    udp_socket.close()


if __name__ == "__main__":
    main()
