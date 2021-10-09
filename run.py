#use this to process the job and run the application
from main import *

if __name__ == "__main__":
    csvtoDict()
    #insert and loop paramaters while sending each one
    createEmailBody()
    sendEmail()
