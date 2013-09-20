#!/usr/bin/env python33


'''
Banner printer.

>>> help(banner_printer.main)
'''

import textwrap
import socket
import sys


__author__ = 'Ismael Venegas Castelló'
__license__ = 'GPL v2'
__email__ = 'ismael.vc1337@gmail.com'


def _return_banner(ip:'str', port:'int'=21):
    try:
        socket.setdefaulttimeout(2)
        with socket.socket() as s:
            s.connect((ip, port))
            banner = s.recv(1024).decode().rstrip()

        return banner

    except Exception as e:
        print('[-] ERROR: {0}'.format(e))


def _print_banner(*args):
    for index, ip in enumerate(args):
        banner = _return_banner(ip)

        if banner:
            print(textwrap.dedent(
                 '''[+] SUCCESS:
                    {3}Banner => "{0}"
                    {3}ip #{1} => {2}'''.format(banner, index, ip, '\t')))
        else:
            print('\tip #{0} => {1}'.format(index, ip))


def main(*args):
    '''
    Prints the banner of the provided ips.

    Usage:
        banner_printer.main([args])

    Examples:
        $ python33 banner_printer.py
    
        $ python33 banner_printer.py 150.65.7.130

        $ python33 banner_printer.py 150.65.7.130 72.26.195.64

        $ python33

        >>> import banner_printer

        >>> banner_printer.main()    # Runs default test.

        >>> banner_printer.main('150.65.7.130')

        >>> banner_printer.main('150.65.7.130', '192.168.95.149')

        >>> ip_list = ['192.168.95.148',
                       '150.65.7.130',
                       '192.168.95.149',
                       '72.26.195.64']

        >>> banner_printer.main(*ip_list)

        [-] ERROR: timed out
                ip #0 => 192.168.95.148

        [+] SUCCESS:
                Banner => "220 (vsFTPd 3.0.2)"
                ip #1 => 150.65.7.130

        [-] ERROR: timed out
                ip #2 => 192.168.95.149
        [-] ERROR: timed out
                ip #3 => 72.26.195.64
    '''
    if not args:
        args = ['192.168.95.148',
                '150.65.7.130',
                '192.168.95.149',
                '72.26.195.64']

    if len(sys.argv) >= 2:
        args = sys.argv[1:]

    _print_banner(*args)


if __name__ == '__main__':
    main()
