#!/usr/bin/env  python

import itertools
import re
import socket
import sys


def whois_request(domain, server, port=43):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, port))
    sock.send(("%s\r\n" % domain).encode("utf-8"))
    buff = b""
    while True:
        data = sock.recv(1024)
        if len(data) == 0:
            break
        buff += data
    return buff.decode("utf-8")


def keyword_free(keyword):
    domain_name = keyword + '.com'
    whois_response = whois_request(domain_name, 'whois.verisign-grs.com')

    if re.search("Domain Name: %s" % domain_name.upper(), whois_response):
        return False
    else:
        return True


combinations = list(itertools.product(sys.argv[1:], repeat=2))  # build all combinations
keywords = [value for value in combinations if value[0] != value[1]]  # omit any duplicates
for kw_tuple in keywords:
    kw = ''.join(str(i) for i in kw_tuple)
    if keyword_free(kw):
        print(kw + '.com is available')
