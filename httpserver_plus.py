#!/usr/bin/env python3
# Made by WafflesExploits
import argparse
import http.server
import socketserver
import ssl
import os
import sys

parser = argparse.ArgumentParser(description='An improved version of Pythons http.server, created for redirection purposes.\n\nRerout Example: localhost/about -> localhost/about.html',epilog="[HTTP Usage Example]\n sudo python3 httpserver_plus.py -p <PORT> -d <path-to-directory-with-html-files>\n\n[HTTPS Usage Example]\n 1. Generate a self-signed SSL Certificate.\n  openssl req -new -x509 -keyout server.key -out server.crt -days 365 -nodes\n 2. Run the script with -sc and -sk flags.\n  sudo python3 httpserver_plus.py -p <PORT> -d \"<path-to-directory-with-html-files>\" -sc \"<path-to-server.crt-file>\" -sk \"<path-to-server.key-file>\"" ,formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-p','--port', type=str, help="Specify Port to use.")
parser.add_argument('-d','--directory', type=str, help="Specify directory where .html pages are stored.")
parser.add_argument('-sc','--ssl-certificate', nargs='?' ,type=str, help="Specify the path to SSL's .cert file, to use HTTPS.")
parser.add_argument('-sk','--ssl-key', nargs='?' ,type=str, help="Specify the path to SSL's .key file, to use HTTPS.")

args = parser.parse_args()
# Checks
if(not args.port or not args.directory):
    parser.print_help()
    sys.exit()
if(args.ssl_certificate and not args.ssl_key):
    print('[ERROR] - If you use the -sc flag, you must use -sk flag too!')
    sys.exit()
if(not args.ssl_certificate and args.ssl_key):
    print('[ERROR] - If you use the -sk flag, you must use -sc flag too!')
    sys.exit()

# Define variables
PORT = int(args.port)
directory = args.directory
ssl_certificate_path = ''
use_https = False
if(args.ssl_certificate and args.ssl_key):
    ssl_key_path = args.ssl_key
    ssl_certificate_path = args.ssl_certificate
    use_https = True

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Define a dictionary to map URLs to HTML content
        routes = {
            '/': 'index.html',
            '/about': 'about.html',
            '/contact': 'contact.html'
        }

        # Get the path requested by the client
        path = self.path

        # Check if the path is in the routes dictionary
        if path in routes:
            # Set the file to be served based on the route
            self.path = routes[path]
        else:
            # If the path is not found, serve the 404 page
            self.path = '404.html'

        # Call the superclass method to serve the file
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Define the server address and port
Handler = MyRequestHandler

# Change the working directory to 'public'
web_dir = os.path.join(os.path.dirname(__file__), directory)
os.chdir(web_dir)
# Create the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    if (use_https):
         # Create SSL context
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=ssl_certificate_path, keyfile=ssl_key_path)
        # Wrap the server's socket with SSL
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

        print(f'Serving HTTPS on 0.0.0.0 port {PORT} (https://0.0.0.0:{PORT}/) ...')
    else:
        print(f'Serving HTTP on 0.0.0.0 port {PORT} (http://0.0.0.0:{PORT}/) ...')
    try:
        # Serve until interrupted
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server.")
        httpd.shutdown()
        httpd.server_close()
