import requests
import json
from datetime import datetime, timedelta
# Welcome Message
print('Hello and Welcome to seoMentor Domain Purchase Automation Tool')

# ask which domain he want to buy
domainBuy = str(input('Please Enter Domain Name: '))
def domaincheck(domainBuy):
    while '.co.il' not in domainBuy:
        domainBuy = str(input('please enter a valid input: '))
        if '.co.il' in domainBuy:
            print('Succes')
domaincheck(domainBuy)

# Validation Question Before Start Whois
qCheck = input('ARE YOU READY TO FUCK THEM ALL?!?!: Y/N')
def questioncheck(qCheck):
    while 'y' not in qCheck:
        qCheck = str(input('PLEASE SAY YES!!!: Y/N'))
    else:
        print('Start')
questioncheck(qCheck)

# Check the domain

#api url
apiurl = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?'
#api payload
payload = {'apiKey': 'at_ibMNCbFfUGzZW41eRSXMKapbLUKEW', 'domainName': {domainBuy}, 'outputFormat': 'JSON'}
whois = requests.post(apiurl, params = payload)
data = json.loads(whois.content)
current_date = data['WhoisRecord']['registryData']['expiresDate']
date_obj = datetime.strptime(current_date, '%d-%m-%Y')
print(date_obj)
print('This Domain will be available to register in' + date_obj + timedelta(days=45))

# ask the user if he want to buy this and set timer

qCheck2 = input('Are you want to schedule a purchase for this domain?: Y/N')
def questioncheck(qCheck2):
    while 'y' not in qCheck2:
        qCheck2 = str(input('Please choose the right answer: Y/N'))
    else:
        print('Ok i need some more details')
questioncheck(qCheck2)

#

# Gathering LiveDNS DATA
#now in test mode
