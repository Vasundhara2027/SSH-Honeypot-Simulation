# SSH-Honeypot-Simulation
SSH Honeypot Simulation in Python – a fake SSH server that mimics real SSH login prompts to log connection attempts. Captures IPs, usernames, and passwords, storing them in connections.log. Useful for learning honeypots, attacker behavior, and basic network security.

# SSH Honeypot Simulation

A simple SSH Honeypot written in Python that mimics an SSH server.  
It captures IPs, usernames, and passwords from connection attempts and logs them in `connections.log`.

## Features
- Fake SSH banner and login prompt  
- Logs connection attempts with IP, username, and password  
- Multi-threaded (handles multiple connections)

## Usage
```bash
python fake_server.py
