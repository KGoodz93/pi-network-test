"""
Author: Kelvin Gooding
Created: 22/02/2022
Version: 1.000
"""

# Modules

import os

# google

hostname = "8.8.8.8 (Google Public DNS)"
response = os.popen(f"ping {hostname[:-20]}").read()

if "Received = 4" in response:
    print(f"Connection established to: {hostname}")
else:
    print(f"Unable to connect to: {hostname}. Please check the connection and try again.")

# snowmoon

hostname = "192.168.1.97 (snowmoon)"
response = os.popen(f"ping {hostname[:-11]}").read()

if "Received = 4" in response:
    print(f"Connection established to: {hostname}")
else:
    print(f"Unable to connect to: {hostname}. Please check the connection and try again.")

# wolfmoon

hostname = "192.168.1.238 (wolfmoon)"
response = os.popen(f"ping {hostname[:-11]} ").read()

if "Received = 4" in response:
    print(f"Connection established to: {hostname}")
else:
    print(f"Unable to connect to: {hostname}. Please check the connection and try again.")

input("\nPress any key to exit..")
