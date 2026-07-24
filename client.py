import socket
import threading

SERVER_IP = input("Enter Server IP (Press Enter for localhost): ").strip()
if not SERVER_IP:
    SERVER_IP = '127.0.0.1'  

PORT = 5555
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((SERVER_IP, PORT))
except Exception as e:
    print(f" Could not connect to server: {e}")
    exit()

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print(" Connection closed by the server.")
            client.close()
            break

def write_messages():
    while True:
        text = input("")
        if text.strip():
            message = f"{nickname}: {text}"
            try:
                client.send(message.encode('utf-8'))
            except:
                print(" Failed to send message.")
                break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_messages()
