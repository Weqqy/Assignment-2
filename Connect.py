from netmiko import ConnectHandler
from getpass import getpass

# Define device parameters
password = getpass()
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.123.2',
    'username': 'admin',
    'password': password,
    # 'port': 22,  # Uncomment and change if using a different SSH port
    #'secret': 'enable_password',  # Uncomment and provide enable password if necessary
}

# Connect to the device

net_connect = ConnectHandler(**device)
print("Connected successfully to the device.")

# Disconnect from the device
net_connect.disconnect()
print("Disconnected from the device.")

