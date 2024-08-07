import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='backup',
        description='Backup MySQL database.',
        epilog='Copyright(r) 2024'
    )
    # outfile
    # host localhost
    # port 3306 init
    # u user required
    # p password required
    # database required
    # gz gzcompress optional
    parser.add_argument('outfile')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default='3306', type=int)
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    parser.add_argument('--gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')
    args = parser.parse_args()
    
    print(args)

if __name__ == '__main__':
    main()