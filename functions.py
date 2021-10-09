import pandas as pd
import json
csv_file = pd.read_csv("C:/Users/spbac/PycharmProjects/gradeEmailer2/gradeEmailer/grade_emailer_sheet.csv")
to_dict = csv_file.to_dict()
print(to_dict)

with open("C:/Users/spbac/PycharmProjects/gradeEmailer2/gradeEmailer/storage.json", "w") as json_file:
        json.dump(to_dict, json_file, indent=2)

