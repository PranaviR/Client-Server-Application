#import modules
import os
import sys
import socket

#command line arguments passed to the script
arguments=len(sys.argv)-1
if arguments!=2:
   print "Usage: client.py <serverHost><serverPort>"
   exit()
   
#accept server host name and port number 
serverHost=str(sys.argv[1])
serverPort=int(sys.argv[2])

try:
 #creates the client socket of TCP type
 clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 clientSocket.connect((serverHost,serverPort))
 
 #accept filename to be accessed
 filename=raw_input("Enter the filename \n");
 m='GET '+'/'+filename+' HTTP/1.0\n'
 print m
 clientSocket.sendall(m)
 
 file=clientSocket.makefile()
 #read response from server and split by spaces
 response=file.readline()
 code=response.split(" ")
 print response

 if code[1]=="400":
   print '\nBad Request'

 elif code[1]=="404":
   print '\nFile not found'
   
   #file requested found
 elif code[1]=="200":
   contentlen=file.readline()
   print contentlen
   lines=file.readlines()
   content=open(filename, 'w')
   
   #write data into a new file in the client machine and print the data
   for line in lines:
    content.write(line)
   for line in lines:
	print(line)
   content.close()
   
#exception handling
except:
 print 'Exiting due to error'
 
 #socket connection closed
 clientSocket.close()








