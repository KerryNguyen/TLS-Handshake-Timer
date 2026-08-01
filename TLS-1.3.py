import os, ssl, socket, warnings, time, pyfiglet, subprocess

os.system('cls')
print(pyfiglet.figlet_format("TLS-1.3", font="smblock"))
warnings.filterwarnings("ignore", category=DeprecationWarning)

server = "3.17.14.10"
port = 6768
key = os.path.join(os.getcwd(), "key.pem")
cert = os.path.join(os.getcwd(), "cert.pem")

while True:
 user_input = input("How many trials? ")
 if user_input.isdigit() and int(user_input) > 0:
    req_trials = int(user_input)
    break
else:
   print("Enter a number.")

print()

# Make sure you've opened an OpenSSL server, or else it'll actively refuse
# Go into CMD or Powershell and enter:
# openssl s_server -accept 6768 -cert cert.pem -key key.pem -min_protocol TLSv1.3 -cipher "ALL:@SECLEVEL=0
# raw_sock = socket.create_connection(("localhost", port))

# Setting up the settings for the client
# We're setting it to ONLY use TLS 1.3
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.minimum_version = ssl.TLSVersion.TLSv1_3
ctx.maximum_version = ssl.TLSVersion.TLSv1_3

# This should unblock the old TLS 1.1 ciphers and disable security checks
# Not needed for TLS 1.2 / 1.3, but leaving it in is harmless.
ctx.set_ciphers("DEFAULT:@SECLEVEL=0")
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# A list to keep track of the measured time
# variable to keep track of the handshake's number
times = []
num = 0
timesheet = 'TLS-1.3.txt'

# time.perf is used because it's precise.
# We're wrapping it around the tls creation to measure the tls handshake. 

with open(timesheet, 'w') as log:
   
    for trials in range(req_trials):
        num += 1
        raw_sock = socket.create_connection((server, port))
        start = time.perf_counter()
        tls_sock = ctx.wrap_socket(raw_sock, server_hostname=server)
        end = time.perf_counter()
        elapsed_ms = (end - start) * 1000
        print(f"Handshake #{num}: {elapsed_ms:.3f}", file=log)
        times.append(elapsed_ms)
        tls_sock.close()

    print(f"\nResults:", file=log)
    print(f"Average: {sum(times) / len(times):.3f} ms", file=log)
    print(f"Min: {min(times):.3f} ms", file=log)
    print(f"Max: {max(times):.3f} ms", file=log)