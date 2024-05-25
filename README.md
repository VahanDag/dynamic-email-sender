# Dynamic Email Sender

This project allows you to send HTML formatted emails using Python. The project includes an HTML template (`email_template.html`) and a Python script (`send_email.py`). The HTML file creates the email template, and its contents can be dynamically replaced with values provided in the Python code. The project was created for the "Muamma" project, but anyone can download and modify the HTML template to suit their needs. The code is written to be compatible with MIME format.

## Features

- Send HTML formatted emails
- Dynamic content replacement in HTML template
- Compatible with MIME format
- Easy to configure and extend

## Getting Started

To start using this repository, follow the steps below:

### Prerequisites

- Python 3.x
- An email account to send emails (e.g., Gmail, Outlook)

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/VahanDag/dynamic-email-sender.git
    cd dynamic-email-sender
    ```

2. **Install required packages:**

    Ensure you have the necessary packages installed. You can install them using pip:

    ```bash
    pip install smtplib email
    ```

3. **Configure the email settings:**

    Open the `send_email.py` file and update the email account information with your own credentials:

    ```python
    smtp_server = 'smtpout.secureserver.net' # change your server(if needed)
    smtp_port = 465
    email_user = 'YOUR_EMAIL_HERE'
    email_password = 'YOUR_PASSWORD_HERE'
    ```

4. **Customize the email template:**

    Modify the `email_template.html` file to create your desired email template. Use placeholders (e.g., `{{title}}`) that will be replaced with dynamic content.

5. **Provide the template data:**

    Update the `template_data` dictionary in the `send_email.py` file with the dynamic content for your email:

    ```python
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
    ```

6. **Run the script:**

    Execute the `send_email.py` script to send an email:

    ```bash
    python send_email.py
    ```


## Contact

For any inquiries, please contact vahandag@gmail.com

---

Enjoy using the Muamma Email Sender and customize it to fit your needs!
