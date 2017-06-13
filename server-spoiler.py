"""
SpoilerWall
This service listen in a port and send to the client a SPOILER!!! :P

Use that IPTABLE rule for redirect all traffic incoming from all ports to this service.
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 1:65535 -j DNAT --to-destination HOST:PORT

Nmap scan => Spoilers everywhere.

"""

import SocketServer
import json
import random
import logging

HOST = "127.0.0.1"
PORT = 8080

FILE_SPOILER = "spoilers.json"
MAX_SPOILER_COUNT = 4200


class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        logging.info('Connected with ' + str(self.client_address))

        # Random spoiler select
        chosen = random.choice(movies)
        spoiler_chosen = chosen['name'] + '\n' + ' '.join([x['value'] for x in chosen['spoilers']]) + '\n'

        self.request.sendall(spoiler_chosen.encode('ascii','ignore'))
        self.request.close()

if __name__ == "__main__":

    logging.basicConfig(filename='server.log', format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)

    fileSpoilers = open(FILE_SPOILER, "r")
    spoilers = json.load(fileSpoilers)
    movies = spoilers['movies']
    fileSpoilers.close()

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print "Ready for ACTION"
    server.serve_forever()