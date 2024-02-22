from netmiko import ConnectHandler
from getpass import getpass
import datetime

class CustomAuthenticationError(Exception):
    pass

def connect_to_device(device):
    try:
        # Attempt to connect to the device
        net_connect = ConnectHandler(**device)
        if net_connect:
            print("Connected successfully to the device.")

            # Generate timestamp for the log file
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"report_{timestamp}.log"

            # List of commands to be executed
            commands = [
                'show ip interface brief',
            ]

            # List to store command outputs and errors
            results = []

            # Execute commands and log the results
            for cmd in commands:
                result = {}
                result['command'] = cmd
                try:
                    output = net_connect.send_command(cmd)
                    result['output'] = output
                except Exception as e:
                    result['error'] = str(e)
                results.append(result)

            # Write results to the log file
            with open(filename, "w") as f:
                for result in results:
                    f.write(f"Command: {result['command']}\n")
                    if 'output' in result:
                        f.write("Output:\n")
                        f.write(result['output'])
                    if 'error' in result:
                        f.write("Error:\n")
                        f.write(result['error'])
                    f.write("\n\n")
            print("Report generated:", filename)

            # Disconnect from the device
            if net_connect.disconnect():
                print("Disconnected from the device.")
            else:
                print("Failed to disconnect from the device.")
        else:
            print("Failed to connect to the device.")

    except Exception as e:
        print("An unexpected error occurred:", str(e))

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

# Call the connect_to_device function
connect_to_device(device)
