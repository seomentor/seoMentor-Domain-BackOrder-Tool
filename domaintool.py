import os
import os.path
import requests
import json
from datetime import datetime, timedelta

# Welcome Message
print('Hello and Welcome to seoMentor Domain Purchase Automation Tool\nLet me check few things....')

# Ask the user which domain he want to buy
domainBuy = str(input('Please Enter Domain Name: '))
def domaincheck(domainBuy):
    while '.co.il' not in domainBuy:
        domainBuy = str(input('please enter a valid input: '))
        if '.co.il' in domainBuy:
            print('Lets Check when this domain will be available to purchase')
domaincheck(domainBuy)

# Ask the user what the period he want
periodd = input('Please enter the period time u want: ')

# Collect WhoisXMLAPI Api key from the user

def getwapi():
    if os.path.isfile("whoisapikey.txt"):
        print('its look like its not your first time here. lets go!')
        pass
    else:
        print('Its look like you are first time here, lets start gather some information about you')
        wapifile = open("whoisapikey.txt", "w+")
        wapi = input(f'Enter your "WhoisXMLAPI.com" API Key: ')
        wapifile.write(wapi)
        wapifile.close()
getwapi()

# Collect Live DNS User Information from the user

def getlivedns():
        print('Now i need your Live DNS Details')
        UserName = 'apidemo@livedns.co.il'
        Password = 'demo'
        DomainName = domainBuy
        RegistrationPeriod = periodd
        RegistrantName = f'sapir%20zuberi'
        RegistrantEmail = 'zuberi@zuberi.co.il'
        RegistrantAddress = f'avraham%20yafe%201'
        RegistrantCity = 'holon'
        RegistrantZipCode = '324234'
        RegistrantCountry = 'il'
        RegistrantPhoneCountryCode = '972'
        RegistrantPhoneCityCode = '055'
        RegistrantPhoneNumber = '9282887'
        AdminNicHandle = 'LD-SZ4136'
        TechnicalNicHandle = 'LD-SZ4136'
        ZoneNicHandle = 'LD-SZ4136'
        NS1 = 'ns1.upress.io'
        NS2 = 'ns2.upress.io'
        NS3 = 'ns3.upress.io'
        ldfile = open("livednsurl.txt", "w+")
        writeapi = f'https://domains.livedns.co.il/API/DomainsAPI.asmx/NewDomain?UserName={UserName}&Password={Password}&DomainName={DomainName}&RegistrationPeriod={RegistrationPeriod}&RegistrantName={RegistrantName}&RegistrantEmail={RegistrantEmail}&RegistrantAddress={RegistrantAddress}&RegistrantCity={RegistrantCity}&RegistrantZipCode={RegistrantZipCode}&RegistrantCountry={RegistrantCountry}&RegistrantPhoneCountryCode={RegistrantPhoneCountryCode}&RegistrantPhoneCityCode={RegistrantPhoneCityCode}&RegistrantPhoneNumber={RegistrantPhoneNumber}&AdminNicHandle={AdminNicHandle}&TechnicalNicHandle={TechnicalNicHandle}&ZoneNicHandle={ZoneNicHandle}&NS1={NS1}&NS2={NS2}&NS3={NS3}'
        ldfile.write(str(writeapi))
        ldfile.close()
getlivedns()

# Check the domain via whoisxmlapi.com and take the expired date

def WhoIsApi():
    print('Lets check the domain you want and see when its available')
    wapiurl = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?'
    payload = {'apiKey': 'at_ibMNCbFfUGzZW41eRSXMKapbLUKEW', 'domainName': {domainBuy}, 'outputFormat': 'JSON'}
    request = requests.post(wapiurl, params=payload)
    response = json.loads(request.content)
    expired_date = response['WhoisRecord']['registryData']['expiresDate']
    date_obj = datetime.strptime(expired_date, '%d-%m-%Y')
    print('This Domain will be available to register in' + str(date_obj) + str(timedelta(days=45)))
WhoIsApi()

# ask the user if he want to buy this and set timer

qCheck2 = input('Are you want to schedule a purchase for this domain?: Y/N')
def questioncheck(qCheck2):
    while 'y' not in qCheck2:
        qCheck2 = str(input('Please choose the right answer: Y/N'))
    else:
        print('Ok let me check something')
questioncheck(qCheck2)

# Schedule and purchase the domain

def dlastpurchase():
    if os.path.isfile("livednsurl.txt"):
        apikeyfile = open("livednsurl.txt", "r")
        url = apikeyfile.read()
        r = requests.get(url)
        print(r.headers)
dlastpurchase()
