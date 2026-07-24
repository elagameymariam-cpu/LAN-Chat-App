import socket
import threading

# 1. إدخال عنوان الـ IP والاسم
SERVER_IP = input("Enter Server IP (Press Enter for localhost): ").strip()
if not SERVER_IP:
    SERVER_IP = '127.0.0.1'  # العنوان الافتراضي للتشغيل على نفس الكومبيوتر

PORT = 5555
nickname = input("Choose your nickname: ")

# 2. إنشاء الـ Socket والاتصال بالسيرفر
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((SERVER_IP, PORT))
except Exception as e:
    print(f"❌ Could not connect to server: {e}")
    exit()

def receive_messages():
    """دالة استقبال الرسائل القادمة من السيرفر وعرضها في الشاشة"""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            # السيرفر بيطلب الاسم أول ما نتصل
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("❌ Connection closed by the server.")
            client.close()
            break

def write_messages():
    """دالة قراءة ما يكتبه المستخدم وإرساله للسيرفر"""
    while True:
        text = input("")
        if text.strip():
            message = f"{nickname}: {text}"
            try:
                client.send(message.encode('utf-8'))
            except:
                print("❌ Failed to send message.")
                break

# 3. تشغيل Thread خاص باستقبال الرسائل في الخلفية عشان الشاشة ما تتجمدش وأنت بتكتب
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# 4. تشغيل دالة إرسال الرسائل على الشاشة الرئيسية
write_messages()