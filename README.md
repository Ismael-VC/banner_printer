banner_printer
==============

Banner printer


Prints the banner of the provided ips.

    Usage:
        banner_printer.main([args[, port[, timeout]]])

    Examples:

        $ python33 banner_printer.py    # Runs default test.
        $ python33 banner_printer.py 150.65.7.130
        $ python33 banner_printer.py 150.65.7.130 72.26.195.64

        $ python33
        >>> import banner_printer
        
        >>> banner_printer.main()    # Runs default test.
        >>> banner_printer.main('150.65.7.130', port=21, timeout=3)
        >>> banner_printer.main('150.65.7.130', '192.168.95.149')

        >>> ip_list = ['192.168.95.148',
                       '150.65.7.130',
                       '192.168.95.149',
                       '72.26.195.64']
                       
        >>> banner_printer.main(*ip_list)
        [-] ERROR: timed out
                ip => "192.168.95.148"
        [+] SUCCESS:
                Banner => "220 (vsFTPd 3.0.2)"
                ip => "150.65.7.130"
        [-] ERROR: timed out
                ip => "192.168.95.149"
        [-] ERROR: timed out
                ip => "72.26.195.64"
