import smtplib
import pandas as pd
import json


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
    csv_file = pd.read_csv("C:/Users/spbac/PycharmProjects/gradeEmailer/gradeEmailer/grade_emailer_sheet_2.txt", sep='\t')
    to_dict = csv_file.to_dict()
    # print(to_dict)
    return to_dict


def createJson():
    json_dict = csvtoDict()
    with open("C:/Users/spbac/PycharmProjects/gradeEmailer/gradeEmailer/shared_folder/storage.json", "w") as json_file:
        json.dump(json_dict, json_file, indent=2)


csvtoDict()
createJson()
# I think we should store the csv_file as a dictionary

# https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary

# iterate through dictionary to send the email


# test json work here
json_dict = csvtoDict()
# print(json_dict['student_id'])
# loop through each 'key' eg) student_id, student_first and then returns the value tied to that key
# def createEmailMessage(sent_from, parent_email, subject_email, parent_first, parent_last, student_first, student_last, grade, subject_class, missing_assignments)
# https://www.geeksforgeeks.org/read-json-file-using-python/
# instead of using json_dict use the created json file
for x in range(len(json_dict['student_id'])):
    sent_from = json_dict['my_email'][x]
    parent_email = json_dict['parent_email'][x]
    subject_email = json_dict['email_subject'][x]
    parent_first = json_dict['parent_first'][x]
    parent_last = json_dict['parent_last'][x]
    student_first = json_dict['student_first'][x]
    student_last = json_dict['student_last'][x]
    grade = json_dict['current_grade'][x]
    subject_class = json_dict['grade_subject'][x]
    missing_assignments = json_dict['number_missing_assignments'][x]

    # print(data_dict['missing_assignment'])
    email_message = createEmailMessage(parent_first, parent_last, student_first,
                                       student_last, grade, subject_class, missing_assignments)
    print(email_message)

# def createEmailMessage(sent_from, parent_email, subject_email, parent_first, parent_last, student_first, student_last, grade, subject_class, missing_assignments):
