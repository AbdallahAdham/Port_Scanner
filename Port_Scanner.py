import socket

TARGET_IP = input("Enter the Target IP: ")

PortRange = input("Enter the Port Range (Ex. 5-25): ")

LowPort = int(PortRange.split('-')[0])
HighPort = int(PortRange.split('-')[1])

print("Scanning Host (", TARGET_IP, ") from port [", LowPort, "] to port [", HighPort, "]")

for port in range(LowPort, HighPort):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    status = s.connect_ex((TARGET_IP, port))

    if(status == 0):
        
        print("Port [", port, "] is OPENED")
        print("---------------------------")

    else:
        print("Port [", port, "] is CLOSED")
        print("---------------------------")

    s.close()
