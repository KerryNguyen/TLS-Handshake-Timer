# TLS-Handshake-Timer

To get started, download the Python files and generate your key / cert files in the same directory.
I recommend you put the Python files in a new folder.

- Be sure to have OpenSSL installed on your machine.
https://github.com/openssl/openssl

# Generating Key / Cert files
Go onto your terminal and run:
<li>cd [the directory you've placed the Python files to]</li>
<li>openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"</li>

# Running the Python scripts
<li>cd [the directory you've placed the Python files to]</li>
<li>openssl s_server -accept 6768 -cert cert.pem -key key.pem -min_protocol [TLS-Version] -cipher "ALL:@SECLEVEL=0"</li>

# TLS-Version
When running the 'openssl s_server' command, be sure to use the TLS-version to whatever corresponds to the script version.
<ul>
  <li>TLSv1.1</li>
  <li>TLSv1.2</li>
  <li>TLSv1.3</li>
</ul>
