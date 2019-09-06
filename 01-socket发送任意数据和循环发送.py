import socket


def main():
    """udp通信"""
    # 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 使用socket套接字收发数据
    # udp_socket.sendto(b"hahahaha", ("127.0.0.1", 60000))  # 使用sendto方法时发送的数据不能为字符串，应该是类字节类型的数据
    while True:
        send_data = input("输入要发送的数据： ")
        if send_data == "exit":
            break
        udp_socket.sendto(send_data.encode("gbk"), ("127.0.0.1", 60000))
    # 关闭socket
    udp_socket.close()


if __name__ == "__main__":
    main()
