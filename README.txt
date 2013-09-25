=====
Growl
=====

Growl is a Python interface for the Growl (GNTP) protocol. It can be used to
build registration and notification packets for sending over a socket connection.

    >>> from growl import Registration, Notification, GROWL_UDP_PORT   
    >>> from socket import socket, AF_INET, SOCK_DGRAM
    >>> addr = ("localhost", GROWL_UDP_PORT)
    >>> s = socket(AF_INET, SOCK_DGRAM)
    >>> p = Registration()
    >>> p.add_notification()
    >>> s.sendto(p.payload(), addr)
    >>>
    >>> p = Notification()
    >>> s.sendto(p.payload(), addr)


Installation
=============

To install Growl, simply:

    $ pip install growl

You should have either the open-source version of Growl (1.2.2) or the commercial 
version of Growl (2.1.2). In the Network pane of the Growl preferences, check both:

* Listen for incoming notifications

* Allow remote application registration

If you set a server password (which you should), include the password in all 
packets sent.


Contributions
=============

Forked to Github from Rui Carmo's netgrowl.py: https://the.taoofmac.com/space/projects/netgrowl

Ingmar J Stein (Growl Team) and John Morrissey both contributed to netgrowl.py

The goal of this fork is to provide compatability with both the commerical and 
open-source versions of Growl, improve PEP-8 support and encourage contributions
by hosting on Github.
