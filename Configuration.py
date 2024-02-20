from netmiko import ConnectHandler
from getpass import getpass

# Define device parameters
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'cameron',
    'password': 'telecomS144',
    # 'port': 22,  # Change if using a different SSH port
    # 'secret': 'enable_password',  # Uncomment and provide enable password if necessary
}

# Connect to the device
try:
    net_connect = ConnectHandler(**device)
    print("Connected successfully to the device.")

    # Example: Sending a command and printing the output
    output = net_connect.send_command('show ip interface brief')
    print(output)

    # Disconnect from the device
    net_connect.disconnect()
    print("Disconnected from the device.")

except Exception as e:
    print("Failed to connect to the device:", str(e))