import smtplib
import pandas as pd
import json

# create functions

# sent_from = username_email
# sent_to = ['email1', 'email2']
# subject = 'Testing Testing'
# body ='hi testing this automated email'


def createEmailMessage(sent_from, parent_email, subject_email, parent_first, parent_last, student_first, student_last, grade, subject_class):
    email_text = '''\
    From: %s
    To: %s
    Subject: %s
    Hi %s %s your student %s %s, is receiving this grade:%s in this subject:%s. They are missing:%s assignments
    Thank you for reading
    
    Best, 
    Teacher
    ''' %(sent_from, parent_email, subject_email, parent_first, parent_last, student_first, student_last, grade, subject_class)

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

# def messageVariables():
#     #store information in dictionary
#     #then use the key from the dictionary to return the value for the key:value pair


def csvtoDict():
    csv_file = pd.read_csv("C:/Users/spbac/PycharmProjects/gradeEmailer/gradeEmailer/grade_emailer_sheet.txt", sep='\t')
    to_dict = csv_file.to_dict()
    print(to_dict)

    with open("C:/Users/spbac/PycharmProjects/gradeEmailer/gradeEmailer/shared_folder/storage.json", "w") as json_file:
        json.dump(to_dict, json_file, indent=2)


csvtoDict()
    # I think we should store the csv_file as a dictionary

    # https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary

    # iterate through dictionary to send the email

