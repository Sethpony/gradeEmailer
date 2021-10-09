import pandas as pd
import json
csv_file = pd.read_csv("C:/Users/spbac/PycharmProjects/gradeEmailer2/gradeEmailer/grade_emailer_sheet.csv")
to_dict = csv_file.to_dict()
print(to_dict)

with open("C:/Users/spbac/PycharmProjects/gradeEmailer2/gradeEmailer/storage.json", "w") as json_file:
        json.dump(to_dict, json_file, indent=2)

#I think we should store the csv_file as a dictionary

#https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary

#iterate through dictionary to send the email