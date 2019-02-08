from bluetooth import *
import time

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "47e9ef55-47e9-11e4-8939-164230d1df67"

advertise_service( server_sock, "SampleServer",
               service_id = uuid,
               service_classes = [ uuid, SERIAL_PORT_CLASS ],
               profiles = [ SERIAL_PORT_PROFILE ],#,
#              protocols = [ OBEX_UUID ]
              )

print ("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print ("Accepted connection from ", client_info)



while True:
    try:
        print("Preparing to send data\n")
        server_sock.send("This is a test of the android raspberry pi Bluetooth Connection\n")
        print("Data sent\n")
        time.sleep(0.5)


    except IOError:
        pass

print ("disconnected")

client_sock.close()
server_sock.close()
print ("all done")