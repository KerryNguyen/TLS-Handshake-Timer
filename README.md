# TLS-Handshake-Timer

To get started, download the Python files and generate your key / cert files in the same directory.
I recommend you put the Python files in a new folder.

- Be sure to have OpenSSL installed on your machine.
<li>https://github.com/openssl/openssl</li>

# Generating Key / Cert files
Go onto your terminal and run:
<li>openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"</li>

<h2> BE SURE THAT THE KEY AND CERT FILES ARE IN THE SAME DIRECTORY AS THE PYTHON SCRIPTS</h2>

# Running the Python scripts
<h2>If you don't do this, the script will give an error, saying that the server refused to connect.</h2>
Before you run the Python scripts, make sure you open an OpenSSL server with the corresponding TLS version the script by changing the [-min_protocol] value.
<br>
<br>
<li>openssl s_server -accept 6768 -cert cert.pem -key key.pem -min_protocol [TLS-Version] -cipher "ALL:@SECLEVEL=0"</li>
<br>
Once the server is up, you may run the Python script. It'll ask you how many handshakes to do and will output the results onto a text file.
<br>

# TLS-Version
When running the 'openssl s_server' command, be sure to use the TLS-version to whatever corresponds to the script version.
<ul>
  <li>TLSv1.1</li>
  <li>TLSv1.2</li>
  <li>TLSv1.3</li>
</ul>
