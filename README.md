# HTTPServer Plus
### -> An improved version of Python's SimpleHTTPServer, created for redirection purposes.
I’m sharing this script because I found it incredibly useful, and I hope many of you will too.
Feel free to share any improvements or suggestions. Happy Hacking!
### Description
When I was perfoming a penetration test, I needed to host HTML files because the default Python server was downloading the files instead of rendering them. Additionally, the URLs couldn't contain dots. To solve this, I created a simple script to redirect users to specific HTML pages.

As shown in the image below, you can define routes. For example, if the user navigates to `localhost/about`, they will be redirected to `localhost/about.html`. This allows you to use clean URLs while still pointing to the desired HTML files.

<img src="https://github.com/user-attachments/assets/afab892a-b772-4f14-a81c-c8b41ef24876" alt="Defined-routes-example" width="260" height="94">

In the image below, you'll notice that the user received a `200` status code despite visiting `/about` instead of `/about.html`.

<img src="https://github.com/user-attachments/assets/dfe0d09a-c7ab-4981-bcc3-6afb47817b62" alt="Defined-routes-example2" width="461" height="121">

You can run the server with HTTPS, by using a self-signed certificate:

<img src="https://github.com/user-attachments/assets/2f3648a2-971c-441a-957d-1d6b30450c39" alt="78e0f69ba4ab9414512e6c6909c92865.png" width="712" height="77">

### Usage
```
usage: httpserver_plus.py [-h] [-p PORT] [-d DIRECTORY] [-sc [SSL_CERTIFICATE]] [-sk [SSL_KEY]]

An improved version of Pythons SimpleHTTPServer, created for redirection purposes.

Rerout Example: localhost/about -> localhost/about.html

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Specify Port to use.
  -d DIRECTORY, --directory DIRECTORY
                        Specify directory where .html pages are stored.
  -sc [SSL_CERTIFICATE], --ssl-certificate [SSL_CERTIFICATE]
                        Specify the path to SSL's .cert file, to use HTTPS.
  -sk [SSL_KEY], --ssl-key [SSL_KEY]
                        Specify the path to SSL's .key file, to use HTTPS.

[HTTP Usage Example]
 sudo python3 httpserver_plus.py -p <PORT> -d <path-to-directory-with-html-files>

[HTTPS Usage Example]
 1. Generate a self-signed SSL Certificate.
  openssl req -new -x509 -keyout server.key -out server.crt -days 365 -nodes
 2. Run the script with -sc and -sk flags.
  sudo python3 httpserver_plus.py -p <PORT> -d "<path-to-directory-with-html-files>" -sc "<path-to-server.crt-file>" -sk "<path-to-server.key-file>"
``
