from twilio.rest import Client
import csv

account_sid = 'ACc4b773fb954a3188081b9985b11f791a'
auth_token = 'AUTHTOKENHERE'
client = Client(account_sid, auth_token)

fromNumber = '+18557298705'
testRecipient = '+18777804236'
todesthisshowup

def createAndSendMessage(message, sender, recipient):
    if type(recipient) == list:
        for i in recipient:
            message = client.messages.create(
                from_=sender,
                body=message,
                to=i
            )
    elif type(recipient) == str:
        message = client.messages.create(
            from_=sender,
            body=message,
            to=recipient
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
    myNewFile = myFile[startLine:]
    # print(myFile,myNewFile)
    for i in myNewFile:
        for ii in range(int(i[2])):
            input(f"Press enter to start heat {ii+1} of {i[1]}")
            createAndSendMessage(f"{i[1]} heat {ii+1} starting now", fromNumber, [testRecipient])

        # print(myNewFile[i][1],myNewFile[i][2])
    # createAndSendMessage("test12345", fromNumber, '+18777804236')

 

Main()

# myMessage = Message('testClass', '+18777804236')
# myMessage.createAndSendMessage()
