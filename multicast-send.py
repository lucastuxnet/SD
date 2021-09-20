# Multicast sender
# Guidance:  https://stackoverflow.com/a/1794373
import socket
from typing import cast
import time

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
MESSAGE = b'MSG 03'

# regarding socket.IP_MULTICAST_TTL
# ---------------------------------
# for all packets sent, after two hops on the network the packet will not
# be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
MULTICAST_TTL = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

counter = 0
try:
    while True:
        sock.sendto(MESSAGE, (MCAST_GRP, MCAST_PORT))
        #sock.sendto(input().encode(), (MCAST_GRP, MCAST_PORT))
        print("Mensagens enviadas {0}".format(counter))
        counter = counter + 1
        time.sleep(.5)
except Exception as e:
    print(e)
