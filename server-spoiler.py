"""
SpoilerWall
This service listen in a port and send to the client a SPOILER!!! :P

Use that IPTABLE rule for redirect all traffic incoming from all ports to this service.
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 1:65535 -j DNAT --to-destination HOST:PORT

If you redirect to localhost, you need that:
sysctl -w net.ipv4.conf.eth0.route_localnet=1

Nmap scan => Spoilers everywhere.

"""

try:
    import socketserver as server
except ImportError:
    import SocketServer as server
import json
import random
import logging

HOST = "127.0.0.1"
PORT = 8080

FILE_SPOILER = "spoilers.json"
MAX_SPOILER_COUNT = 4200

SPOILER_COLOR = '\033[92m'
ASCII_NO_COLOR = '\033[0m'


class MyTCPHandler(server.BaseRequestHandler):

    def handle(self):
        logging.info('Connected with ' + str(self.client_address))

        # Random spoiler select
        chosen = random.choice(movies)
        spoiler_chosen = chosen['name'] + '\n' + ' '.join([x['value'] for x in chosen['spoilers']]) + '\n'

        self.request.sendall(SPOILER_COLOR + spoiler_chosen.encode('ascii','ignore') + ASCII_NO_COLOR)
        self.request.close()

if __name__ == "__main__":

    logging.basicConfig(filename='server.log', format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())

    fileSpoilers = open(FILE_SPOILER, "r")
    spoilers = json.load(fileSpoilers)
    movies = spoilers['movies']
    fileSpoilers.close()

    server = server.TCPServer((HOST, PORT), MyTCPHandler)
    logging.info("Ready for ACTION")
    server.serve_forever()
