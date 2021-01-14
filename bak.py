import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
import pandas as pd
import datetime

api_id = '2693209'
api_hash = '3fe9c8a13bc5bd85c03aabeb2e4ff54f'
token = '1595059626:AAEu6IwzKSQinnQO_1hB5hHoJ8RSSBrm-ms'

phone = '+919033717372'

client = TelegramClient('session', api_id, api_hash) 

client.connect() 

if not client.is_user_authorized(): 

	client.send_code_request(phone)
	client.sign_in(phone, input('Enter the code: ')) 

if __name__ == "__main__":

    rd = pd.read_excel("data.xlsx") #read dara =  rd
    #print(rd) # When You want to check data in inserted successfully uncomment print function
    
    today = datetime.datetime.now().strftime("%d-%m")
    # print(today) #Print This year For send Email


    yearNow = datetime.datetime.now().strftime("%Y")
    writeYr = []
    # This will add the current year to the excel sheet so that the mail does not go again

    for index , item in rd.iterrows():
        # print(index , item['Birthday'])

        birthday = item['Birthday'].strftime("%d-%m")
       # print(birthday)
        
        if (today  == birthday) and yearNow not in str(item['Year']):
            # print(item['Mobile'])
            client.send_message(f"+{item['Mobile']}", item['Dailogue'])
            writeYr.append(index)

        if (today  == birthday) and yearNow in str(item['Year']):
            print(f"Your wish mail alredy send to {item['Name']}")
    
    for i in writeYr:
        yr = rd.loc[i , 'Year']
        rd.loc[i , 'Year'] = str(yr) + ',' + str(yearNow)

    rd.to_excel('data.xlsx', index=False)


# ==================When Check All Details Send To EveryOne Comment Out This==================
        # try:
        #     client.send_message(f"+{item['Mobile']}", item['Demo'] + ' ' + item['Name'])
        # except:
        #     print(item['Name'])
# ============================================================================================

client.disconnect()