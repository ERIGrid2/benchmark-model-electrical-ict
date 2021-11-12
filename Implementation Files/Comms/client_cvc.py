import binascii
import _thread
import time
import socket
import time
import datetime
from Voltage_controller_V02 import *

HOST2 = '100.6.0.11'
PORT1 = 991
PORT2 = 992

# Define a function for the thread
def serverOne():
	Vbusbars = [] # empty list for the ouput of the state estimation
	for i in range(1,12):
				Vbusbars.append(1)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.connect((HOST2, PORT1))
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
			s2.connect((HOST2, PORT2))
			x = 1
			while x < 2:
				# receive data from server
				data1 = s1.recv(1024)
				data1new = data1.decode("utf-8")
				tap,status,step= data1new.split("-")
				print("connected to OPC")
				print(status,step,tap)
				tap=int(tap)
				status= int(status)
				step=int(step)
				# cvc code
				a,b,c = Voltage_Controller(Vbusbars,status,step,tap)
				print(b,c) # a -> new Q; b -> new tap; c -> new step of capacitor
				tap_new=str(b)
				step_new=str(c)
				string_new = tap_new+"-"+ step_new
				# convert string to bytes data
				data_new = string_new.encode()
				# send data back to OPC
				s2.sendall(data_new)
				
# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   #_thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
