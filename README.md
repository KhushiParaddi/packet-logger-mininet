# Packet Logger using Mininet

## 1. Overview

This project demonstrates packet-level monitoring in a virtual network environment using Mininet. Network traffic is generated between hosts and captured in real time using packet analysis tools.

The system identifies different types of packets such as ARP, ICMP, and TCP and logs relevant information including source, destination, and protocol.

---

## 2. Objectives

* Capture packets traversing the network
* Identify protocol types (ARP, ICMP, TCP)
* Log packet information
* Observe network behavior in a simulated environment

---

## 3. Tools Used

* Mininet (Network Emulator)
* Ubuntu Linux (Virtual Machine)
* tcpdump (Packet Capture Tool)

---

## 4. Network Topology

The topology consists of:

* 1 switch (s1)
* 3 hosts (h1, h2, h3)

All hosts are connected to a single switch using virtual Ethernet links.

---

## 5. Implementation Steps

### Step 1: Start Mininet

sudo mn --topo single,3

### Step 2: Open terminal for host

xterm h1

### Step 3: Capture packets

tcpdump -i h1-eth0 -n

### Step 4: Generate ICMP traffic

pingall

### Step 5: Generate TCP traffic

h1 iperf -s &
h2 iperf -c h1

### Step 6: Save logs

tcpdump -i h1-eth0 -n > logs.txt

---

## 6. Observations

### ARP

Used for mapping IP addresses to MAC addresses.

### ICMP

Observed during ping operations for connectivity testing.

### TCP

Observed during iperf execution for data transfer.

---

## 7. Test Scenarios

### Scenario 1: Connectivity Test

Command: pingall
Result: Successful communication with no packet loss

### Scenario 2: TCP Traffic Test

Command: iperf
Result: Successful data transfer between hosts

---

## 8. Results

* Packets were successfully captured in real time
* Protocol types were correctly identified
* Logs were stored for further analysis
* Network behavior was clearly observed

---

## 9. Files in Repository

* packet_logger.py
* logs.txt
* README.md

---

## 10. Conclusion

The project successfully demonstrates packet capture and analysis in a virtual network. It provides insight into how different network protocols operate and how traffic flows between nodes in a simulated environment.

---

## 11. Limitations

* Does not use a full SDN controller (Ryu/POX)
* Packet logging is performed at the host level

---

## 12. Future Improvements

* Integration with SDN controller for centralized control
* Implementation of filtering or firewall rules
* Advanced logging and traffic analysis

## Proof of Execution

![Screenshot 1](proof-of-exec/ss1.png)
<img width="581" height="337" alt="Screenshot 2026-04-19 114757" src="https://github.com/user-attachments/assets/77fed2cb-9511-4c7b-9b22-11401e377fb2" />

![Screenshot 2](proof-of-exec/ss2.png)
<img width="855" height="191" alt="Screenshot 2026-04-19 120746" src="https://github.com/user-attachments/assets/1607713e-43dd-4106-9626-5fd8dac400a1" />

![Screenshot 3](proof-of-exec/ss3.png)
<img width="974" height="448" alt="Screenshot 2026-04-19 120816" src="https://github.com/user-attachments/assets/43e964ad-0403-4030-8c8a-cf07ef2e1d59" />

