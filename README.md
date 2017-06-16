# Beware! Spoilers ahead!

Spoilerwall introduces a brand new concept in the field of network hardening. Avoid being scanned by spoiling movies on all your ports!

Firewall? How about Fire'em'all! Stop spending thousand of dollars on big teams that you don't need! Just fire up the Spoilers Server and that's it!

Movie Spoilers DB + Open Ports + Pure Evil = Spoilerwall

Set your own:

1. Clone this repo

```
$ git clone git@github.com:infobyte/spoilerwall.git
```

2. Edit the file `server-spoiler.py` and set the **HOST** and **PORT** variables.

3. Run the server

```
$ python2 server-spoiler.py
```


View the live demo running in spoilerwall.faradaysec.com

```
~ ❯❯❯ telnet spoilerwall.faradaysec.com 23

Trying 138.197.196.144...

Connected to spoilerwall.faradaysec.com.

Escape character is '^]'.

Gummo

Fucked up people killing cats after a tornado

Connection closed by foreign host.
```

Browse in Shodan (but beware of the Spoilers!):

https://www.shodan.io/host/138.197.196.144

Be careful in your next CTF - you never know when the spoilers are coming!

