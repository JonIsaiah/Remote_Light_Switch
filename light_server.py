import socket
import threading

import time
import bluetooth




bind_ip = "192.168.1.114"
bind_port = 46000
bluetooth_MAC = '98:D3:31:30:77:53'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

#listen on port 46000 with max connection baglog = 5
server.listen(30)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)





def bt_connect(address, channel):
    while(True):
        try:
            btSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            btSocket.connect((address, channel))
            break
        except:
            btSocket.close()
            print "Could not establish bluetooth connection: ", error, "; Retrying in 1s..."
            time.sleep(1)
    return btSocket
        
def bt_disconnect(bt_socket):
    bt_socket.close()





def turn_off_lights():
    switchSocket = bt_connect(bluetooth_MAC, 1)
    switchSocket.send('0')
    bt_disconnect(switchSocket) 


def turn_on_lights():
    switchSocket = bt_connect(bluetooth_MAC, 1)
    switchSocket.send('1')
    bt_disconnect(switchSocket)






# client handling thread
def handle_client(client_socket):
    
    request = client_socket.recv(1024)
    
    if request != '':
        print "[*] Received: %s" % (request)

        client_socket.send("ACK!")
        client_socket.close()

    
        request_params = request.splitlines()
        path = request_params[0].split()[1]

        if path == '/lights-on':
            print path
            turn_on_lights()
        elif path == '/lights-off':
            print path
            turn_off_lights()
        

    else:
        client_socket.send("ACK!")
        client_socket.close()












#Main server loop
while True:

    client, addr = server.accept()
    print "[*] Accepted connection from %s:%d" % (addr[0], addr[1])
    
    #spin up client thread to pass off connection
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

     



