from netmiko import ConnectHandler
from getpass import getpass
import datetime
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
try:
    net_connect = ConnectHandler(**device)
    print("Connected successfully to the device.")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"ip_interface_status_{timestamp}.log"
    
    # log output of show ip interface brief command
    output = net_connect.send_command('show ip interface brief')
    with open(filename, "w") as f:
        f.write(output)
        print("ip interface status logged to:", filename)

    # Disconnect from the device
    net_connect.disconnect()
    print("Disconnected from the device.")
# error handling message
except Exception as e:
    print("Failed to connect to the device:", str(e))
