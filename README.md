banner_printer
==============

Banner printer


Prints the banner of the provided ips.

    Usage:
        banner_printer.main([args])

    Examples:

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
