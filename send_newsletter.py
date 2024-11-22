import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

# Email settings
sender_email = "vivalph12@gmail.com"
recipient_email = "vivalph4@gmail.com"
subject = f"Inventory Newsletter - {datetime.now().strftime('%d/%m/%Y')}"

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

# Attach email body
body = f"Dear Team,\n\nPlease find the attached inventory newsletter for {datetime.now().strftime('%d/%m/%Y')}.\n\nBest regards,\nYour Company"
msg.attach(MIMEText(body, 'plain'))

# Attach the PDF
with open("newsletter.pdf", "rb") as pdf_file:
    pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
    pdf_attachment.add_header('Content-Disposition', 'attachment', filename="newsletter.pdf")
    msg.attach(pdf_attachment)

# Send the email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, "rhtu vjdw cixs wesu")  # Use environment variables for security
server.send_message(msg)
server.quit()

print("Newsletter sent successfully!")
