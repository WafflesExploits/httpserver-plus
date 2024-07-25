#!/usr/bin/env python3
# Made by WafflesExploits
import argparse
import http.server
import socketserver
import os
import sys

parser = argparse.ArgumentParser(description='A simple http server to avoid using extensions.\n\nRerout Example: localhost/about -> localhost/about.html',epilog="[Usage Example]\nsudo python3 simple_http_server.py -p 80 -d <path-to-server-files>" ,formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-p','--port', type=str, help="Specify Port to use.")
parser.add_argument('-d','--directory', type=str, help="Specify directory where .html pages are stored.")

args = parser.parse_args()
# Checks
if(not args.port or not args.directory):
    parser.print_help()
    sys.exit()
# Define variables
PORT = int(args.port)
directory = args.directory

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
    print(f'Serving HTTP on 0.0.0.0 port {PORT} (http://0.0.0.0:{PORT}/) ...')
    try:
        # Serve until interrupted
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server.")
        httpd.shutdown()
        httpd.server_close()
