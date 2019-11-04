#!/usr/bin/env  python

import argparse
import itertools
import re
import socket
import sys


def whois_request(domain, server='whois.verisign-grs.com', port=43):
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


def check_domain_candidate(keyword, args):
    """
    'Builds' the domain name (just appends .com as that's all I check right now)
    then checks its WHOIS status - assuming we don't skip this in the args.
    """
    domain_name = keyword + '.com'

    if not args.skip_whois:
        whois_response = whois_request(domain_name)

        if re.search("Domain Name: %s" % domain_name.upper(), whois_response):
            # we have a match; the domain is already registered
            if args.show_taken:
                try:
                    expiry_date = re.search("Registry Expiry Date\: (.*)", whois_response).group(1)
                    print(domain_name + ' is NOT available; expiry date is ' + expiry_date)
                except AttributeError:
                    print(domain_name + ' is NOT available')
        else:
            print(domain_name + ' is available')
    else:
        print(domain_name + ' was generated (but not checked for availability)')


def parse_cli_args():
    """ Parses the command line arguments to (e.g.) keep duplicate combinations. """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--skip-whois", default=False,
        help="Only generate the possible domain name candidates (and output them)"
             "- this does not do the actual WHOIS availability check.",
        action="store_true"
    )

    parser.add_argument(
        "--show-taken", default=False,
        help="Outputs all results, even generated domains which have already been registered.",
        action="store_true"
    )

    parser.add_argument('--kws', nargs='+',
                        help='<Required> Provide one or more groups of keywords (each group can be a single keyword'
                             'or comma separated, e.g. "--kws kw1,kw1alt,kw1b kw2,kw2alt"'
                             'and "--kws kw1 kw2" are both valid inputs)',
                        required=True)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_cli_args()

    kws = [kw.split(",") for kw in args.kws]

    # build all combinations from the provided keyword groups (i.e. the list of list of strings)
    combinations = list(itertools.product(*kws))

    for kw_tuple in combinations:
        kw = ''.join(str(i) for i in kw_tuple)
        check_domain_candidate(kw, args)
