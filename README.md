Real-Time Multi-User LAN Chat Application
​Overview
​This is an individual software project that implements a real-time, multi-user text chat application designed to run over a Local Area Network. Developed entirely from scratch using standard Python, it demonstrates fundamental computer networking principles such as TCP socket programming and multithreading without using third-party frameworks.
​System Architecture
​The application follows a central Client-Server architecture. The server acts as a message router and connection manager, while client instances connect to it to exchange messages.
​Server Module: Listens for incoming connections, maintains a registry of active users, and broadcasts received messages to all participants.
​Client Module: Connects to the server IP address, prompts the user for a nickname, and handles incoming and outgoing message streams.
​Key Technical Concepts
​1. TCP Socket Communication
​The system utilizes Transmission Control Protocol through Python socket interface using the SOCK_STREAM configuration. TCP is selected to guarantee ordered, reliable, and error-checked data delivery across the network. The server binds to address 0.0.0.0 on port 5555, enabling it to accept requests from any network adapter on the host machine.
​2. Multithreading
​To prevent network operations and terminal inputs from blocking execution, multithreading is implemented on both ends:
​Server Multithreading: Every accepted client connection spawns an independent worker thread. This ensures that one user typing or experiencing network lag does not delay message processing for others.
​Client Multithreading: The client runs two parallel threads. A background thread listens for incoming broadcasts from the server, while the main thread captures terminal user input.
​3. Data Broadcast Flow
​When a user sends a text message, it is encoded into UTF-8 bytes and transmitted over TCP to the server. The server receives the byte payload in that client's dedicated handler thread, iterates over all active client socket instances, and forwards the payload to every participant.
​Project Files
​server.py: Contains the main server socket logic, client thread handler, and broadcasting function.
​client.py: Contains the connection setup, input handler, and background message receiver thread.
​README.md: Technical documentation and operational guide.
​Connection Validation & Testing Methods
​The application connection can be validated using two distinct approaches depending on the testing environment:
​Method 1: Local Single-Device Validation (Code Logic Test)
​Run server.py in the primary terminal window to start the server on port 5555.
​Open a second terminal tab, run client.py, press Enter for localhost (127.0.0.1), and enter a nickname (for example, Mona).
​Open a third terminal tab, run client.py again, press Enter for localhost, and enter a second nickname (for example, Ahmed).
​Send a message from Mona tab and verify that it immediately appears in Ahmed tab via the central server broadcast.
​Method 2: Multi-Device Network Validation (LAN Test)
​Run server.py on the host machine connected to a shared Wi-Fi network.
​Obtain the host machine IPv4 address using ipconfig or ifconfig (for example, 192.168.1.15).
​Run client.py on a second machine connected to the same Wi-Fi network.
​Enter the host IPv4 address when prompted, register a nickname, and verify bi-directional message exchange between the separate devices.
​Troubleshooting
​If devices on the same Wi-Fi network fail to connect to the host machine, ensure that port 5555 is allowed through the host system firewall settings and that all devices share the same IP subnet.