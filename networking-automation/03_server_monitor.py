import psutil
import time
import smtplib
from email.message import EmailMessage

def send_alert(subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "your_email@gmail.com" # Replace email 
    msg["To"] = "recipient_email@gmail.com" # Replace email 

    msg.set_content(body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_app_password") # Replace credentials 
    server.send_message(msg)
    server.quit()

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80

while True:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    if cpu_usage > CPU_THRESHOLD:
        send_alert(
            "CPU Alert",
            f"CPU usage is high: {cpu_usage}%"
        )

    if memory_usage > MEMORY_THRESHOLD:
        send_alert(
            "Memory Alert",
            f"Memory usage is high: {memory_usage}%"
        )

    time.sleep(60)



