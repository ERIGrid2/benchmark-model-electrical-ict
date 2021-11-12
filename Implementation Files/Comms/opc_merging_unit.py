from opcua import Client
from opcua import ua
import socket
import binascii
import _thread
import time

HOST = ''
PORT1 = 991
PORT2 = 992
PORT3 = 993
PORT4 = 994

# Access data from OPC UA server
url = "opc.tcp://192.168.56.101:8899/freeopcua/server/"
client = Client(url)
client.connect()
print("connected to OPC UA Server")
val1 = client.get_node("ns=2;i=10")#tap position of transformer
val2 = client.get_node("ns=2;i=20")#capacitor status
val3 = client.get_node("ns=2;i=22")#capacitor step
val4 = client.get_node("ns=2;i=9")#tap control
val5 = client.get_node("ns=2;i=21")#capacitor step control

# Define a function for the thread
def serverOne(): #read data from OPC and send to algorithm
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.bind(('',PORT1))
		s1.listen()
		conn1, addr = s1.accept()
		value=0
		with conn1:
			print('Server 1 from:',addr)
			a = 1
			value = 2
			while a < 6:
				# Update OPC values
				value1 = val1.get_value()
				value2 = val2.get_value()
				value3 = val3.get_value()
	
				# convert integer to string
				stringd = str(value1)+"-"+str(value2)+"-"+str(value3)
				# convert string to bytes data
				data1 = stringd.encode()
				# send data back to client
				conn1.sendall(data1)
				print("sent data")
				# delay for 150s
				time.sleep(150)
				
def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.bind(('',PORT2))
		s2.listen()
		conn2, addr = s2.accept()
		valueb=0
		with conn2:
			print('Server 2 from:',addr)
			while True:
				data2 = conn2.recv(1024)
				data2 = data2.decode("utf-8")
				print(data2)

				tap_new,step_new= data2.split("-")
				print("Received updated values from CVC")
				print(tap_new,step_new)
				tap_new=int(tap_new)
				step_new=int(step_new)

				val4.set_value(tap_new, ua.VariantType.Int16)
				val5.set_value(step_new, ua.VariantType.Int16)

# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
