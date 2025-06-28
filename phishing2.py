import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_phishing_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Replace with your SMTP port

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Connect to SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login with sender email and password
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)  # Send email
        print(f"Phishing email sent successfully to {recipient_email}")
        server.quit()
    except Exception as e:
        print(f"Failed to send phishing email: {e}")

# Example usage
sender_email = "aadilsamar46@gmail.com"  # Replace with attacker's email address
sender_password = "Samar786@"  # Replace with attacker's email password
recipient_email = "rayansamar403@gmail.com"  # Replace with victim's email address
subject = "Important: Security Alert"
message = ""

Dear User,

We have detected suspicious activity on your account. Please click the link below to verify your account details:
https://example.com/verify-account

Thank you,
IT Support Team
"""

# Send the phishing email
send_phishing_email(sender_email, sender_password, recipient_email, subject, message)
