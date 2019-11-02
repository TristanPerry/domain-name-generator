#!/usr/bin/env  python

import argparse
import itertools
import re
import socket
import sys


def whois_request(domain, server, port=43):
    """
    Carries out the WHOIS request for a particular domain name, against a particular registrar.
    This is not .com specific.
    """
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
    """ 'Builds' the domain name (just appends .com as that's all I check right now) then checks its WHOIS status """
    domain_name = keyword + '.com'
    whois_response = whois_request(domain_name, 'whois.verisign-grs.com')

    if re.search("Domain Name: %s" % domain_name.upper(), whois_response):
        return False
    else:
        return True


def parse_cli_args():
    """ Parses the command line arguments to (e.g.) keep duplicate combinations. """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--allow-duplicates", default=True, help="Allows for keywords to be re-used in the generated domain name",
        action="store_true"
    )

    parser.add_argument("--number-words", default=2, type=int, help="numbers of words in the domain candidates")

    parser.add_argument('--kws', nargs='+', help='<Required> Provide one or more keywords', required=True)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_cli_args()

    combinations = list(itertools.product(args.kws, repeat=args.number_words))  # build all combinations
    keywords = [value for value in combinations if
                args.allow_duplicates or (value[0] != value[1] and not args.allow_duplicates)]  # optionally omit dups

    for kw_tuple in keywords:
        kw = ''.join(str(i) for i in kw_tuple)
        if keyword_free(kw):
            print(kw + '.com is available')
