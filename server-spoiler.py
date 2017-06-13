"""
SpoilerWall
This service listen in a port and send to the client a SPOILER!!! :P

Use that IPTABLE rule for redirect all traffic incoming from all ports to this service.
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 1:65535 -j DNAT --to-destination HOST:PORT

Nmap scan => Spoilers everywhere.

"""

import socket
import json
import random
import logging

HOST = "127.0.0.1"
PORT = 8080

FILE_SPOILER = "spoilers.json"
MAX_SPOILER_COUNT = 4200

logging.basicConfig(filename='server.log', format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)

fileSpoilers = open(FILE_SPOILER, "r")
spoilers = json.load(fileSpoilers)
movies = spoilers['movies']
fileSpoilers.close()

if __name__ == "__main__":

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(3)
    print "Ready for ACTION"

    # Main Loop, listen for a connection ... and spoiler!
    while 1:

        # Random spoiler select
        chosen = random.choice(movies)
        spoiler_chosen = chosen['name'] + '\n' + ' '.join([x['value'] for x in chosen['spoilers']]) + '\n'

        conn, addr = s.accept()
        logging.info('Connected with ' + str(addr))

        conn.sendall(spoiler_chosen.encode('ascii','ignore'))
        conn.close()
