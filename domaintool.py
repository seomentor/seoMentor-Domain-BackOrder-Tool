import os
import os.path
import requests
import json
from datetime import datetime, timedelta
from requests import Request, Session
# Welcome Message
print('Hello and Welcome to seoMentor Domain Purchase Automation Tool\nLet me check few things....')

def getwapi():
    if os.path.isfile('./Live DNS Project/whoisapikey.txt'):
        print('its look like its not your first time here. lets go!')
        pass
    else:
        print('Its look like you are first time here, lets start gather some information about you')
        wapi = input(f'Enter your "WhoisXMLAPI.com" API Key: ')
        wapifile = open('./Live DNS Project/whoisapikey.txt', "w+")
        wapifile.write(wapi)
        wapifile.close()
getwapi()

def getlivedns():
    if os.path.isfile('./Live DNS Project/livednsurl.txt'):
        pass
    else:
        print('Now i need your Live DNS Details, its lil bit long but you do it one time.')
        UserName = 'apidemo@livedns.co.il'
        Password = 'demo'
        RegistrantName = f'sapir%20zuberi'
        RegistrantEmail = 'zuberi'
        RegistrantAddress = 'avraham yafe 11'
        RegistrantCity = 'holon'
        RegistrantZipCode = '324234'
        RegistrantCountry = 'IL'
        RegistrantPhoneCountryCode = '972'
        RegistrantPhoneCityCode = '03'
        RegistrantPhoneNumber = '559282887'
        AdminNicHandle = 'shay'
        TechnicalNicHandle = 'adjkhas'
        ZoneNicHandle = 'asdasd'
        NS1 = 'asdasd'
        NS2 = 'asdasd'
        NS3 = 'asdasd'
        lapiurl = 'https://domains.livedns.co.il/API/DomainsAPI.asmx/NewDomain?'
        payload = {
            'UserName': UserName,
            'Password': Password,
            'RegistrantName': RegistrantName,
            'RegistrantEmail': RegistrantEmail,
            'RegistrantAddress': RegistrantAddress,
            'RegistrantCity': RegistrantCity,
            'RegistrantZipCode': RegistrantZipCode,
            'RegistrantCountry': RegistrantCountry,
            'RegistrantPhoneCountryCode': RegistrantPhoneCountryCode,
            'RegistrantPhoneCityCode': RegistrantPhoneCityCode,
            'RegistrantPhoneNumber': RegistrantPhoneNumber,
            'AdminNicHandle': AdminNicHandle,
            'TechnicalNicHandle': TechnicalNicHandle,
            'ZoneNicHandle': ZoneNicHandle,
            'NS1': NS1,
            'NS2': NS2,
            'NS3': NS3}
        ldfile = open('./Live DNS Project/livednsurl.txt', "w+")
        writeapi = f'https://domains.livedns.co.il/API/DomainsAPI.asmx/NewDomain?UserName={UserName}&Password={Password}&DomainName=&RegistrationPeriod=&RegistrantName={RegistrantName}&RegistrantEmail={RegistrantEmail}&RegistrantAddress={RegistrantAddress}&RegistrantCity={RegistrantCity}&RegistrantZipCode={RegistrantZipCode}&RegistrantCountry={RegistrantCountry}&RegistrantPhoneCountryCode={RegistrantPhoneCountryCode}&RegistrantPhoneCityCode={RegistrantPhoneCityCode}&RegistrantPhoneNumber={RegistrantPhoneNumber}&AdminNicHandle={AdminNicHandle}&TechnicalNicHandle={TechnicalNicHandle}&ZoneNicHandle={ZoneNicHandle}&NS1={NS1}&NS2={NS2}&NS3={NS3}'
        ldfile.write(str(writeapi))
        ldfile.close()
getlivedns()

# ask which domain he want to buy
domainBuy = str(input('Please Enter Domain Name: '))
def domaincheck(domainBuy):
    while '.co.il' not in domainBuy:
        domainBuy = str(input('please enter a valid input: '))
        if '.co.il' in domainBuy:
            print('Success')
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
wapiurl = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?'
#api payload
payload = {'apiKey': 'at_ibMNCbFfUGzZW41eRSXMKapbLUKEW', 'domainName': {domainBuy}, 'outputFormat': 'JSON'}
whois = requests.post(wapiurl, params=payload)
data = json.loads(whois.content)
current_date = data['WhoisRecord']['registryData']['expiresDate']
date_obj = datetime.strptime(current_date, '%d-%m-%Y')
print(date_obj)
print('This Domain will be available to register in' + str(date_obj) + str(timedelta(days=45)))
# ask the user if he want to buy this and set timer
qCheck2 = input('Are you want to schedule a purchase for this domain?: Y/N')
def questioncheck(qCheck2):
    while 'y' not in qCheck2:
        qCheck2 = str(input('Please choose the right answer: Y/N'))
    else:
        print('Ok let me check something')
questioncheck(qCheck2)
#check if its first time using and look for url.txt if exist
def clogin():
    if os.path.isfile('./url.txt'):
        urlfile = open("url.txt", "r")
        lines = urlfile.read()
        ldapi = lines
        r = requests.get(ldapi)
        print(r.headers)
    else:
        pass
