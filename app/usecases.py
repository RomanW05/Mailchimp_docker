import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import sys


'''
Use cases, aka business rules.
    - Create custom emails
    - Send emails to a list of subscribers
    - Generate stats


    
Create custom emails:
    - Load template
    - Replace placeholders for subscribers data
    - Create a simple hash value with the parameters: campaign id, template id and subscriber id

Generate stats:
    - Create percentages of success, opened emails, how far down the email, opened links
    - Retrive data from campaign status, filter by campaign

Send emails:
    - Retrieve a list of active subscribers
    - Send a personalized email
    - Update status of sent email
'''


def custom_email(encoded_params, name, html_template, plain_template, url):
    white_pixel = f'<img src="{url}/white_pixel/{encoded_params}">'
    unsubscribe_link = f'<a href="{url}/unsubscribe_subscriber/{encoded_params}">Unsubscribe</a>'

    html_template = html_template.replace('+subscriber_name+', name)
    html_template = html_template.replace('+unsubscribe_subscriber+', unsubscribe_link)
    html_template = html_template.replace('<head>', f'<head>{white_pixel}')
    html_template = html_template.replace('\n', '<br>')

    plain_template = plain_template.replace('+subscriber_name+', name)
    plain_template = plain_template.replace('+unsubscribe_subscriber+', unsubscribe_link)
    plain_template = plain_template.replace('\n', '<br>')


    return html_template, plain_template



def send_single_email(html_body, plain_body, subject, to, credentials):
    # to = 'sadsad@asdasd.asdasd'
    print('Sending email to:', to)
    server_credentials = credentials['server']
    from_email = credentials['email_address']
    password = credentials['password']
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to

    part1 = MIMEText(html_body, 'html')
    part2 = MIMEText(plain_body, 'plain')
    
    msg.attach(part1)
    msg.attach(part2)

    context = ssl.create_default_context()
    port = 465

    try:
        with smtplib.SMTP_SSL(server_credentials, port, context) as server:
            server.login(from_email, password)
            log = server.sendmail(from_email, [to], msg.as_string())
            if log == {}:
                return 'email sent'
            else:
                print('The email was not sent')
                return 'email not sent'
    except Exception as e:
        print('Error while sending the email with error:', e)
        return 'error'

