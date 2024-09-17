import socket
import sys
import pyfiglet
from datetime import datetime

banner = pyfiglet.figlet_format("Port Scanner")
print(banner)

date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"Port-Scanner_{date}.txt"
print(f"Output file: {filename}")

try:
    file = open(filename, "w")
except Exception as e:
    print(f"Error opening file: {e}")
    sys.exit()

t1 = datetime.now()
print("Start Time: {}".format(t1.strftime("%H:%M:%S")))
file.write("Start Time: {}\n".format(t1.strftime("%H:%M:%S")))

target = input("Enter host to Scan: ")
host = socket.gethostbyname(target)

try:
    for port in range(1, 1025):
        #AF_INET is IPv4 AF_INET6 is IPv6, SOCK_STREAM is TCP SOCK_DGRAM is UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a more reasonable timeout

        result = sock.connect_ex((host, port))
        if result == 0:
            try:
                service_name = socket.getservbyport(port, "tcp")
            except socket.error:
                service_name = "unknown"
                
            print(f"Port No. : {port}      Open Protocol Service Name: {service_name}")
            file.write(f"Port No. : {port}      Open Protocol Service Name: {service_name}\n")
        #else:
         #   print(f"Port No. : {port} Closed")
          #  file.write(f"Port No. : {port} Closed\n")

except socket.gaierror:
    print("HostName could not be resolved. Exiting")
    file.write("\n\nHostName could not be resolved. Exiting\n")
    sys.exit()
except socket.error:
    print("Couldn't connect to server :(. Exiting")
    file.write("\n\nCouldn't connect to server :(. Exiting\n")
    sys.exit()

# End Time
t2 = datetime.now()
print("End Time: {}".format(t2.strftime("%H:%M:%S")))
file.write("End Time: {}\n".format(t2.strftime("%H:%M:%S")))

# Total Time
total_time = t2 - t1
print("Total Time: {}".format(total_time))
file.write("Total Time: {}\n".format(total_time))

file.close()
