#use this to process the job and run the application
from main import *

if __name__ == "__main__":
    #create json from excel file
    csvtoDict()
    #insert and loop paramaters while sending each one
    #get values in json where index = 0 to end of file

    createEmailBody()
    sendEmail()
