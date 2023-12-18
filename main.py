from twilio.rest import Client
import csv

account_sid = 'ACc4b773fb954a3188081b9985b11f791a'
auth_token = '0104ffd38139d79a9e83ada0706a6fd9'
client = Client(account_sid, auth_token)

fromNumber = '+18557298705'

class Message:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient
    def createAndSendMessage(self):
        self.message = client.messages.create(
        from_=fromNumber,
        body=self.message,
        to=self.recipient
)

def Main():
    with open('data.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        startLine = -1
        myFile=[]
        for lines in csvFile:
            myFile.append(lines)
        for i in range(len(myFile)):
            try:
                if int(myFile[i][0]) == 1:
                    startLine = i
            except:
                pass
    if startLine == -1:
        raise Exception('CSV Read Error: CSV lines not numbered properly/No line with the first cell labelled 1 found')



Main()

# myMessage = Message('testClass', '+18777804236')
# myMessage.createAndSendMessage()