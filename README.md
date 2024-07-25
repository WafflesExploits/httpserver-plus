# SimpleHTTPServer Improved
### -> This is slightly improved version of Python's SimpleHTTPServer, created for redirection purposes.
### Description
When I was perfoming a penetration test, I needed to host HTML files because the default Python server was downloading the files instead of rendering them. Additionally, the URLs couldn't contain dots. To solve this, I created a simple script to redirect users to specific HTML pages.

As shown in the image below, you can define routes. For example, if the user navigates to `localhost/about`, they will be redirected to `localhost/about.html`. This allows you to use clean URLs while still pointing to the desired HTML files.

<img src="https://github.com/user-attachments/assets/afab892a-b772-4f14-a81c-c8b41ef24876" alt="Defined-routes-example" width="260" height="94">

### Usage
```bash
usage: simple_http_server.py [-h] [-p PORT] [-d DIRECTORY]

A simple http server to avoid using extensions.

Rerout Example: localhost/about -> localhost/about.html

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Specify Port to use.
  -d DIRECTORY, --directory DIRECTORY
                        Specify directory where .html pages are stored.

[Usage Example]
sudo python3 simple_http_server.py -p 80 -d <path-to-server-files>
``
