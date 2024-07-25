# HTTPServer Plus
### -> An slightly improved version of Python's SimpleHTTPServer, created for redirection purposes.
I’m sharing this script because I found it incredibly useful, and I hope many of you will too.
Feel free to share any improvements or suggestions. Happy Hacking!
### Description
When I was perfoming a penetration test, I needed to host HTML files because the default Python server was downloading the files instead of rendering them. Additionally, the URLs couldn't contain dots. To solve this, I created a simple script to redirect users to specific HTML pages.

As shown in the image below, you can define routes. For example, if the user navigates to `localhost/about`, they will be redirected to `localhost/about.html`. This allows you to use clean URLs while still pointing to the desired HTML files.

<img src="https://github.com/user-attachments/assets/afab892a-b772-4f14-a81c-c8b41ef24876" alt="Defined-routes-example" width="260" height="94">

In the image below, you'll notice that the user received a `200` status code despite visiting `/about` instead of `/about.html`.

<img src="https://github.com/user-attachments/assets/dfe0d09a-c7ab-4981-bcc3-6afb47817b62" alt="Defined-routes-example2" width="461" height="121">

You can also use HTTPS by using a self-signed certificate:

<img src="https://github.com/user-attachments/assets/2f3648a2-971c-441a-957d-1d6b30450c39" alt="78e0f69ba4ab9414512e6c6909c92865.png" width="712" height="77">

### Usage
```bash
usage: simple_http_server_improved.py [-h] [-p PORT] [-d DIRECTORY]

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
