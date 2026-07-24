import socket
import threading

# 1. إعدادات الشبكة والـ Port
# HOST = '0.0.0.0' بيخلي السيرفر يسمع لأي أجهزة جاية من الـ LAN أو المحلية
HOST = '0.0.0.0'
PORT = 5555

# 2. إنشاء السوكت (TCP Socket)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# قوائم لحفظ المستخدِمين والـ Sockets الخاصة بيهم
clients = []
nicknames = []

def broadcast(message):
    """إرسال الرسالة لكل العملاء المتصلين"""
    for client in clients:
        try:
            client.send(message)
        except:
            # لو في مشكلة في الاتصال مع عميل معين
            pass

def handle_client(client):
    """استقبال وإدارة الرسائل لكل عميل متصل"""
    while True:
        try:
            # استقبال الرسالة من العميل (حجم البايت 1024)
            message = client.recv(1024)
            if message:
                broadcast(message)
            else:
                break
        except:
            break
            
    # في حالة خروج العميل أو انقطاع الاتصال
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        client.close()
        nickname = nicknames[index]
        nicknames.remove(nickname)
        broadcast(f'📢 {nickname} left the chat!'.encode('utf-8'))

def receive():
    """استقبال الاتصالات الجديدة باستمرار"""
    print(f"🚀 Server is running on port {PORT}...")
    while True:
        # قبول الاتصال الجديد
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # طلب اسم المستخدم عند الاتصال
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname is {nickname}")
        broadcast(f"📢 {nickname} joined the chat!".encode('utf-8'))
        client.send("✅ Connected to the server!".encode('utf-8'))

        # تشغيل Thread منفصل لكل عميل عشان يقدر السيرفر يتعامل مع الكل مع بعض
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()