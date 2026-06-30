# TCP Multi-Client Chat Server

A Python-based TCP Multi-Client Chat Server that enables multiple clients to communicate simultaneously using TCP socket programming and multithreading. The project demonstrates real-time communication, concurrent client handling, chat logging, and network packet analysis using Wireshark.

---

## Features

- Multi-client communication using TCP sockets
- Concurrent client handling with multithreading
- Real-time message broadcasting
- Chat logging
- Graceful client connection and disconnection
- TCP packet analysis using Wireshark
- Network topology testing

---

## Technologies Used

- Python
- TCP Socket Programming
- Multithreading
- Computer Networks
- Wireshark
- Linux
- CSV
- Git & GitHub

---

## Project Structure

```
tcp-multi-client-chat-server/
│
├── server.py
├── client.py
├── graph.py
├── performance_results.csv
├── chat_log.txt
├── Report.pdf
├── SCREENSHOTS/
└── README.md
```

---

## How to Run

### Start the Server

```bash
python server.py
```

### Start Client 1

```bash
python client.py
```

### Start Additional Clients

Open multiple terminals and run:

```bash
python client.py
```

Clients can communicate with each other in real time through the server.

---

## Screenshots

### Network Topology

![Network Topology](SCREENSHOTS/net.png)

---

### Multiple Clients Connected

![Multi Client Chat](SCREENSHOTS/multi_client_chat.png)

---

### Chat Message Exchange

![Chat Message](SCREENSHOTS/chat_message.png)

---

### Broadcast Message

![Broadcast Message](SCREENSHOTS/broadcast_message.png)

---

### Chat Log

![Chat Log](SCREENSHOTS/chat_log.png)

---

### TCP Handshake (Wireshark)

![TCP Handshake](SCREENSHOTS/tcp_handshake.png)

---

### Wireshark Packet Capture

![Wireshark Capture](SCREENSHOTS/wireshark_capture.png)

---

### PingAll Verification

![PingAll](SCREENSHOTS/topology_pingall.png)

---

### Connection Closed Successfully

![Connection Close](SCREENSHOTS/connection_close.png)

---

## Network Configuration

### Host IP Configuration

**Host H1**

![H1](SCREENSHOTS/h1%20ifconfig.png)

**Host H2**

![H2](SCREENSHOTS/h2%20ifconfig.png)

**Host H3**

![H3](SCREENSHOTS/h3%20ifconfig.png)

**Host H4**

![H4](SCREENSHOTS/h4%20ifconfig.png)

---

## Learning Outcomes

- TCP Socket Programming
- Client-Server Architecture
- Multithreading in Python
- Network Communication
- TCP Three-Way Handshake
- Packet Analysis using Wireshark
- Concurrent Programming
- Chat Application Development

---

## Author

**Khatija Fathima**

B.Tech Computer Science & Engineering  
Andhra University College of Engineering

GitHub: https://github.com/Khatija-Fathima
