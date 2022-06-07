"""
Author: Kelvin Gooding
Created: 22/02/2022
Version: 1.002
"""

# Modules

import os
import win32com.client as win32

def mailbox():
    outlook = win32.Dispatch("outlook.application")
    mail = outlook.CreateItem(0)
    mail.To = "kelvingooding@msn.com"
    mail.Subject = f"Server Connectivity Issue - {hostname}"
    mail.Body = f"Unable to connect to {hostname}. Please check the connection and try again."
    mail.Send()

# google

hostname = "8.8.8.8 (Google Public DNS)"

print(f"Connecting to {hostname}")

response = os.popen(f"ping {hostname[:-20]}").read()

if "Destination host unreachable" in response:
    print(f"Unable to connect to {hostname}. Please check the connection and try again.\n")
    mailbox()
    pass
elif "Received = 4" in response:
    print(f"Connection established!\n")
else:
    print(f"Unable to connect to {hostname}. Please check the connection and try again.\n")
    mailbox()
    pass

# wolfmoon

hostname = "192.168.1.238 (wolfmoon)"

print(f"Connecting to {hostname}")

response = os.popen(f"ping {hostname[:-11]}").read()

if "Destination host unreachable" in response:
    print(f"Unable to connect to {hostname}. Please check the connection and try again.\n")
    mailbox()
    pass
elif "Received = 4" in response:
    print(f"Connection established!\n")
else:
    print(f"Unable to connect to {hostname}. Please check the connection and try again.\n")
    mailbox()
    pass

# snowmoon

hostname = "192.168.1.97 (snowmoon)"

print(f"Connecting to {hostname}")

response = os.popen(f"ping {hostname[:-11]}").read()

if "Destination host unreachable" in response:
    print(f"Unable to connect to {hostname}. Please check the connection and try again.\n")
    mailbox()
    pass
elif "Received = 4" in response:
    print(f"Connection established!\n")
else:
    print(f"Unable to connect to {hostname}. Please check the connection and try again.\n")
    mailbox()
    pass

# wormmoon

hostname = "192.168.1.88 (wormmoon)"

print(f"Connecting to {hostname}")

response = os.popen(f"ping {hostname[:-11]}").read()

if "Destination host unreachable" in response:
    print(f"Unable to connect to {hostname}. Please check the connection and try again.\n")
    mailbox()
    pass
elif "Received = 4" in response:
    print(f"Connection established!\n")
else:
    print(f"Unable to connect to {hostname}. Please check the connection and try again.\n")
    mailbox()
    pass

input("Press any key to exit..")
