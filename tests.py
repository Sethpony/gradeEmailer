import os.path
from datetime import datetime

csv_file_location = "C:/Users/spbac/PycharmProjects/gradeEmailer/grade_emailer_sheet_2.txt"

def func():
    return 1

def test_func(function):
    assert function == 1, "test did not pass"

#test that the txt file was last saved as of today

def test_saved_today(file_location):
    file_last_saved = os.path.getctime(csv_file_location)
    file_last_saved_date_time = datetime.fromtimestamp(file_last_saved)
    month_saved = file_last_saved_date_time.month
    day_saved = file_last_saved_date_time.day

    current_date_time = datetime.now()
    current_month = current_date_time.month
    current_day = current_date_time.day

    assert month_saved == current_month, "save the file to save with current_month"
    assert day_saved == current_day


#RUN TESTS
test_saved_today(csv_file_location)
test_func(func())