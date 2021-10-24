import smtplib
import pandas as pd
import json

csv_file_location = "C:/Users/spbac/PycharmProjects/gradeEmailer/grade_emailer_sheet_2.txt"
json_file_location = "C:/Users/spbac/PycharmProjects/gradeEmailer/shared_folder/storage.json"
def createEmailMessage(parent_first, parent_last, student_first, student_last,
                       grade, subject_class, missing_assignments):
    email_text ='''\
Subject: Students Grades
Hi Good Evening %s %s,

%s %s is receiving this grade: %s, in this subject: %s. 

They are missing: %s assignments.Thank you for reading.
    
Best, 
Teacher
    ''' % (parent_first, parent_last, student_first, student_last, grade,
           subject_class, missing_assignments)

    return email_text


# need to use config parser for this
def sendEmail(username_email, user_password, sent_from, sent_to, email_text):


    try:
        # instantiates a smtplib object open and creates the SSL connection to gmail on port 465
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        # from the created smtplib_server object activate login and password
        smtp_server.login(username_email, user_password)
        # act on method to send mail needing from, to, and the sent and to recipient information as well as body of email
        smtp_server.sendmail(sent_from, sent_to, email_text)
        smtp_server.close()
        print("email sent successfully")
    except Exception as ex:
        print("something went wrong", ex)


# create function that returns the variables that will be put into the email
# this will be looped

# def messageVariables():
#     #store information in dictionary
#     #then use the key from the dictionary to return the value for the key:value pair


def csvtoDict():
    csv_file = pd.read_csv(csv_file_location, sep='\t')
    to_dict = csv_file.to_dict()
    # print(to_dict)
    return to_dict


def createJson():
    json_dict = csvtoDict()
    with open(json_file_location, "w") as json_file:
        json.dump(json_dict, json_file, indent=2)


# csvtoDict()
# createJson()
