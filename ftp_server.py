from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
from pyftpdlib.handlers import TLS_FTPHandler
from pyftpdlib.servers import FTPServer
import argparse



def main(args):

    authorizer = DummyAuthorizer()
    authorizer.add_user(args.user, args.pswd, args.root_dir, perm=args.perm)
    handler = TLS_FTPHandler
    handler.certfile = './key.pem'
    handler.authorizer = authorizer
    # requires SSL for both control and data channel
    handler.tls_control_required = True
    handler.tls_data_required = True
    if args.nat_addr.upper() != 'NA':
        handler.masquerade_address = args.nat_addr
    handler.permit_foreign_addresses = True
    portrange = args.port_range.split('-')
    handler.passive_ports = range(int(portrange[0]), int(portrange[1]))
    server = FTPServer((args.lstn_addr, args.port), handler)
    server.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FTP Server Parameters')
    parser.add_argument('--user', required=True, help='Username')
    parser.add_argument('--pswd', required=True, help='Password')
    parser.add_argument('--port', required=True, type=int, help='port number')
    parser.add_argument('--root_dir', required=True, help='root dictionary')
    parser.add_argument('--port_range', required=True, help='passive port range')
    parser.add_argument('--perm',default='elr', help='permission default=elr')
    parser.add_argument('--nat_addr',default='na', help='masquerade_address')
    parser.add_argument('--lstn_addr', default='0.0.0.0', help='serving address')
    args = parser.parse_args()
    main(args)