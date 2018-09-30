#import modules
import os
import sys
import socket

#import threading module for queued connections 
import threading    

#command line arguments passed to the script
arguments = len(sys.argv)-1
if arguments!= 1:
   print "Usage:server.py <serverport>"
   exit()
   
#accept server port
serverHost = ''
serverPort = int(sys.argv[1])

#responses of server to client
http200 = 'HTTP/1.0 200 OK\n'
http400 = 'HTTP/1.0 400 Bad Request\n'
http404 = 'HTTP/1.0 404 Not Found\n'

#create socket for server
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "This is the server running"

#bind the socket to the port number and wait for connection request
serverSocket.bind((serverHost,serverPort))  
#50 queued connections acceptable 
serverSocket.listen(50)
print 'The server is ready to receive'
   
def clientthread(connectionSocket):
  
    try:
        # get request from client
        data = connectionSocket.recv(1024)
        parameters = data.split(" ")
        message = ''
    
        print parameters
        if parameters[0] == "GET":
           parameters[1]= '.' + parameters[1]
           filename =parameters[1]
           print filename
		   #check if the file exists
           if os.path.isfile(filename):
              target = open ( filename , 'r' )
              lines = target.readlines()
              
              count = 0 
              for line in lines:
                 count= count+len(line)
              #send a message to the server 
              message = message + http200 + 'Content-Length:' + str(count) + '\n' + '\n'
              for line in lines:
                  message = message + line
           else:
              message = http404
        else: 
           message = http400
    
        connectionSocket.sendall(message)
 	#exception handling	 
    except:
        print 'ERROR: Error processing the client. Closing connection...'
    finally:
        connectionSocket.close()
 
while 1:
   connectionSocket, addr=serverSocket.accept()
   print ' New client'
   #starting a new thread
   clientthread(connectionSocket)

conn.close()




