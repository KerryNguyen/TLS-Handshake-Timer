# TLS-Handshake-Timer

To get started, download the Python files and generate your key / cert files in the same directory.
I recommend you put the Python files in a new folder.

- Be sure to have OpenSSL installed on your machine.

# Generating Key / Cert files
Go onto your terminal and run:
'cd <the directory you've downloaded the python files to'
'openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"'

# Running the Python scripts
'cd <the directory you've downloaded the python files to'
'openssl s_server -accept 6768 -cert cert.pem -key key.pem -min_protocol <TLS-Version> -cipher "ALL:@SECLEVEL=0"'

<TLS-Version> consists of TLSv1.1, TLSv1.2, and TLSv1.3.
