def sc():
    import socket
    from time import sleep as sl
    from colorama import Fore
    host = input(Fore.WHITE+'input URL: \n>>')
    ports = []
    for i in range(0, 65536):
        ports.append(i)
    open_port = []
    for port in ports:
        sock = socket.   socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.05)
        try:
            sock.connect((host, port))
        except:
            print(Fore.CYAN+'[|]', end ='Cheking port\r')
            sl(0.09)
            print('[/]', end ='Cheking port %s\r' % port)
            sl(0.09)
            print('[—]', end ='Cheking port \r')
            sl(0.09)
            print('[\]', end ='Cheking port \r')
            sl(0.09)
            print('[|]', end ='Cheking port \r')
            sl(0.0009)
        else:
            open_port.append(port)
            print(Fore.LIGHTGREEN_EX+'Порт %s открыт        \n' % port)
            sock.close()
