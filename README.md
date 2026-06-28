Network Performance Simulation for Hybrid Work Environments

This repository contains the Python implementation developed for the Computer Science Project (DLMCSPCSP01) at IU International University of Applied Sciences.

The project implements a virtual enterprise network using Python, Mininet, and Open vSwitch to evaluate the performance of hybrid work environments. The simulated topology represents remote users, VPN connectivity, corporate infrastructure, and cloud services while supporting controlled performance evaluation under different network conditions.

Technologies
Python 3
Mininet
Open vSwitch
Xubuntu 24.04 LTS
Oracle VirtualBox 7.2.8
iPerf
Implemented Features
Hybrid work network topology
Remote users, VPN gateway, corporate LAN, and cloud server
Configurable bandwidth limitations
Configurable transmission delay
Packet loss simulation
Connectivity verification using pingall
Latency evaluation using ICMP ping
Throughput evaluation using iPerf
Scalability testing with increasing numbers of users
Initial congestion analysis
Python-based topology implementation
Repository Structure
hybrid_topology.py
README.md
Requirements
Python 3
Mininet
Open vSwitch
iPerf
Running the Project

Start the topology:

sudo python3 hybrid_topology.py

After the Mininet CLI starts, verify connectivity:

pingall

Example latency test:

h1 ping -c 10 srv1

Example throughput test:

h1 iperf -c srv1

Exit Mininet:

exit
Author

Sahar Mansouri

IU International University of Applied Sciences

Computer Science Project (DLMCSPCSP01)