import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Enter your email account information here
smtp_server = 'smtpout.secureserver.net' # change your server(if needed)
smtp_port = 465
email_user = 'YOUR_EMAIL_HERE'
email_password = 'YOUR_PASSWORD_HERE'

# Read HTML template
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        template_content = file.read()
    return template_content

# Replace template with dynamic data
def fill_template(template, data):
    for key, value in data.items():
        template = template.replace(f'{{{{{key}}}}}', value)
    return template

def send_email(to_email, subject, plain_content, html_content):
    # Creating a MIME object
    msg = MIMEMultipart('alternative')
    msg['From'] = email_user
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add plain text and HTML content
    msg.attach(MIMEText(plain_content, 'plain'))
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Connecting to SMTP server and sending email
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(email_user, email_password)
        server.sendmail(email_user, to_email, msg.as_string())
        server.quit()
        print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

# Enter your email information and template data here
recipient_email = 'RECIPENT_EMAIL_ADDRESS'
email_subject = 'MAIL_TITLE'
template_file = 'email_template.html'

# Fill the HTML template 
template_data = {
    'title': 'Muamma Verification Code',
    'verificationCodeMessage': 'Here is your verification code:',
    'verificationCode': '112233',
    'codeTimeout': 'This code will expire in 10 minutes.',
    'emailSecurityMessage': 'For your security:',
    'emailSecurityArticle1': 'Do not share this code with anyone.',
    'emailSecurityArticle2': 'If you did not request this code, please ignore this email.',
    'emailSecurityArticle3': 'Contact us immediately if you suspect any suspicious activity.',
    'contactUsMessage': 'If you have any questions, feel free to contact us at',
    'copyright': '&copy; 2024 Muamma Team'
}

# Read and fill the template
email_template = read_template(template_file)
email_html_content = fill_template(email_template, template_data)

# Create plain text content
plain_content = (
    f"{template_data['title']}\n\n"
    f"{template_data['verificationCodeMessage']}\n"
    f"{template_data['verificationCode']}\n\n"
    f"{template_data['codeTimeout']}\n\n"
    f"{template_data['emailSecurityMessage']}\n"
    f"1. {template_data['emailSecurityArticle1']}\n"
    f"2. {template_data['emailSecurityArticle2']}\n"
    f"3. {template_data['emailSecurityArticle3']}\n\n"
    f"{template_data['contactUsMessage']} support@muamma.io\n\n"
    f"{template_data['copyright']}"
)

# Send email
send_email(recipient_email, email_subject, plain_content, email_html_content)