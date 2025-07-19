import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email_with_attachment(subject, body, to_emails, from_email, smtp_user, smtp_pass, attachment_path):
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject

    # Tambah body teks
    msg.attach(MIMEText(body, "html"))

    # Tambah file attachment
    with open(attachment_path, "rb") as f:
        part = MIMEApplication(f.read(), Name="test_report.html")
        part['Content-Disposition'] = 'attachment; filename="test_report.html"'
        msg.attach(part)

    # Kirim email via Gmail SMTP
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.sendmail(from_email, to_emails, msg.as_string())
            print("Email report sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
