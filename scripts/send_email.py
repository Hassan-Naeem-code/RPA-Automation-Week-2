"""
Simple Email Service for sending reports
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email(report_file, to_email="recipient@example.com", smtp_config=None):
    """Send email with report attachment."""
    
    # Default SMTP configuration (Gmail example)
    if smtp_config is None:
        smtp_config = {
            'server': 'smtp.gmail.com',
            'port': 587,
            'username': 'your_email@gmail.com',
            'password': 'your_app_password'
        }
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = smtp_config['username']
        msg['To'] = to_email
        msg['Subject'] = "Invoice Processing Report"
        
        # Email body
        body = """
        Hello,
        
        Please find attached the invoice processing report.
        
        Best regards,
        Automation System
        """
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach report file if it exists
        if os.path.exists(report_file):
            with open(report_file, 'rb') as attachment:
                part = MIMEApplication(attachment.read())
                part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(report_file))
                msg.attach(part)
        
        # Send email
        server = smtplib.SMTP(smtp_config['server'], smtp_config['port'])
        server.starttls()
        server.login(smtp_config['username'], smtp_config['password'])
        
        text = msg.as_string()
        server.sendmail(smtp_config['username'], to_email, text)
        server.quit()
        
        print(f"Email sent successfully to {to_email}")
        return True
        
    except Exception as e:
        print(f"Error sending email: {e}")
        print("Note: Configure SMTP settings to enable email functionality")
        return False

if __name__ == "__main__":
    report_file = "data/report.xlsx"
    
    # Demo mode - just show that email function exists
    print("Email service available. Configure SMTP settings to enable.")
    print(f"Would send report: {report_file}")
    
    # Uncomment to actually send email (after configuring SMTP)
    # send_email(report_file)
