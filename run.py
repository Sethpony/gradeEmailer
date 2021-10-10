# use this to process the job and run the application
from main import *

if __name__ == "__main__":

    csvtoDict()
    createJson()
    json_dict = csvtoDict()

    for x in range(len(json_dict['student_id'])):
        data_dict = {
            "sent_from": json_dict['my_email'][x],
            "parent_email": json_dict['parent_email'][x],
            "subject_email": json_dict['email_subject'][x],
            "parent_first": json_dict['parent_first'][x],
            "parent_last": json_dict['parent_last'][x],
            "student_first": json_dict['student_first'][x],
            "student_last": json_dict['student_last'][x],
            "grade": json_dict['current_grade'][x],
            "subject_class": json_dict['email_subject'][x],
            "missing_assignment": json_dict['number_missing_assignments'][x]
        }

        print(data_dict['sent_from'])
        print(data_dict['parent_email'])
        print(data_dict['subject_email'])
        print(data_dict['parent_first'])
        print(data_dict['parent_last'])
        print(data_dict['student_first'])
        print(data_dict['student_last'])
        print(data_dict['grade'])
        print(data_dict['subject_class'])
        print(data_dict['missing_assignment'])

        email_message = createEmailMessage(data_dict['sent_from'], data_dict['parent_email'],
                                           data_dict['subject_email'], data_dict['parent_first'],
                                           data_dict['parent_last'], data_dict['student_first'],
                                           data_dict['student_last'], data_dict['grade'], data_dict['subject_class'],
                                           data_dict['missing_assignment'])
        print(email_message)
