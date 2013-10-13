import os
import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendEmails(subject, fromAddress, emailHtml, emailText, member_data):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From']    = fromAddress 
    member_info = member_data.values()
    
    username = 'givecamp2013@tbanks.org'
    password = '54I7zU4cVDJqAVAAoudnjg'
    s = smtplib.SMTP('smtp.mandrillapp.com', 587)
    s.login(username, password)
    
    for member in member_info:
        text = emailText.replace('{{first_name}}', member['first'])
        html = emailHtml.replace('{{first_name}}', member['first'])
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        msg['To'] = member['email']
        #print msg['From'], msg['To'], msg.as_string()
        #print ''
        s.sendmail(msg['From'], msg['To'], msg.as_string())

    s.quit()



