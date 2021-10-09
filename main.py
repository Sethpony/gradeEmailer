import smtplib

# create functions

sent_from = username_email
sent_to = ['email1', 'email2']
subject = 'Testing Testing'
body ='hi testing this automated email'


def createEmailBody():
    email_text = '''\
    From: %s
    To: %s
    Subject: %s
    %s
    ''' %(sent_from, sent_to, subject, body)

    return email_text


def sendEmail():
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

#create function that returns the variables that will be put into the email
#this will be looped

def messageVariables():
    #store information in dictionary
    #then use the key from the dictionary to return the value for the key:value pair

