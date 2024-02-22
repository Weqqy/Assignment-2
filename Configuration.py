# Configuration Commands

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
# Config device
config = [
    'enable'
    'config t'
    'interface lo0',
    'ip address 10.1.1.1 255.255.255.255',
    'end',
]

# Connect to the device

net_connect = ConnectHandler(**device)
print("Connected successfully to the device.")

# Send configuration commands to the device
output = net_connect.send_config_set(config)
print("Configuration commands sent successfully.")
print("Output:")
print(output)

# Example: Sending a command and printing the output
output = net_connect.send_command('show ip interface brief')
print(output)

print("End of Script")

