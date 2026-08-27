# 🟣 Python Networking & Socket Programming

Month 8 – Day 27 | Python Practice Roadmap
A Python-based networking project that demonstrates how computers communicate using **sockets, IP addresses, ports, and TCP client-server architecture**.

The project implements **Programs 136–140 in a single Python file**.

---

## 🚀 Programs Implemented

### 136. Get Local IP Address

A simple program that retrieves and displays the computer's network information.

### Features

- Display hostname
- Display local IP address
- Display network IP address when available
- Handle network errors

Example:

```text
Hostname   : DESKTOP-ABC123
IP Address : 192.168.1.5
Network IP : 192.168.1.5

137. TCP Client–Server

Demonstrates basic TCP communication between a client and a server.

Server
Creates a socket
Binds to an IP address and port
Listens for a client
Accepts the connection
Receives a message
Sends a response
Client
Creates a socket
Connects to the server
Sends a message
Receives the server response

Example:

Client → Hello Server
Server → Message received by server!
138. Two-Way Communication

Demonstrates continuous communication between a TCP client and server.

Features
Client sends messages
Server receives messages
Server responds
Communication continues
exit command terminates communication

Example:

Client: Hello
Server: Hi!
Client: How are you?
Server: I am fine!
Client: exit
139. Simple Network File Transfer

Demonstrates how a small text file can be transferred from a client to a server.

Client
Selects a .txt file
Connects to the server
Sends the filename
Sends file contents
Server
Accepts the client
Receives the filename
Receives file data
Saves the file

Example:

sample.txt
       ↓
Client
       ↓
TCP Connection
       ↓
Server
       ↓
received_sample.txt
140. Mini LAN Chat Application

A basic client-server chat application using TCP sockets and threading.

Features
Server accepts a client
Client and server exchange messages
Messages can be sent continuously
Separate receiving thread
Clean exit mechanism
exit command terminates the chat

Example:

You: Hello!
Other: Hi!
You: How are you?
Other: Good!
You: exit
🛠️ Technologies Used
Python
Socket Programming
TCP
IP Addressing
Client-Server Architecture
Threading
File Handling
OS Module

🧠 Concepts Practiced
Socket programming
IPv4
Hostname
IP addresses
Ports
TCP
Client-server architecture
Network connections
socket()
bind()
listen()
accept()
connect()
sendall()
recv()
File transfer
Threading
Error handling
Network communication
📚 Learning Outcome

Through this project, I learned how Python can communicate between different processes and computers using socket programming.

I practiced creating TCP servers and clients, exchanging messages, transferring files, and building a basic chat application.

I also learned the fundamental flow of client-server communication and how IP addresses and ports are used to establish network connections.

🔮 Future Improvements
🌐 Support multiple clients
💬 Add group chat
🔐 Add authentication
🔒 Add encrypted communication
📁 Support larger file transfers
🖥️ Build a GUI chat application
👥 Add usernames
💾 Save chat history
📡 Add automatic client discovery
🌍 Build a multi-device messaging application
👨‍💻 Project Information

Month: 8
Day: 27
Programs: 136–140
Project: Python Networking & Socket Programming
Language: Python
Libraries: socket, threading, os
Protocol: TCP
Type: Networking & Client-Server Applications

🏷️ Tags

#Python #SocketProgramming #Networking #TCP #ClientServer #LAN #PythonProjects #NetworkProgramming #FileTransfer #ChatApplication #Programming #GitHub #LearningInPublic
