import smtplib

username_email = 'waddlewaddleanon@gmail.com'
user_password ='Punch123!'

sent_from = username_email

sent_to = ['itzelpz45@gmail.com', 'tehsethinator@gmail.com']
subject = 'Testing Testing'
body ='hi testing this automated email'

email_text = '''\
From: %s
To: %s
Subject: %s

%s
''' %(sent_from, sent_to, subject, body)

try:
    #instantiates a smtplib object open and creates the SSL connection to gmail on port 465
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    #from the created smtplib_server object activate login and password
    smtp_server.login(username_email, user_password)
    #act on method to send mail needing from, to, and the sent and to recipient information as well as body of email
    smtp_server.sendmail(sent_from, sent_to, email_text)
    smtp_server.close()
    print("email sent successfully")
except Exception as ex:
    print("something went wrong", ex)

